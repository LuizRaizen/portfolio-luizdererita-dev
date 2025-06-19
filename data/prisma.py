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

projeto = "prisma" # Exemplo: "meu-projeto-avancado"

# ------------------------------------------------------------------------------
# Ficha Técnica
# ------------------------------------------------------------------------------
# Informações exibidas na seção "Ficha Técnica" da página principal do projeto.
# Os campos podem ser deixados em branco ("") caso não se apliquem.
# ------------------------------------------------------------------------------

ficha_tecnica = {
    "nome": "Prisma",
    "linguagem": "Python",
    "framework": "Tkinter",
    "paradigma": "Programação Orientada a Objetos (OOP)",
    "arquitetura": "",
    "tipo_projeto": "Um visualizador de Códigos RGB para cores.",
    "interface": "Canvas e widgets de cor nativos do Tkinter",
    "funcionalidades": ["Obtenção de códigos RGB"],
    "bibliotecas": [],
    "banco_de_dados": "SQlite",
    "api_externa": "",
    "plataforma": "Desktop (Windows / Linux)",
    "resolucao": "",
    "status": "Em estágio inicial / conceito"
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
        "titulo": "A Origem do Prisma",
        "data": datetime(2025, 6, 12),
        "autor": "Luiz R. Dererita",
        "nome_arquivo": "post1",
        "conteudo": """
        <p>
          O Prisma surgiu numa época em que eu estava me aprofundando nos estudos sobre interfaces gráficas com Python. Naquele período, eu trabalhava em uma ótica — a mesma citada no projeto do E-commerce da Óticas Picerni — onde, além do atendimento, também era responsável por criar toda a parte visual da loja: posts para redes sociais, panfletos, identidade visual, entre outros materiais gráficos.
        </p>
        <p>
          Como designer autodidata, lidar com cores fazia parte do meu dia a dia. Eu precisava constantemente escolher, combinar e replicar cores em diferentes formatos, especialmente em RGB e hexadecimal. E foi aí que nasceu o estalo: "e se eu criasse um programa que me ajudasse a extrair e trabalhar com essas cores de forma prática?".
        </p>

        <h2 class="section-title mt-4">Explorando o Tkinter</h2>
        <p>
          Estudando Tkinter, descobri widgets interessantes que permitiam manipulação de cores e desenhos com o <code>Canvas</code>. Criei, então, um pequeno app que batizei de <strong>Prisma</strong>. A ideia era simples: permitir que o usuário escolhesse uma cor e tivesse acesso ao seu código RGB.
        </p>
        <p>
          No entanto, logo percebi que só o RGB não era suficiente para o que eu precisava. Na prática, a maioria das ferramentas de design trabalha com código hexadecimal. Infelizmente, naquela fase, eu ainda não tinha domínio suficiente sobre conversão entre esses formatos, e isso acabou limitando a utilidade prática do app.
        </p>

        <h2 class="section-title mt-4">Um projeto com potencial</h2>
        <p>
          O Prisma nunca chegou a ser usado no meu dia a dia profissional, mas ele representa uma etapa importante da minha evolução com Python e interfaces gráficas. Ele me fez entender a importância de pensar no uso real de uma aplicação — e como a escolha de ferramentas certas pode transformar um projeto simples em algo poderoso.
        </p>
        <p>
          Até hoje, tenho vontade de revisitar esse projeto. Talvez criar uma versão web, moderna, com acesso via navegador. Mesmo existindo diversas ferramentas online que fazem isso, eu acredito que construir a minha própria versão seria um ótimo desafio e uma excelente forma de consolidar conhecimentos adquiridos.
        </p>

        <h2 class="section-title mt-4">Reflexão</h2>
        <p>
          O Prisma é mais do que um app incompleto — é um marco da minha trajetória como desenvolvedor e designer. É um lembrete de onde comecei e o quanto evoluí desde então. Guardá-lo e, quem sabe, aprimorá-lo futuramente é uma forma de honrar esse caminho de descobertas que o Python me proporcionou.
        </p>

        <p class="meta-info">Postado em <strong>9 de Junho de 2025</strong> por <strong>Luiz R. Dererita</strong></p>
          
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
    {"alerta": "Este projeto está em fase de desenvolvimento"},

    # METAS
    {"status": "concluido", "meta": "Criação do protótipo inicial com Tkinter"},
    {"status": "concluido", "meta": "Implementação básica da seleção de cores com exibição do código RGB"},
    {"status": "desenvolvimento", "meta": "Conversão automática de RGB para hexadecimal"},
    {"status": "desenvolvimento", "meta": "Exibição em tempo real da cor selecionada e seu código em múltiplos formatos"},
    {"status": "planejado", "meta": "Paleta de cores personalizada com sistema de favoritos"},
    {"status": "planejado", "meta": "Exportação de paletas como imagem ou arquivo JSON"},
    {"status": "planejado", "meta": "Migração para uma versão web responsiva com Flask ou Django"},
    {"status": "planejado", "meta": "Compatibilidade com bibliotecas de design (Material, Tailwind, etc.)"},
    {"status": "planejado", "meta": "Dark Mode e temas customizáveis para a interface"},
]

# ------------------------------------------------------------------------------
# Galeria de imagens
# ------------------------------------------------------------------------------
# Cada imagem deve conter:
# - src: caminho relativo à pasta static/
# - descricao: legenda exibida ao lado da imagem
# ------------------------------------------------------------------------------

imagens = [
    {"src": "img/prisma/prisma.png", "descricao": "Tela do Prisma"}
]

# ------------------------------------------------------------------------------
# Vídeos do projeto
# ------------------------------------------------------------------------------
# Cada vídeo deve conter:
# - src: caminho relativo à pasta static/
# - descricao: legenda opcional
# ------------------------------------------------------------------------------

videos = []

# ------------------------------------------------------------------------------
# Arquivos disponíveis para download
# ------------------------------------------------------------------------------
# Cada item deve conter:
# - nome: nome do arquivo
# - descricao: descrição exibida ao lado do botão
# - arquivo: caminho relativo à pasta static/
# ------------------------------------------------------------------------------

downloads = []
