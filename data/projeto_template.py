"""
Módulo de configuração do projeto para exibição dinâmica no portfólio/blog.

Este módulo define as informações estruturadas sobre um projeto específico,
incluindo dados técnicos, posts, roadmap, imagens, vídeos e arquivos para download.
Ele será importado dinamicamente pelo sistema Flask do site.

Exemplo de uso:
    from data import nome_do_projeto
    dados = carregar_projeto(nome_do_projeto)
"""

from datetime import datetime

# ------------------------------------------------------------------------------
# Nome do projeto (deve corresponder ao nome da pasta e à URL)
# ------------------------------------------------------------------------------

projeto = "nome-do-projeto" # Exemplo: "meu-projeto-avancado"

# ------------------------------------------------------------------------------
# Ficha Técnica
# ------------------------------------------------------------------------------
# Informações exibidas na seção "Ficha Técnica" da página principal do projeto.
# Os campos podem ser deixados em branco ("") caso não se apliquem.
# ------------------------------------------------------------------------------

ficha_tecnica = {
    "nome": "Nome do Projeto",
    "linguagem": "Linguagem(s) utilizadas no projeto",
    "framework": "Framework utilizado no projeto",
    "paradigma": "Paradigma de desenvolvimento",
    "arquitetura": "Arquitetura utilizada no projeto",
    "tipo_projeto": "Descrição do projeto",
    "interface": "Tipo de interface do projeto",
    "funcionalidades": [
        "Funcionalidade 1",
        "Funcionalidade 2",
    ],
    "bibliotecas": [
        "biblioteca_1",
        "biblioteca_2",
    ],
    "banco_de_dados": "Banco de dados utilizado no projeto",
    "api_externa": [
        "API_1",
        "API_2",
    ],
    "plataforma": "Plataforma onde roda o projeto",
    "resolucao": "000x000",
    "status": "Status do projeto"
}

# ------------------------------------------------------------------------------
# Postagens do blog
# ------------------------------------------------------------------------------
# Cada postagem deve conter:
# - titulo (str)
# - data (datetime)
# - autor (str)
# - nome_arquivo (str) - usado na URL para exibição individual
# - conteudo (str) - HTML com parágrafos, títulos, etc.
# - imagem (opcional) - caminho relativo à pasta static/
# ------------------------------------------------------------------------------

posts = [
    {
        "titulo": "Título da Postagem",
        "data": datetime(0000, 0, 0),
        "autor": "Autor",
        "nome_arquivo": "post1",
        "conteudo": """
          <p>Conteúdo da postagem</p>
        """,
    },
]

# ------------------------------------------------------------------------------
# Roadmap do projeto
# ------------------------------------------------------------------------------
# A primeira entrada pode ser um alerta opcional (com chave "alerta").
# As metas devem conter:
# - status: "concluido", "desenvolvimento" ou "planejado"
# - meta: descrição da tarefa/meta
# ------------------------------------------------------------------------------

roadmap = [
    # ALERTA OPCIONAL
    {"alerta": "Mensagem de alerta"},

    # METAS
    {"status": "planejado", "meta": "Descrição da meta"},
]

# ------------------------------------------------------------------------------
# Galeria de imagens
# ------------------------------------------------------------------------------
# Cada imagem deve conter:
# - src: caminho relativo à pasta static/
# - descricao: legenda exibida ao lado da imagem
# ------------------------------------------------------------------------------

imagens = [
    {"src": "img/pasta-do-projeto/imagem", "descricao": "Descrição do imagem"},
]

# ------------------------------------------------------------------------------
# Vídeos do projeto
# ------------------------------------------------------------------------------
# Cada vídeo deve conter:
# - src: caminho relativo à pasta static/
# - descricao: legenda opcional
# ------------------------------------------------------------------------------

videos = [
    {
        "youtube_id": "ID do vídeo no Youtube",
        "descricao": "Descrição do vídeo"
    }
]

# ------------------------------------------------------------------------------
# Arquivos disponíveis para download
# ------------------------------------------------------------------------------
# Cada item deve conter:
# - nome: nome do arquivo
# - descricao: descrição exibida ao lado do botão
# - arquivo: caminho relativo à pasta static/
# ------------------------------------------------------------------------------

downloads = [
    {
        "nome": "nome-do-arquivo",
        "descricao": "Descrição do Download",
        "arquivo": "downloads/caminho-para-o-arquivo"
    }
]
