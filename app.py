import os
from datetime import datetime
from dotenv import load_dotenv
from flask import Flask, render_template, request, url_for
from flask_compress import Compress
from data import carregar_projeto, listar_projetos
from data.perfil import sobre, jornada, habilidades, certificados, TEMAS_CERTIFICADOS
from utils.atividade import (
    enriquecer_certificados,
    enriquecer_projetos,
    eventos_atividade,
    ordenar_por_atividade,
    posts_recentes,
    resumo_certificados,
    rotulo_relativo,
    separar_certificados,
)
from utils.db import db
from utils.visualizacoes import registrar_visualizacao, obter_visualizacoes

load_dotenv()  # no-op se .env não existir; em produção o Railway injeta as env vars diretamente

# Inicializa o aplicativo Flask
app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY", "segredo-super-seguro")  # valor padrão só para dev local
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 3600
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URL", "sqlite:///dev.db")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

Compress(app)
db.init_app(app)

with app.app_context():
    db.create_all()  # idempotente: só cria tabelas ausentes (necessário para o fallback sqlite local)

DISQUS_API_KEY = os.getenv("DISQUS_API_KEY")
DISQUS_FORUM = "luiz-dererita-dev"
EMAIL_CONTATO = "luizrdererita@gmail.com"


@app.context_processor
def inject_globals():
    return {"ano_atual": datetime.now().year, "email_contato": EMAIL_CONTATO}


def _url_for_com_cache_busting(endpoint, **valores):
    """Acrescenta `?v=<mtime>` aos links de arquivos estáticos.

    SEND_FILE_MAX_AGE_DEFAULT deixa o navegador cachear CSS/JS/imagens por
    1h sem revalidar. Sem isso, todo deploy que mexe em style.css deixa
    visitantes com a versão antiga em cache enquanto o HTML (nunca
    cacheado) já usa as classes novas — o layout "quebra" em produção até
    o cache expirar. O `v` muda sempre que o arquivo muda, então o
    navegador busca a versão nova imediatamente, e arquivos que não
    mudaram continuam cacheados por 1h normalmente.
    """
    if endpoint == "static":
        nome_arquivo = valores.get("filename")
        if nome_arquivo:
            caminho = os.path.join(app.root_path, "static", nome_arquivo)
            try:
                valores["v"] = int(os.stat(caminho).st_mtime)
            except OSError:
                pass
    return url_for(endpoint, **valores)


@app.context_processor
def inject_url_for_com_cache_busting():
    return {"url_for": _url_for_com_cache_busting}


@app.template_global()
def url_item(link):
    """Resolve links `(endpoint, params)` devolvidos por utils.atividade."""
    endpoint, params = link
    return _url_for_com_cache_busting(endpoint, **params)


PROJETOS_NA_HOME = 6
POSTS_NA_HOME = 3
NOVIDADES_NA_HOME = 6


@app.route("/")
def portfolio():
    agora = datetime.now()
    projetos = ordenar_por_atividade(enriquecer_projetos(listar_projetos(), agora))
    certs = enriquecer_certificados(certificados, agora)
    cert_destaques, cert_demais = separar_certificados(certs)
    return render_template(
        "index.html",
        projetos=projetos[:PROJETOS_NA_HOME],
        total_projetos=len(projetos),
        sobre=sobre,
        jornada=jornada,
        habilidades=habilidades,
        certificados_destaque=cert_destaques,
        resumo_certs=resumo_certificados(certs, TEMAS_CERTIFICADOS),
        posts_recentes=posts_recentes(projetos, POSTS_NA_HOME),
        novidades=eventos_atividade(projetos, certs, NOVIDADES_NA_HOME, agora),
    )


@app.route("/projetos")
def projetos_lista():
    projetos = ordenar_por_atividade(enriquecer_projetos(listar_projetos()))
    categorias = sorted({p["home_card"]["categoria"] for p in projetos})
    return render_template("projetos.html", projetos=projetos, categorias=categorias)


@app.route("/certificados")
def certificados_lista():
    certs = enriquecer_certificados(certificados)
    destaques, _ = separar_certificados(certs)
    return render_template(
        "certificados.html",
        certificados_destaque=destaques,
        certificados_todos=certs,
        resumo_certs=resumo_certificados(certs, TEMAS_CERTIFICADOS),
    )


