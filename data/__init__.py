import importlib
import os
import pkgutil
import sys

_MODULOS_IGNORADOS = {"projeto_template", "perfil"}


def carregar_projeto(nome):
    """Importa dinamicamente o módulo do projeto pelo nome."""
    try:
        nome_modulo = nome.replace('-', '_')  # converte para nome de módulo válido
        modulo = importlib.import_module(f"data.{nome_modulo}")

        caminho_logo = os.path.join("static", "img", nome, "logo.png")
        caminho_banner = os.path.join("static", "img", nome, "banner.png")
        tem_logo = os.path.exists(caminho_logo)
        tem_banner = os.path.exists(caminho_banner)

        return {
            "projeto": getattr(modulo, "projeto"),
            "ficha_tecnica": getattr(modulo, "ficha_tecnica", {}),
            "posts": sorted(getattr(modulo, "posts", []), key=lambda post: post["data"], reverse=True),
            "roadmap": getattr(modulo, "roadmap", []),
            "imagens": getattr(modulo, "imagens", []),
            "videos": getattr(modulo, "videos", []),
            "downloads": getattr(modulo, "downloads", []),
            "home_card": getattr(modulo, "home_card", None),
            "tem_logo": tem_logo,
            "tem_banner": tem_banner
        }

    except ModuleNotFoundError:
        return None


def listar_projetos():
    """Descobre todos os módulos de projeto em data/ e retorna os que têm home_card,
    prontos para exibição na home. Novos projetos criados via manage.py aparecem aqui
    automaticamente, sem nenhum passo extra de registro."""
    pacote = sys.modules[__name__]
    projetos = []

    for _, nome_modulo, is_pkg in pkgutil.iter_modules(pacote.__path__):
        if is_pkg or nome_modulo in _MODULOS_IGNORADOS:
            continue

        try:
            modulo = importlib.import_module(f"data.{nome_modulo}")
            slug = getattr(modulo, "projeto", None)
            if not slug:
                continue

            dados = carregar_projeto(slug)
        except Exception as erro:
            # Um módulo de projeto com erro (ex.: em edição) não pode derrubar a home inteira.
            print(f"[data.listar_projetos] Ignorando '{nome_modulo}': {erro}")
            continue

        if dados and dados.get("home_card"):
            projetos.append(dados)

    projetos.sort(key=lambda d: (d["home_card"].get("ordem", 999), d["projeto"]))
    return projetos
