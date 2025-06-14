"""Lista de postagens do blog do Floux."""

from datetime import datetime

projeto = "tomato"

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

# Lista de metas definidas para a conclusão do projeto
roadmap = [
    {"status": "concluido", "meta": "Interface gráfica finalizada"},
    {"status": "desenvolvimento", "meta": "Integração com API da OpenAI"},
    {"status": "planejado", "meta": "Envio automático de e-mails"},
    {"alerta": "Este projeto está em fase de desenvolvimento"}
]

imagens = []

videos = []

downloads = []