@app.route("/blogs/<projeto>", endpoint="blog_index")
def blog_index(projeto):
    dados = carregar_projeto(projeto)
    if not dados:
        return "Projeto não encontrado", 404

    pagina = int(request.args.get("pagina", 1))
    posts_por_pagina = 9
    inicio = (pagina - 1) * posts_por_pagina
    fim = inicio + posts_por_pagina
    total_paginas = (len(dados["posts"]) + posts_por_pagina - 1) // posts_por_pagina

    posts_paginados = dados["posts"][inicio:fim]
    for post in posts_paginados:
        post["visualizacoes"] = obter_visualizacoes(projeto, post["nome_arquivo"])

    return render_template(
        "blogs/index.html",
        projeto=dados["projeto"],
        ficha_tecnica=dados["ficha_tecnica"],
        home_card=dados["home_card"],
        posts=posts_paginados,
        todos_os_posts=dados["posts"],
        pagina_atual=pagina,
        total_paginas=total_paginas,
        roadmap=dados["roadmap"],
        tem_logo=dados["tem_logo"],
        tem_banner=dados["tem_banner"],
        banner_tem_titulo=dados["banner_tem_titulo"],
        repositorio=dados.get("repositorio"),
    )


@app.route("/blogs/<projeto>/postagens/<nome>", endpoint="ver_post")
def ver_post(projeto, nome):
    dados = carregar_projeto(projeto)
    if not dados:
        return "Projeto não encontrado", 404

    post = next((p for p in dados["posts"] if p["nome_arquivo"] == nome), None)
    if not post:
        return "Post não encontrado", 404

    registrar_visualizacao(projeto, nome)
    visualizacoes = obter_visualizacoes(projeto, nome)

    return render_template(
        "blogs/post.html",
        projeto=dados["projeto"],
        ficha_tecnica=dados["ficha_tecnica"],
        post=post,
        todos_os_posts=dados["posts"],
        tem_logo=dados["tem_logo"],
        tem_banner=dados["tem_banner"],
        banner_tem_titulo=dados["banner_tem_titulo"],
        visualizacoes=visualizacoes
    )


@app.route("/blogs/<projeto>/images", endpoint="galeria_imagens")
def galeria_imagens(projeto):
    dados = carregar_projeto(projeto)
    if not dados:
        return "Projeto não encontrado", 404

    imagens = dados.get("imagens", [])
    pagina = int(request.args.get("pagina", 1))
    itens_por_pagina = 10
    inicio = (pagina - 1) * itens_por_pagina
    fim = inicio + itens_por_pagina
    total_paginas = (len(imagens) + itens_por_pagina - 1) // itens_por_pagina

    return render_template(
        "blogs/images.html",
        projeto=dados["projeto"],
        ficha_tecnica=dados["ficha_tecnica"],
        imagens=imagens[inicio:fim],
        todas_imagens=imagens,
        pagina_atual=pagina,
        total_paginas=total_paginas,
        todos_os_posts=dados["posts"],
        tem_logo=dados["tem_logo"],
        tem_banner=dados["tem_banner"],
        banner_tem_titulo=dados["banner_tem_titulo"]
    )


@app.route("/blogs/<projeto>/videos", endpoint="galeria_videos")
def galeria_videos(projeto):
    dados = carregar_projeto(projeto)
    if not dados:
        return "Projeto não encontrado", 404

    videos = dados.get("videos", [])
    pagina = int(request.args.get("pagina", 1))
    itens_por_pagina = 10
    inicio = (pagina - 1) * itens_por_pagina
    fim = inicio + itens_por_pagina
    total_paginas = (len(videos) + itens_por_pagina - 1) // itens_por_pagina

    return render_template(
        "blogs/videos.html",
        projeto=dados["projeto"],
        ficha_tecnica=dados["ficha_tecnica"],
        videos=videos[inicio:fim],
        todos_videos=videos,
        pagina_atual=pagina,
        total_paginas=total_paginas,
        todos_os_posts=dados["posts"],
        tem_logo=dados["tem_logo"],
        tem_banner=dados["tem_banner"],
        banner_tem_titulo=dados["banner_tem_titulo"]
    )


@app.route("/blogs/<projeto>/downloads", endpoint="galeria_downloads")
def galeria_downloads(projeto):
    dados = carregar_projeto(projeto)
    if not dados:
        return "Projeto não encontrado", 404

    return render_template(
        "blogs/downloads.html",
        projeto=dados["projeto"],
        ficha_tecnica=dados["ficha_tecnica"],
        downloads=dados.get("downloads", []),
        todos_os_posts=dados["posts"],
        tem_logo=dados["tem_logo"],
        tem_banner=dados["tem_banner"],
        banner_tem_titulo=dados["banner_tem_titulo"]
    )


@app.template_filter('data_curta')
def data_curta(data):
    return data.strftime('%d/%m/%Y')


@app.template_filter('relativo')
def relativo(data):
    return rotulo_relativo(data)


@app.template_filter('mes_ano')
def mes_ano(data):
    meses = [
        'janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho',
        'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro'
    ]
    return f"{meses[data.month - 1]} de {data.year}"


@app.template_filter('data_extensa')
def data_extensa(data):
    meses = [
        'janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho',
        'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro'
    ]
    return f"{data.day} de {meses[data.month - 1].capitalize()} de {data.year}"


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=int(os.getenv("PORT", 5000)))
