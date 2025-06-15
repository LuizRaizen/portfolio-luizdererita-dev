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

projeto = "invaders-from-mars"  # Exemplo: "meu-projeto-avancado"

# ------------------------------------------------------------------------------
# Ficha Técnica
# ------------------------------------------------------------------------------
# Informações exibidas na seção "Ficha Técnica" da página principal do projeto.
# Os campos podem ser deixados em branco ("") caso não se apliquem.
# ------------------------------------------------------------------------------

ficha_tecnica = {
    "nome": "Invaders From Mars",
    "linguagem": "Python",
    "framework": "Flask",
    "paradigma": "Programação Orientada a Objetos",
    "arquitetura": "MVC (Model-View-Controller)",
    "tipo_projeto": "Aplicação Web",
    "interface": "Interface Web Responsiva com Bootstrap",
    "funcionalidades": [
        "Autenticação de usuários",
        "Sistema de posts e comentários",
        "Painel administrativo"
    ],
    "bibliotecas": ["Flask", "Jinja2", "SQLAlchemy"],
    "banco_de_dados": "SQLite",
    "api_externa": "OpenAI API",
    "plataforma": "Desktop e Mobile via Navegador",
    "resolucao": "Responsivo",
    "status": "Concluído"
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
        "titulo": "Como Tudo Começou",
        "data": datetime(2025, 6, 8),
        "autor": "Luiz R. Dererita",
        "nome_arquivo": "post1",
        "conteudo": """
            <p>Meu interesse por programação veio através do meu fascínio pelo desenvolvimento de jogos. Desde adolescente, sempre fui movido pela curiosidade — mas também sofri com falta de foco e dificuldade em concluir o que começava. Isso me levou a diversos momentos de frustração e autossabotagem, questionando minha capacidade e inteligência. Por muito tempo, achei que eu não era bom em nada. Mas dentro de mim havia sempre essa vontade insistente de criar, de aprender, de construir algo meu.</p>
            <p>Ganhei meu primeiro computador por volta dos 14 anos. Era um desktop com monitor de tubo, e com ele mergulhei no universo dos jogos. No início, me contentava com games em Flash, de sites como ClickJogos, até descobrir os emuladores — e isso mudou tudo. A possibilidade de jogar clássicos do SNES, GBA e Mega Drive me encantou. Meus favoritos? RPGs asiáticos como Final Fantasy, Terranigma, Fire Emblem... e claro, os jogos de luta como Street Fighter, KoF e Fatal Fury.</p>
            <p>Com o tempo, o encantamento deu lugar à inquietação: “Como esses jogos são feitos?” Essa pergunta me perseguiu por anos. Eu experimentava engines como RPG Maker e Game Maker, mas sempre esbarrava nas limitações. Foi nesse contexto que conheci o Python.</p>
            <p><strong>Invaders From Mars</strong> é um jogo de ação 2D no estilo arcade, onde o jogador controla uma nave espacial em meio a uma invasão alienígena vinda do planeta Marte. Com jogabilidade frenética e progressiva, o jogo resgata a nostalgia dos clássicos de fliperama, adicionando elementos modernos como efeitos visuais, power-ups e padrões de inimigos inteligentes. Criado com Python e Pygame, o projeto é uma homenagem às raízes da ficção científica e representa um marco pessoal na minha trajetória como desenvolvedor de jogos.</p>

            <h3 class="section-title mt-4">A Inspiração</h3>
            <p>Na época, eu estava sem computador e sem internet. Mesmo assim, não quis parar de estudar. Usava o celular para ler PDFs, e foi assim que encontrei o livro <em>Curso Intensivo de Python</em>, do Eric Matthes. A leitura foi desafiadora, mas mudou minha vida. O último projeto do livro propunha desenvolver um jogo de nave, inspirado no clássico <strong>Alien Invaders</strong>, do Atari. Parecia simples à primeira vista, mas para mim era um desafio enorme.</p>
            <p>Não consegui concluir da primeira vez. Nem da segunda. Nem da terceira. Toda vez que eu tentava, queria melhorar o projeto, adicionar ideias minhas: um novo efeito visual, um comportamento inédito para os inimigos, uma arma especial... e acabava travando. Me perdia no código, não entendia mais nada, e abandonava. Mas uma coisa nunca mudei: a promessa de que um dia eu finalizaria esse jogo.</p>

            <h3 class="section-title mt-4">A Redescoberta</h3>
            <p>Depois de alguns anos estudando programação com mais maturidade, voltei ao projeto. Em vez de usar o código do livro, resolvi recomeçar do zero. E logo percebi: o projeto original era bom como exercício de lógica, mas não era ideal para um jogo de verdade. Eu precisava aplicar arquitetura adequada, dividir responsabilidades, usar padrões de projeto como o <strong>State Pattern</strong> e o <strong>Modelo MVC</strong>. Com essa base mais sólida, o desenvolvimento finalmente deslanchou.</p>
            <p>Mesmo com ferramentas simples como o <code>pygame</code>, decidi fazer o melhor que eu podia com o que tinha. A cada pequeno avanço, sentia que aquele não era mais só um projeto de livro. Era <em>meu jogo</em>.</p>
            <p>O mercado de jogos evoluiu consideravelmente ao longo dos anos. Quando iniciei o desenvolvimento de <strong>Invaders From Mars</strong>, eu já tinha plena consciência de que o <code>pygame</code> não era a ferramenta mais adequada para a criação de um jogo com padrão profissional. Ainda assim, decidi seguir com o projeto justamente por permitir que eu criasse os gráficos e as estruturas do jogo a partir do zero — algo que muitas vezes passa despercebido por desenvolvedores que utilizam engines mais robustas e focadas apenas no aspecto prático do desenvolvimento. Acredito que essa escolha foi essencial para o meu amadurecimento como desenvolvedor, além de ter contribuído de forma significativa para o aprimoramento da minha lógica de programação.</p>

            <p>O jogo também conta com <strong>transições visuais</strong>, <strong>efeitos sonoros personalizados</strong> e uma HUD minimalista com contador de vidas, tempo e pontuação.</p>

            <h3 class="section-title mt-4">Design e Arte</h3>
            <p>Apesar das limitações técnicas, me preocupei bastante com a apresentação visual. Utilizei imagens raster com efeitos em camadas para o fundo, simulando profundidade estelar. Os inimigos possuem efeitos de entrada com fade-in e expansão de escala, criando a sensação de teletransporte. Os power-ups contam com sprites animadas e efeitos de brilho. E a nave principal tem múltiplos estágios visuais de transformação ao adquirir upgrades, com cores, sombras e traços diferentes.</p>
            <p>A arte do jogo foi feita toda com ferramentas gratuitas, e o design busca remeter à ficção científica retrô — inspirando-se em obras como <em>Space Invaders</em>, <em>R-Type</em>, <em>Galaga</em> e até alguns elementos estéticos de <em>Metroid</em>.</p>

            <h3 class="section-title mt-4">Jogabilidade</h3>
            <p><strong>Invaders From Mars</strong> é um jogo de nave 2D com rolagem vertical, onde o jogador assume o controle de um piloto solitário enfrentando uma invasão alienígena vinda de Marte. O gameplay é inspirado nos clássicos de fliperama, mas com mecânicas modernas como:</p>
            <ul>
                <li>Power-ups temporários (escudo, velocidade, tiro duplo);</li>
                <li>Sistema de pontuação e combo;</li>
                <li>Ondas de inimigos com comportamento progressivo e teleporte dimensional;</li>
                <li>Chefes com padrão de ataque único e efeitos especiais ao entrar em cena.</li>
            </ul>

            <h3 class="section-title mt-4">Reflexão Final</h3>
            <p>Desenvolver <strong>Invaders From Mars</strong> me ensinou mais do que qualquer curso. Aprendi sobre organização, persistência, humildade e sobretudo, sobre mim mesmo. O jogo é simples. Mas ele representa o reencontro com a minha confiança. Hoje, sei que sou capaz de concluir projetos. E mais do que isso: capaz de criar algo com identidade.</p>

            <p class="meta-info">Postado em <strong>7 de Junho de 2025</strong> por <strong>Luiz R. Dererita</strong></p>

        """,
    },
    {
        "titulo": "Design de Inimigos e Bosses",
        "data": datetime(2025, 6, 10),
        "autor": "Luiz R. Dererita",
        "nome_arquivo": "post2",
        "conteudo": """
            <p>Um dos aspectos mais divertidos — e desafiadores — de desenvolver <strong>Invaders From Mars</strong> foi criar os inimigos. Desde o início, eu não queria que fossem apenas obstáculos aleatórios na tela. Queria que cada um tivesse <em>personalidade</em>, <em>movimentos distintos</em>, e representassem algum tipo de ameaça reconhecível — como se tivessem uma história por trás, mesmo que o jogador nunca a conheça.</p>

            <p>Minhas inspirações vieram de todo lado. Os clássicos como <strong>Galaga</strong> e <strong>R-Type</strong> me influenciaram diretamente na forma como os inimigos se organizam e se movem em padrões. Já os bosses, esses vieram da minha fascinação por vilões que causam impacto visual e mecânico — penso em jogos como <em>Metal Slug</em>, <em>Undertale</em> e até alguns chefes do <strong>Final Fantasy</strong>.</p>

            <h3 class="section-title mt-4">Construindo Ameaças</h3>
            <p>Para os inimigos comuns, criei três categorias principais: os <strong>escoteiros</strong>, os <strong>bombardeiros</strong> e os <strong>imprevisíveis</strong>. Os escoteiros são rápidos e tentam enganar o jogador com pequenas curvas; os bombardeiros descem lentamente, mas disparam projéteis em linha reta; já os imprevisíveis... bem, o nome já diz tudo. Eles aparecem e desaparecem com um efeito de teleporte, deixando um rastro visual que confunde quem joga.</p>

            <p>Mas o verdadeiro desafio foram os <strong>Bosses</strong>. Eu queria que cada chefe tivesse uma identidade clara. O primeiro boss, por exemplo, é inspirado em um polvo alienígena gigante — seus tentáculos se movem em diferentes direções enquanto ele solta disparos em espiral. Visualmente, usei uma estética que remete aos velhos filmes de ficção científica dos anos 50, com formas exageradas e olhos brilhantes.</p>

            <h3 class="section-title mt-4">Animações e Efeitos</h3>
            <p>Todo inimigo novo que aparece em tela conta com uma animação de <strong>entrada dimensional</strong>. Eles não surgem “do nada”. Há um pequeno <code>fade-in</code> com crescimento de escala, seguido por uma explosão de luz branca — como se estivessem atravessando uma fenda no espaço-tempo. Isso não é só um enfeite: serve para avisar o jogador que algo importante está chegando.</p>

            <p>Para os bosses, a entrada é ainda mais dramática: a tela escurece, o fundo para, e a nave do jogador é empurrada levemente para baixo. O som muda. E só então, o chefe surge com seu efeito visual. Eu me inspirei muito na ideia de que o jogo deve “avisar” que algo maior está para acontecer. É quase como se o jogo dissesse: <em>Prepare-se.</em></p>

            <h3 class="section-title mt-4">Comportamentos e Inteligência</h3>
            <p>Não queria inimigos com comportamento completamente aleatório, mas também não queria que fossem 100% previsíveis. Alguns bosses aprendem com os movimentos do jogador — se você ficar muito tempo em uma lateral, ele começa a mirar mais para esse lado. Outros lançam projéteis que seguem o jogador com leve atraso, obrigando você a estar sempre em movimento.</p>

            <p>Esse tipo de sistema me obrigou a estudar lógica condicional, timers e sistemas de prioridade. E foi aí que percebi: mesmo um jogo simples pode ser extremamente complexo por trás das câmeras.</p>

            <h3 class="section-title mt-4">Reflexão Final</h3>
            <p>O design dos inimigos e bosses não é só sobre visual e dificuldade. É sobre contar uma história silenciosa. É sobre deixar o jogador curioso sobre quem é aquele inimigo, de onde veio, e por que está ali. E mesmo que essas perguntas nunca sejam respondidas dentro do jogo, a sensação de que existe algo maior por trás do caos torna tudo mais envolvente.</p>

            <p>Criei cada um com carinho — e confesso, me divirto mais enfrentando os bosses do meu próprio jogo do que jogando muitos títulos por aí. Porque sei exatamente o que cada detalhe representa. E isso, pra mim, é uma das maiores satisfações de desenvolver jogos.</p>

            <p class="meta-info">Postado em <strong>11 de Junho de 2025</strong> por <strong>Luiz R. Dererita</strong></p>

        """
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
    {"alerta": "Este projeto está em fase de desenvolvimento."},

    # METAS
    {"status": "concluido", "meta": "Criação da nave do jogador e movimentação básica"},
    {"status": "concluido", "meta": "Sistema de tiros e colisão com inimigos"},
    {"status": "concluido", "meta": "Criação e movimentação dos alienígenas",},
    {"status": "concluido", "meta": "HUD com score, vidas e tempo de jogo"},
    {"status": "concluido", "meta": "Efeitos visuais e sonoros (explosões, música de fundo)"},
    {"status": "concluido", "meta": "Sistema de fases com aumento gradual de dificuldade"},
    {"status": "desenvolvimento", "meta": "Implementação de power-ups e upgrades da nave"},
    {"status": "desenvolvimento", "meta": "Tela de início, pause e game over"},
]

# ------------------------------------------------------------------------------
# Galeria de imagens
# ------------------------------------------------------------------------------
# Cada imagem deve conter:
# - src: caminho relativo à pasta static/
# - descricao: legenda exibida ao lado da imagem
# ------------------------------------------------------------------------------

imagens = [
    {"src": "img/invaders-from-mars/menu_principal.png", "descricao": "Menu Principal do jogo"},
    {"src": "img/invaders-from-mars/gameplay.png", "descricao": "Jogando Invaders From Mars"},
]

# ------------------------------------------------------------------------------
# Vídeos do projeto
# ------------------------------------------------------------------------------
# Cada vídeo deve conter:
# - src: caminho relativo à pasta static/
# - descricao: legenda opcional
# ------------------------------------------------------------------------------

videos = [
    {"src": "https://youtu.be/XJhx2AI0BfM", "descricao": "Breve demonstração do jogo"},
]

# ------------------------------------------------------------------------------
# Arquivos disponíveis para download
# ------------------------------------------------------------------------------
# Cada item deve conter:
# - nome: nome do arquivo
# - descricao: descrição exibida ao lado do botão
# - arquivo: caminho relativo à pasta static/
# ------------------------------------------------------------------------------

downloads = []
