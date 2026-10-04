"""
Agregação de "atividade recente" para a home e páginas de listagem.

Funções puras (sem Flask, sem banco): recebem os dados que já existem em
`data/` (projetos carregados por `listar_projetos()` e `certificados` de
`data/perfil.py`) e devolvem estruturas prontas para os templates. Isso evita
uma segunda fonte de verdade — tudo é derivado dos módulos de projeto.

Links são devolvidos como tuplas `(endpoint, params)`; quem renderiza (o
template, via `url_item`) resolve com `url_for`.

Datas opcionais aceitas em `home_card`:
    publicado_em   — quando o projeto foi publicado (datetime)
    atualizado_em  — última atualização relevante (datetime)
Sem elas, usa-se a data do post mais antigo / mais recente do projeto.
"""

import re
from datetime import date, datetime, timedelta

from markupsafe import Markup

JANELA_NOVO_DIAS = 30             # certificado "Novo" até N dias após a data
JANELA_NOVIDADE_BLOG_DIAS = 30    # projeto com badge "novidades no blog" até N dias após o último post
PALAVRAS_POR_MINUTO = 200
TAMANHO_RESUMO = 200


def _como_datetime(valor):
    if valor is None:
        return None
    if isinstance(valor, datetime):
        return valor
    if isinstance(valor, date):
        return datetime.combine(valor, datetime.min.time())
    return None


def texto_puro(html):
    """Remove tags e normaliza espaços. Devolve `str` simples (o Jinja escapa na saída)."""
    return " ".join(Markup(html or "").striptags().split())


def resumo_post(post, tamanho=TAMANHO_RESUMO):
    if post.get("resumo"):
        return post["resumo"]
    texto = texto_puro(post.get("conteudo", ""))
    if len(texto) <= tamanho:
        return texto
    return texto[:tamanho].rsplit(" ", 1)[0].rstrip(".,;:—-") + "…"


def tempo_leitura(post):
    """Minutos de leitura estimados (mínimo 1), a partir do conteúdo."""
    palavras = len(texto_puro(post.get("conteudo", "")).split())
    return max(1, round(palavras / PALAVRAS_POR_MINUTO))


def rotulo_relativo(data, agora=None):
    """'hoje', 'ontem', 'há 5 dias', 'há 2 semanas', 'há 3 meses', 'há 1 ano'."""
    data = _como_datetime(data)
    if data is None:
        return ""
    agora = agora or datetime.now()
    dias = (agora.date() - data.date()).days
    if dias <= 0:
        return "hoje"
    if dias == 1:
        return "ontem"
    if dias < 7:
        return f"há {dias} dias"
    if dias < 30:
        semanas = dias // 7
        return f"há {semanas} semana{'s' if semanas > 1 else ''}"
    if dias < 365:
        meses = dias // 30
        return f"há {meses} {'meses' if meses > 1 else 'mês'}"
    anos = dias // 365
    return f"há {anos} ano{'s' if anos > 1 else ''}"


def _recente(data, janela_dias, agora):
    data = _como_datetime(data)
    return data is not None and timedelta(0) <= agora - data <= timedelta(days=janela_dias)


# ------------------------------------------------------------------------------
# Posts
# ------------------------------------------------------------------------------

def _enriquecer_post(post, projeto):
    card = projeto.get("home_card") or {}
    return {
        "titulo": post["titulo"],
        "data": post["data"],
        "autor": post.get("autor", ""),
        "resumo": resumo_post(post),
        "tags": post.get("tags", []),
        "tempo_leitura": tempo_leitura(post),
        "imagem": post.get("imagem") or card.get("imagem"),
        "nome_projeto": projeto.get("ficha_tecnica", {}).get("nome", projeto["projeto"]),
        "link": ("ver_post", {"projeto": projeto["projeto"], "nome": post["nome_arquivo"]}),
        "link_projeto": ("blog_index", {"projeto": projeto["projeto"]}),
    }


def posts_recentes(projetos, limite=3):
    """Posts mais recentes entre todos os projetos (já carregados), do mais novo ao mais antigo."""
    todos = [_enriquecer_post(post, p) for p in projetos for post in p["posts"]]
    todos.sort(key=lambda x: x["data"], reverse=True)
    return todos[:limite]


