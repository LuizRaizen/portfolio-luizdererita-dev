import unittest
from datetime import datetime

from utils import atividade as at

AGORA = datetime(2026, 6, 15, 12, 0)


def projeto(slug, posts, **card):
    return {
        "projeto": slug,
        "ficha_tecnica": {"nome": slug.title(), "status": "Em produção"},
        "home_card": {"categoria": "web", "imagem": f"img/{slug}.webp", "ordem": 10, **card},
        "posts": posts,
    }


def post(nome, data, conteudo="<p>Texto do post</p>", **extra):
    return {"titulo": nome, "data": data, "autor": "L", "nome_arquivo": nome, "conteudo": conteudo, **extra}


class RotuloRelativo(unittest.TestCase):
    def test_faixas(self):
        casos = {
            datetime(2026, 6, 15): "hoje",
            datetime(2026, 6, 14): "ontem",
            datetime(2026, 6, 10): "há 5 dias",
            datetime(2026, 6, 1): "há 2 semanas",
            datetime(2026, 4, 1): "há 2 meses",
            datetime(2025, 6, 1): "há 1 ano",
        }
        for data, esperado in casos.items():
            self.assertEqual(at.rotulo_relativo(data, AGORA), esperado)


class Posts(unittest.TestCase):
    def test_resumo_remove_html_e_trunca(self):
        p = post("a", AGORA, conteudo="<h2>Oi</h2><p>" + "palavra " * 100 + "</p>")
        r = at.resumo_post(p)
        self.assertNotIn("<", r)
        self.assertLessEqual(len(r), at.TAMANHO_RESUMO + 1)
        self.assertTrue(r.endswith("…"))

    def test_resumo_explicito_tem_prioridade(self):
        self.assertEqual(at.resumo_post(post("a", AGORA, resumo="Meu resumo")), "Meu resumo")

    def test_tempo_leitura_minimo_um(self):
        self.assertEqual(at.tempo_leitura(post("a", AGORA)), 1)
        self.assertEqual(at.tempo_leitura(post("a", AGORA, conteudo="palavra " * 600)), 3)

    def test_recentes_ordenados_entre_projetos(self):
        ps = [
            projeto("x", [post("x1", datetime(2026, 1, 1)), post("x2", datetime(2026, 3, 1))]),
            projeto("y", [post("y1", datetime(2026, 2, 1))]),
        ]
        nomes = [p["titulo"] for p in at.posts_recentes(ps, 2)]
        self.assertEqual(nomes, ["x2", "y1"])


class Projetos(unittest.TestCase):
    def test_datas_inferidas_dos_posts(self):
        p = projeto("x", [post("a", datetime(2026, 6, 1)), post("b", datetime(2026, 1, 1))])
        r = at.enriquecer_projetos([p], AGORA)[0]
        self.assertEqual(r["publicado_em"], datetime(2026, 1, 1))
        self.assertEqual(r["atualizado_em"], datetime(2026, 6, 1))
        self.assertEqual(r["ultimo_post"]["titulo"], "a")

    def test_novidade_blog_dentro_da_janela(self):
        p = projeto("x", [post("a", datetime(2026, 6, 10)), post("b", datetime(2026, 1, 1))])
        self.assertTrue(at.enriquecer_projetos([p], AGORA)[0]["novidade_blog"])

    def test_novidade_blog_expira(self):
        p = projeto("x", [post("a", datetime(2026, 5, 1))])  # 45 dias
        self.assertFalse(at.enriquecer_projetos([p], AGORA)[0]["novidade_blog"])

    def test_novidade_blog_usa_so_posts_nao_a_data_do_projeto(self):
        p = projeto("x", [post("a", datetime(2025, 1, 1))], publicado_em=datetime(2026, 6, 14))
        self.assertFalse(at.enriquecer_projetos([p], AGORA)[0]["novidade_blog"])

    def test_sem_posts(self):
        r = at.enriquecer_projetos([projeto("x", [])], AGORA)[0]
        self.assertFalse(r["novidade_blog"])
        self.assertIsNone(r["ultimo_post"])

    def test_ordenacao_por_atividade_com_desempate_pela_ordem(self):
        a = projeto("a", [post("p", datetime(2026, 1, 1))], ordem=20)
        b = projeto("b", [post("p", datetime(2026, 1, 1))], ordem=10)
        c = projeto("c", [post("p", datetime(2026, 5, 1))], ordem=99)
        ordem = [p["projeto"] for p in at.ordenar_por_atividade(at.enriquecer_projetos([a, b, c], AGORA))]
        self.assertEqual(ordem, ["c", "b", "a"])

    def test_nao_muta_entrada(self):
        p = projeto("x", [post("a", AGORA)])
        at.enriquecer_projetos([p], AGORA)
        self.assertNotIn("recencia", p)


