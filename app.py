import os
from flask import Flask, render_template, request
from flask_compress import Compress
from data import carregar_projeto
from utils.db import db
from utils.visualizacoes import registrar_visualizacao, obter_visualizacoes

# Inicializa o aplicativo Flask
app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY", "segredo-super-seguro")
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 3600
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv(
    "DATABASE_URL",
    'postgresql://postgres:obNQSieLVHcKtokSiOejJTNaQyExEsaS@yamabiko.proxy.rlwy.net:51189/railway'
)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

Compress(app)
db.init_app(app)

DISQUS_API_KEY = os.getenv("DISQUS_API_KEY")
DISQUS_FORUM = "luiz-dererita-dev"


@app.route("/")
def portfolio():
    return render_template("index.html")


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
        posts=posts_paginados,
        todos_os_posts=dados["posts"],
        pagina_atual=pagina,
        total_paginas=total_paginas,
        roadmap=dados["roadmap"],
        tem_logo=dados["tem_logo"]
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
        tem_logo=dados["tem_logo"]
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
        tem_logo=dados["tem_logo"]
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
        tem_logo=dados["tem_logo"]
    )


@app.template_filter('data_curta')
def data_curta(data):
    return data.strftime('%d/%m/%Y')


@app.template_filter('data_extensa')
def data_extensa(data):
    meses = [
        'janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho',
        'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro'
    ]
    return f"{data.day} de {meses[data.month - 1].capitalize()} de {data.year}"


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=int(os.getenv("PORT", 5000)))