# ------------------------------------------------------------------------------
# Projetos
# ------------------------------------------------------------------------------

def enriquecer_projetos(projetos, agora=None):
    """Cópia dos projetos com datas efetivas, último post e `novidade_blog`
    (True enquanto o post mais recente tem até JANELA_NOVIDADE_BLOG_DIAS dias)."""
    agora = agora or datetime.now()
    saida = []
    for p in projetos:
        card = p.get("home_card") or {}
        posts = sorted(p["posts"], key=lambda x: x["data"], reverse=True)

        publicado = _como_datetime(card.get("publicado_em")) or (_como_datetime(posts[-1]["data"]) if posts else None)
        atualizado = _como_datetime(card.get("atualizado_em")) or (_como_datetime(posts[0]["data"]) if posts else None)
        datas = [d for d in (publicado, atualizado) if d]
        ultima = max(datas) if datas else None

        saida.append({
            **p,
            "publicado_em": publicado,
            "atualizado_em": atualizado,
            "ultima_atividade": ultima,
            "novidade_blog": bool(posts) and _recente(posts[0]["data"], JANELA_NOVIDADE_BLOG_DIAS, agora),
            "status": p.get("ficha_tecnica", {}).get("status", ""),
            "ultimo_post": _enriquecer_post(posts[0], p) if posts else None,
            "total_posts": len(posts),
        })
    return saida


def ordenar_por_atividade(projetos):
    """Mais recentes primeiro; empates respeitam a `ordem` curada em home_card."""
    por_ordem = sorted(projetos, key=lambda p: (p["home_card"].get("ordem", 999), p["projeto"]))
    return sorted(por_ordem, key=lambda p: p["ultima_atividade"] or datetime.min, reverse=True)


# ------------------------------------------------------------------------------
# Certificados
# ------------------------------------------------------------------------------

def _horas(c):
    """Carga horária numérica de "330h" (0 se ausente)."""
    m = re.match(r"\s*(\d+)", c.get("carga_horaria", "") or "")
    return int(m.group(1)) if m else 0


def enriquecer_certificados(certificados, agora=None):
    """Cópia dos certificados com título curto, horas numéricas, link de verificação
    (None se não houver arquivo) e selo "novo"; ordenados do mais recente ao mais
    antigo (sem data vão ao fim, na ordem original)."""
    agora = agora or datetime.now()
    saida = []
    for c in certificados:
        titulo = c["titulo"]
        instituicao = c.get("instituicao", "")
        sufixo = f" - {instituicao}"
        arquivo = c.get("documento") or c.get("imagem_full")
        saida.append({
            **c,
            "titulo_curto": titulo[: -len(sufixo)] if instituicao and titulo.endswith(sufixo) else titulo,
            "horas": _horas(c),
            "recencia": "novo" if _recente(c.get("data"), JANELA_NOVO_DIAS, agora) else None,
            "link": ("static", {"filename": arquivo}) if arquivo else None,
        })
    com_data = sorted((c for c in saida if c.get("data")), key=lambda c: c["data"], reverse=True)
    return com_data + [c for c in saida if not c.get("data")]


def resumo_certificados(certificados, temas_ordem=()):
    """Totais para o cabeçalho e agrupamento por tema:
    {"total", "horas", "temas": [{"nome", "total", "horas"}, ...]}
    Temas na ordem de `temas_ordem` (os demais, por quantidade, depois)."""
    por_tema = {}
    for c in certificados:
        tema = c.get("tema") or "Outros"
        g = por_tema.setdefault(tema, {"nome": tema, "total": 0, "horas": 0})
        g["total"] += 1
        g["horas"] += c.get("horas", _horas(c))
    ordem = {nome: i for i, nome in enumerate(temas_ordem)}
    temas = sorted(por_tema.values(), key=lambda g: (ordem.get(g["nome"], len(ordem)), -g["total"]))
    return {"total": len(certificados), "horas": sum(g["horas"] for g in temas), "temas": temas}


def separar_certificados(certificados):
    """(destaques, demais). Sem nenhum `destaque` marcado, todos contam como destaque."""
    destaques = [c for c in certificados if c.get("destaque")]
    if not destaques:
        return list(certificados), []
    return destaques, [c for c in certificados if not c.get("destaque")]


