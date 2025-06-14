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

projeto = "dieroll"  # Exemplo: "meu-projeto-avancado"

# ------------------------------------------------------------------------------
# Ficha Técnica
# ------------------------------------------------------------------------------
# Informações exibidas na seção "Ficha Técnica" da página principal do projeto.
# Os campos podem ser deixados em branco ("") caso não se apliquem.
# ------------------------------------------------------------------------------

ficha_tecnica = {
    "nome": "Dieroll",
    "linguagem": "Python",
    "framework": "",
    "paradigma": "Programação Estruturada e Orientada a Objetos",
    "arquitetura": "Projeto simples com separação entre lógica e interface",
    "tipo_projeto": "Simulação visual de lançamento de dados de azar/RPG",
    "interface": "Gráfica, com botão interativo para realizar a rolagem",
    "funcionalidades": ["Obtém valores aleatórios para simular um dado"],
    "bibliotecas": ["pygame", "random"],
    "banco_de_dados": "",
    "api_externa": "",
    "plataforma": "Desktop (Windows / Linux)",
    "resolucao": "",
    "status": "Finalizado"
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
        "titulo": "Explorando os Módulos do Python",
        "data": datetime(2025, 6, 12),
        "autor": "Luiz R. Dererita",
        "nome_arquivo": "post1",
        "conteudo": """
        <p>
          O <strong>Dieroll</strong> foi um dos primeiros projetos que desenvolvi quando comecei a explorar a biblioteca <strong>Pygame</strong>. A ideia surgiu de algo simples: eu queria criar um programa que simulasse o lançamento de um dado, como aqueles usados em jogos de tabuleiro ou RPG. Já conhecia o módulo <code>random</code> do Python, e já havia criado um módulo de linha de comando que simulava rolagens, mas sentia falta de algo visual.
        </p>

        <h2 class="section-title mt-4">Primeira Experiência Visual com Pygame</h2>
        <p>
          Como ainda estava aprendendo Pygame, achei que seria uma ótima oportunidade para aplicar os conceitos em algo prático. O funcionamento é bem direto: o usuário clica no botão "Rolar", e a face do dado na tela se atualiza com uma nova imagem, representando o número sorteado aleatoriamente entre 1 e 6.
        </p>
        <p>
          Trabalhar com imagens, eventos de mouse, renderização de tela e controle de loop de jogo foi essencial para entender a dinâmica do Pygame e me sentir mais confortável desenvolvendo interfaces simples com feedback visual.
        </p>

        <h2 class="section-title mt-4">Aprendizados Técnicos</h2>
        <ul>
          <li>Uso do <strong>módulo random</strong> para gerar números aleatórios simulando a rolagem do dado.</li>
          <li>Manipulação de <strong>eventos de clique</strong> com Pygame para interatividade.</li>
          <li>Exibição e <strong>atualização de imagens</strong> na tela com base no resultado da rolagem.</li>
          <li>Estrutura de <strong>loop principal</strong> do programa com controle de tempo e renderização.</li>
        </ul>

        <h2 class="section-title mt-4">Motivações</h2>
        <p>
          Eu sempre gostei da estética dos jogos de RPG, e como iniciante em desenvolvimento de jogos, fazer algo que reproduzisse uma ação típica desses jogos (rolar um dado) foi uma forma divertida e acessível de entrar no universo do desenvolvimento de jogos simples com Python. Mesmo sendo um projeto pequeno, ele tem muito valor pessoal para mim.
        </p>

        <h2 class="section-title mt-4">Reflexão Final</h2>
        <p>
          <strong>Dieroll</strong> foi um projeto essencial na minha curva de aprendizado. Ele me ensinou como criar aplicações interativas, lidar com eventos e estruturar projetos pequenos, mas completos. Além disso, me proporcionou aquela sensação gratificante de ver algo ganhando vida visualmente na tela — uma sensação que me motivou a continuar criando. Mesmo sendo um projeto simples, ele cumpre o que se propõe com elegância e é um marco importante na minha trajetória.
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
    {"alerta": ""},

    # METAS
    {"status": "concluido", "meta": "Criação do módulo base com random para simular a rolagem"},
    {"status": "concluido", "meta": "Implementação do esqueleto do programa com Pygame"},
    {"status": "concluido", "meta": "dição de imagens para as faces do dado"},
    {"status": "concluido", "meta": 'Criação do botão "Rolar" com detecção de clique'},
    {"status": "concluido", "meta": "Renderização da imagem do dado com base no número sorteado"},
    {"status": "concluido", "meta": "Testes de funcionamento e ajustes visuais"},
    {"status": "desenvolvimento", "meta": "Gerar executável e disponibilizar para Download"},
]

# ------------------------------------------------------------------------------
# Galeria de imagens
# ------------------------------------------------------------------------------
# Cada imagem deve conter:
# - src: caminho relativo à pasta static/
# - descricao: legenda exibida ao lado da imagem
# ------------------------------------------------------------------------------

imagens = [
    {"src": "img/dieroll/print.png", "descricao": "Tela do Dieroll"}
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