class Certificados(unittest.TestCase):
    CERT = {"titulo": "Curso - Escola", "instituicao": "Escola", "categoria": "online",
            "imagem_thumb": "t.webp", "imagem_full": "f.png"}

    def test_titulo_curto_e_link(self):
        c = at.enriquecer_certificados([self.CERT], AGORA)[0]
        self.assertEqual(c["titulo_curto"], "Curso")
        self.assertEqual(c["link"], ("static", {"filename": "f.png"}))

    def test_separar_sem_destaque_mantem_todos_em_destaque(self):
        d, o = at.separar_certificados([self.CERT, self.CERT])
        self.assertEqual((len(d), len(o)), (2, 0))

    def test_separar_com_destaque(self):
        d, o = at.separar_certificados([{**self.CERT, "destaque": True}, self.CERT])
        self.assertEqual((len(d), len(o)), (1, 1))


class Feed(unittest.TestCase):
    def test_feed_mistura_tipos_ordena_e_ignora_futuro_e_sem_data(self):
        ps = at.enriquecer_projetos([
            projeto("x", [post("p1", datetime(2026, 6, 1))], publicado_em=datetime(2026, 5, 1)),
        ], AGORA)
        certs = at.enriquecer_certificados([
            {"titulo": "Novo", "categoria": "online", "imagem_thumb": "t", "data": datetime(2026, 6, 10)},
            {"titulo": "Futuro", "categoria": "online", "imagem_thumb": "t", "data": datetime(2027, 1, 1)},
            {"titulo": "SemData", "categoria": "online", "imagem_thumb": "t"},
        ], AGORA)
        ev = at.eventos_atividade(ps, certs, 10, AGORA)
        self.assertEqual([e["tipo"] for e in ev], ["certificado", "post", "projeto"])
        self.assertEqual(ev[0]["relativo"], "há 5 dias")
        self.assertEqual(ev[1]["cta"], "Ler artigo")
        self.assertEqual(ev[1]["imagem"], "img/x.webp")

    def test_projeto_sem_data_explicita_nao_gera_evento(self):
        ps = at.enriquecer_projetos([projeto("x", [])], AGORA)
        self.assertEqual(at.eventos_atividade(ps, [], 5, AGORA), [])

    def test_limite(self):
        ps = at.enriquecer_projetos([projeto("x", [post(str(i), datetime(2026, 1, i + 1)) for i in range(5)])], AGORA)
        self.assertEqual(len(at.eventos_atividade(ps, [], 3, AGORA)), 3)


class CertificadosEmMassa(unittest.TestCase):
    def certs(self):
        base = {"categoria": "online", "imagem_thumb": "t.webp", "documento": "d.pdf"}
        return at.enriquecer_certificados([
            {**base, "titulo": "A", "tema": "Python", "carga_horaria": "2h", "data": datetime(2026, 6, 3)},
            {**base, "titulo": "B", "tema": "IA", "carga_horaria": "52h", "data": datetime(2026, 6, 10), "imagem_preview": "b.webp"},
            {**base, "titulo": "C", "tema": "Python", "carga_horaria": "1h", "data": datetime(2026, 5, 20)},
            {**base, "titulo": "Sem data", "tema": "Outros"},
        ], AGORA)

    def test_ordena_por_data_e_deixa_sem_data_no_fim(self):
        self.assertEqual([c["titulo"] for c in self.certs()], ["B", "A", "C", "Sem data"])

    def test_resumo_por_tema_respeita_ordem_e_soma_horas(self):
        r = at.resumo_certificados(self.certs(), ["Python", "IA"])
        self.assertEqual((r["total"], r["horas"]), (4, 55))
        self.assertEqual([(g["nome"], g["total"], g["horas"]) for g in r["temas"]],
                         [("Python", 2, 3), ("IA", 1, 52), ("Outros", 1, 0)])

    def test_feed_agrupa_certificados_por_mes(self):
        ev = at.eventos_atividade([], self.certs(), 10, AGORA)
        self.assertEqual(len(ev), 2)  # junho (2 certs) e maio (1); "sem data" fora
        junho = ev[0]
        self.assertEqual(junho["titulo"], "2 certificações concluídas")
        self.assertEqual(junho["imagem"], "b.webp")      # maior carga horária
        self.assertEqual(junho["link"], ("certificados_lista", {}))
        self.assertEqual(ev[1]["titulo"], "C")           # mês com um só: evento do próprio certificado

    def test_certificado_sem_arquivo_nao_tem_link(self):
        c = at.enriquecer_certificados([{"titulo": "X", "categoria": "online"}], AGORA)[0]
        self.assertIsNone(c["link"])


if __name__ == "__main__":
    unittest.main()