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

projeto = "tomato" # Exemplo: "meu-projeto-avancado"

# ------------------------------------------------------------------------------
# Ficha Técnica
# ------------------------------------------------------------------------------
# Informações exibidas na seção "Ficha Técnica" da página principal do projeto.
# Os campos podem ser deixados em branco ("") caso não se apliquem.
# ------------------------------------------------------------------------------

ficha_tecnica = {
    "nome": "Tomato",
    "linguagem": "Python",
    "framework": "",
    "paradigma": "Programação Orientada a Objetos (OOP)",
    "arquitetura": "",
    "tipo_projeto": "Uma ferramenta para personalizar códigos ANSI",
    "interface": "",
    "funcionalidades": ["Altera caracteres ANSI através do Terminal/CMD"],
    "bibliotecas": ["colorama"],
    "banco_de_dados": "",
    "api_externa": "",
    "plataforma": "Desktop (Windows / Linux)",
    "resolucao": "",
    "status": "Em análise para possíveis melhorias"
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
        "titulo": "Origem do Tomato",
        "data": datetime(2025, 6, 12),
        "autor": "Luiz R. Dererita",
        "nome_arquivo": "post1",
        "conteudo": """
          Quando comecei a programar o que viria a se tornar o <strong>Tomato</strong>, ele nem sequer tinha nome. Era apenas um apanhado de funções que alteravam minimamente a aparência dos caracteres no terminal. Na época, eu usava um All-in-One da Positivo — um computador simples, mas que me acompanhou por quase cinco anos. Meu pai havia comprado para mim, por volta de 2017.
        </p>
        <p>
          Estava dando meus primeiros passos com Python, e o interesse por programação surgiu de uma curiosidade antiga: desenvolver jogos. Eu frequentava fóruns sobre MUGEN, RPG Maker e Game Maker. Quem conhece essas engines sabe que muitas delas se apoiam em eventos gráficos e arrastar-e-soltar. Justamente por isso, eu fugia da palavra "programação". Achava complicado demais. Sempre procurava formas de criar jogos sem precisar escrever código.
        </p>
        <p>
          O problema é que essas engines têm limitações — especialmente para quem não sabe programar. O RPG Maker, por exemplo, usa Ruby por trás das cortinas, e eu era preguiçoso demais para tentar entendê-lo. Game Maker usava uma linguagem própria, o GML. Já o MUGEN exigia edição de arquivos específicos, mesmo sem ser programação propriamente dita.
        </p>
        <p>
          Nesse cenário de experimentações, surgiu meu primeiro contato com código real — e com Python. Não lembro o momento exato, mas foi movido por uma frustração: a sensação de estar limitado pelas ferramentas que eu conhecia. Eu queria mais controle. Queria personalização. E foi assim que nascia, ainda de forma rudimentar, a ideia do Tomato.
        </p>

        <h2 class="section-title mt-4">Desenvolvimento Inicial</h2>
        <p>
          O caminho até a primeira versão do Tomato não foi fácil. Eu não conhecia boas práticas, e o código era bem bagunçado (risos). Assisti muitas aulas no YouTube, li PDFs obscuros da internet e fui aprendendo na marra. O nome “Tomato” surgiu do nada. Por algum motivo, associei a ideia de um tomate a um módulo de personalização ANSI — vai entender!
        </p>
        <p>
          A ideia principal era criar um módulo que me ajudasse a estilizar saídas de texto no terminal de forma automatizada. Eu já tinha usado bastante o módulo <code>colorama</code>, e isso me inspirou. A diferença é que o Tomato seria modular, reutilizável, e com algumas funções prontas para facilitar a vida de quem, como eu, queria dar um toque visual ao CLI.
        </p>

        <h2 class="section-title mt-4">Por que Ele Está no Portfólio</h2>
        <p>
          Mesmo simples, o Tomato representa o início da minha trajetória real na programação. É o segundo projeto que subi no GitHub — e o primeiro que considero "completo". Na época, eu não fazia ideia de como publicar pacotes Python, e não entendia bem como usar ambientes virtuais. Por isso, toda vez que queria usar o Tomato, eu copiava sua pasta para dentro dos projetos.
        </p>
        <p>
          Hoje, olhando para ele, vejo um marco. Um ponto de partida. Talvez um dia eu volte ao código e o refatore com tudo que aprendi. Quem sabe eu não adicione temas, suporte a tabelas ou até faça uma publicação oficial no PyPI. Mas, por ora, ele segue aqui, como memória viva de onde tudo começou.
        </p>

        <p class="meta-info">Postado em <strong>5 de Junho de 2025</strong> por <strong>Luiz R. Dererita</strong></p>
        
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
    {"status": "concluido", "meta": "Criação do módulo principal com comandos básicos de formatação ANSI"},
    {"status": "concluido", "meta": "Implementação dos primeiros estilos (negrito, itálico, sublinhado, tachado)"},
    {"status": "concluido", "meta": "Leitura e uso de arquivo `config.json` para ajustes dinâmicos"},
    {"status": "concluido", "meta": "Criação do sistema de diretórios e arquitetura para plugins"},
    {"status": "concluido", "meta": "Documentação interna e docstrings para todos os móduloss"},
    {"status": "desenvolvimento", "meta": "Implementação de testes automatizados para os estilos e plugins"},
    {"status": "planejado", "meta": 'Criação de novos plugins com estilos personalizados (ex: "futurista", "vintage")'},
    {"status": "planejado", "meta": "Implementação de modo interativo para seleção de estilo ao vivo"},
    {"status": "planejado", "meta": "Modo compatível com exportação de texto para arquivos `.md` e `.txt`"},
    {"status": "planejado", "meta": "Criação de versão desktop com interface gráfica simples"},
    {"status": "planejado", "meta": "Modo compatível com exportação de texto para arquivos `.md` e `.txt`"},
    {"status": "planejado", "meta": "Distribuição via PyPI com `pip install tomato-cli`"},
]

# ------------------------------------------------------------------------------
# Galeria de imagens
# ------------------------------------------------------------------------------
# Cada imagem deve conter:
# - src: caminho relativo à pasta static/
# - descricao: legenda exibida ao lado da imagem
# ------------------------------------------------------------------------------

imagens = []

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