# ------------------------------------------------------------------------------
# Feed
# ------------------------------------------------------------------------------

def eventos_atividade(projetos, certificados, limite=6, agora=None):
    """Feed unificado (projeto novo/atualizado, post novo, certificação nova).

    `projetos` = saída de `enriquecer_projetos`; `certificados` = de
    `enriquecer_certificados`. Projetos só geram evento quando `publicado_em` /
    `atualizado_em` foram declarados em `home_card` (as datas inferidas pelos
    posts servem aos selos, mas não viram "evento" para não duplicar posts).
    Itens com data no futuro ou sem data são ignorados.
    """
    agora = agora or datetime.now()
    eventos = []

    for p in projetos:
        card = p["home_card"]
        nome = p.get("ficha_tecnica", {}).get("nome", p["projeto"])
        link = ("blog_index", {"projeto": p["projeto"]})
        publicado = _como_datetime(card.get("publicado_em"))
        atualizado = _como_datetime(card.get("atualizado_em"))
        if publicado:
            eventos.append({"tipo": "projeto", "rotulo": "Novo projeto", "icone": "fa-rocket",
                            "titulo": nome, "contexto": "Projeto publicado", "data": publicado, "link": link,
                            "imagem": card.get("imagem"), "resumo": card.get("resumo", ""), "cta": "Ver projeto"})
        if atualizado and atualizado != publicado:
            eventos.append({"tipo": "atualizacao", "rotulo": "Projeto atualizado", "icone": "fa-arrows-rotate",
                            "titulo": nome, "contexto": "Atualização do projeto", "data": atualizado, "link": link,
                            "imagem": card.get("imagem"), "resumo": card.get("resumo", ""), "cta": "Ver projeto"})
        for post in p["posts"]:
            ev = _enriquecer_post(post, p)
            eventos.append({"tipo": "post", "rotulo": "Novo artigo", "icone": "fa-pen-nib",
                            "titulo": ev["titulo"], "contexto": ev["nome_projeto"],
                            "data": _como_datetime(post["data"]), "link": ev["link"],
                            "imagem": ev["imagem"], "resumo": ev["resumo"], "cta": "Ler artigo"})

    # Dezenas de certificados não podem virar dezenas de slides: um evento por mês.
    por_mes = {}
    for c in certificados:
        data = _como_datetime(c.get("data"))
        if data and data <= agora:
            por_mes.setdefault((data.year, data.month), []).append(c)
    for grupo in por_mes.values():
        grupo.sort(key=lambda c: c["data"], reverse=True)
        maior = max(grupo, key=lambda c: (c.get("horas", 0), c["data"]))
        imagem = next((x.get("imagem_preview") or x.get("imagem_full") for x in [maior] + grupo
                       if x.get("imagem_preview") or x.get("imagem_full")), None)
        if len(grupo) == 1:
            c = grupo[0]
            partes = [c.get("instituicao"), c.get("carga_horaria")]
            eventos.append({"tipo": "certificado", "rotulo": "Nova certificação", "icone": "fa-award",
                            "titulo": c["titulo_curto"], "contexto": " · ".join(x for x in partes if x),
                            "data": c["data"], "link": c["link"] or ("certificados_lista", {}),
                            "externo": bool(c["link"]), "imagem": imagem, "resumo": c.get("descricao", ""),
                            "cta": "Ver certificado" if c["link"] else "Ver certificações"})
            continue
        horas = sum(c.get("horas", 0) for c in grupo)
        temas = [g["nome"] for g in resumo_certificados(grupo)["temas"][:3]]
        eventos.append({"tipo": "certificado", "rotulo": "Novas certificações", "icone": "fa-award",
                        "titulo": f"{len(grupo)} certificações concluídas",
                        "contexto": f"{horas}h de estudo" if horas else "",
                        "data": grupo[0]["data"], "link": ("certificados_lista", {}), "externo": False,
                        "imagem": imagem, "resumo": "Temas: " + ", ".join(temas) + ".", "cta": "Ver certificações"})

    eventos = [e for e in eventos if e["data"] and e["data"] <= agora]
    eventos.sort(key=lambda e: e["data"], reverse=True)
    for e in eventos:
        e["relativo"] = rotulo_relativo(e["data"], agora)
    return eventos[:limite]
