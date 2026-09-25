"""
Ferramenta de linha de comando para manutenção do portfólio.

Uso:
    python manage.py novo-projeto <slug>

Exemplo:
    python manage.py novo-projeto meu-novo-projeto

Isso cria data/<slug>.py (a partir de data/projeto_template.py) e a pasta
static/img/<slug>/. Assim que você preencher ficha_tecnica, posts e home_card,
o projeto aparece automaticamente na home e em /blogs/<slug> — não é preciso
registrar nada em app.py.
"""
import argparse
import re
import sys
from datetime import date
from pathlib import Path

RAIZ = Path(__file__).parent
TEMPLATE = RAIZ / "data" / "projeto_template.py"


def slugify_valido(slug: str) -> bool:
    return re.fullmatch(r"[a-z0-9]+(-[a-z0-9]+)*", slug) is not None


def novo_projeto(slug: str):
    if not slugify_valido(slug):
        sys.exit(f"Slug inválido: '{slug}'. Use apenas letras minúsculas, números e hífens (ex.: meu-projeto).")

    modulo_nome = slug.replace("-", "_")
    destino_py = RAIZ / "data" / f"{modulo_nome}.py"
    destino_img = RAIZ / "static" / "img" / slug

    if destino_py.exists():
        sys.exit(f"data/{modulo_nome}.py já existe. Escolha outro slug ou edite o arquivo existente.")

    conteudo = TEMPLATE.read_text(encoding="utf-8")
    titulo = slug.replace("-", " ").title()
    hoje = date.today()
    conteudo = conteudo.replace('projeto = "nome-do-projeto"', f'projeto = "{slug}"')
    conteudo = conteudo.replace('"nome": "Nome do Projeto"', f'"nome": "{titulo}"')
    # O template tem uma data placeholder inválida (datetime(0000, 0, 0)), que quebraria
    # a importação do módulo. Troca por uma data válida (hoje) para o arquivo já funcionar.
    conteudo = conteudo.replace(
        "datetime(0000, 0, 0)",
        f"datetime({hoje.year}, {hoje.month}, {hoje.day})",  # TODO (usuário): ajustar a data da postagem
    )

    conteudo += (
        "\n\n# ------------------------------------------------------------------------------\n"
        "# Cartão de exibição na Home\n"
        "# ------------------------------------------------------------------------------\n"
        "# Preencha estes campos para o projeto aparecer na seção \"Projetos\" da home.\n"
        "# categoria deve ser uma das já usadas nos filtros: jogos, web, desktop, mobile, cli\n"
        "# ------------------------------------------------------------------------------\n\n"
        "home_card = {\n"
        '    "resumo": "TODO: descrição curta (1-2 frases) para o card da home",\n'
        '    "categoria": "web",\n'
        '    "tecnologias": ["TODO"],\n'
        f'    "imagem": "img/{slug}/banner.png",\n'
        '    "ordem": 999,\n'
        "}\n"
    )
    destino_py.write_text(conteudo, encoding="utf-8")

    destino_img.mkdir(parents=True, exist_ok=True)
    (destino_img / ".gitkeep").touch()

    print(f"Criado data/{modulo_nome}.py")
    print(f"Criado static/img/{slug}/ (adicione banner.png e, se quiser, logo.png aqui)")
    print("Próximos passos:")
    print(f"  1. Preencha ficha_tecnica, posts, roadmap e home_card em data/{modulo_nome}.py")
    print(f"  2. Coloque banner.png (e logo.png opcional) em static/img/{slug}/")
    print(f"  3. Rode a app localmente e confira / e /blogs/{slug}")


def main():
    parser = argparse.ArgumentParser(description="Ferramentas de manutenção do portfólio.")
    subparsers = parser.add_subparsers(dest="comando", required=True)

    parser_novo = subparsers.add_parser("novo-projeto", help="Cria um novo módulo de projeto a partir do template.")
    parser_novo.add_argument("slug", help="Slug kebab-case do projeto, ex.: meu-novo-projeto")

    args = parser.parse_args()

    if args.comando == "novo-projeto":
        novo_projeto(args.slug)


if __name__ == "__main__":
    main()
