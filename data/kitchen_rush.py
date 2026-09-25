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

projeto = "kitchen-rush"

# ------------------------------------------------------------------------------
# Ficha Técnica
# ------------------------------------------------------------------------------
# Informações exibidas na seção "Ficha Técnica" da página principal do projeto.
# Os campos podem ser deixados em branco ("") caso não se apliquem.
# ------------------------------------------------------------------------------

ficha_tecnica = {
    "nome": "Kitchen Rush",
    "linguagem": "Python",
    "framework": "",
    "paradigma": "Programação Orientada a Objetos (OOP)",
    "arquitetura": "MVC + State Pattern",
    "tipo_projeto": "Jogo 2D estilo simulador com caracteristicas de RPG",
    "interface": "Interface gráfica personalizada com sprites e animações",
    "funcionalidades": [
        "Interatividade estilo Point e Click",
        "Sistema de gerenciamento de setores",
        "Reações dos personagens influencia no jogo",
        "Personalização do restaurante"
    ],
    "bibliotecas": ["pygame", "os", "random"],
    "banco_de_dados": "",
    "api_externa": "",
    "plataforma": "Desktop (Windows / Linux)",
    "resolucao": "960x540",
    "status": "Em desenvolvimento"
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
        "titulo": "A Ideia para Kitchen Rush",
        "data": datetime(2025, 6, 11),
        "autor": "Luiz R. Dererita",
        "nome_arquivo": "post1",
        "conteudo": """
        <p><strong>Kitchen Rush</strong> é um jogo de simulação e estratégia 2D inspirado no caos — e no charme — do cotidiano de um restaurante movimentado. Nele, o jogador gerencia mesas, atende clientes, designa funcionários, lida com eventos especiais e precisa manter a reputação do restaurante em alta para garantir seu sucesso. Tudo isso em um ciclo diário que simula turnos de trabalho, pagamentos, contratações e desafios imprevisíveis.</p>

        <h3 class="section-title mt-4">Como Tudo Começou</h3>
        <p>A ideia de criar <strong>Kitchen Rush</strong> não surgiu do nada. Ela nasceu diretamente da minha vivência no mundo real. Atualmente, eu ganho a vida como garçom em um restaurante japonês. Ali, vivo de perto as pressões de um ambiente dinâmico, onde cada minuto conta, onde erros simples viram confusão, e onde o bom atendimento depende de sincronia entre todos os setores: salão, cozinha, sushibar, caixa, recepção...</p>
        <p>Foi observando os bastidores, os conflitos silenciosos, os improvisos geniais e os estresses do dia a dia que percebi: “isso daria um jogo”. Mas não apenas um jogo de fazer pratos ou correr com bandejas — eu queria capturar a complexidade da gestão de um restaurante: lidar com salários, folgas, clientes difíceis, funcionários que se recusam a trabalhar se não forem pagos, dias de alta demanda, e até mesmo imprevistos como aniversários surpresa ou visitas de críticos gastronômicos.</p>

        <h3 class="section-title mt-4">Do Caos Real ao Código</h3>
        <p>Desenvolver o Kitchen Rush tem sido uma das experiências mais intensas e longas que já enfrentei como programador. O projeto começou de forma tímida, com algumas mesas estáticas e um relógio digital rodando em uma tela escura. Mas eu sabia que queria mais. A cada dia, eu desenhava algo novo, implementava uma ideia que tinha visto acontecer no meu trabalho real. O jogo foi crescendo em estrutura e em profundidade, e eu fui crescendo junto com ele.</p>
        <p>Um dos maiores desafios foi organizar o projeto para que ele se mantivesse modular e escalável. Por isso, utilizei uma arquitetura baseada em estados (State Pattern), com uma HUD interativa e múltiplas telas de gerenciamento: cardápio, supermercado, calendário, contratação de funcionários, melhorias do restaurante e muito mais.</p>

        <h3 class="section-title mt-4">Uma Simulação com Identidade</h3>
        <p>Diferente de jogos tradicionais de restaurante, o Kitchen Rush não foca apenas na ação frenética. Ele traz elementos de administração real. Todo 5º dia útil do mês, por exemplo, é necessário pagar os salários dos funcionários. É possível contratar garçons, cozinheiros, chefs e gerentes. O jogador pode decorar o salão, expandir mesas e cadeiras, personalizar o cardápio e enfrentar clientes especiais que afetam a dinâmica do dia.</p>
        <p>Cada fase representa um “dia de trabalho”, com um relógio que simula 12 horas em 12 minutos. O ritmo do jogo é ajustável, e há um sistema de reputação que influencia a chegada de novos clientes. Tudo foi pensado para transmitir o desafio de equilibrar qualidade, agilidade e gestão.</p>

        <h3 class="section-title mt-4">Reflexão Pessoal</h3>
        <p>Kitchen Rush não é apenas um projeto técnico. É quase um retrato digital da minha vivência, uma forma de transformar rotinas exaustivas e histórias que vivi em algo interativo e criativo. Cada detalhe — desde a disposição das mesas até os sons do salão — carrega um pouco da minha experiência real no setor de atendimento.</p>
        <p>Esse jogo representa também uma virada na minha vida como desenvolvedor. Foi nele que coloquei em prática tudo o que aprendi sobre estruturação de código, organização visual, efeitos sonoros, otimização e imersão. E ainda está em construção — como um restaurante que está sempre evoluindo. Mas acima de tudo, é um lembrete de que até as situações mais comuns podem se tornar inspiração para algo extraordinário.</p>
        
        <p>Falta muito para <strong>Kitchen Rush</strong> finalmente estar pronto para ser publicado como um jogo de verdade. Por enquanto, muita coisa ainda está no mundo das ideias. Possibilidades, mecânicas, Design... Eu venho trabalhando no jogo quando tenho tempo. Mas devido a rotina de trabalho no restaurante e o fechamento do Semestre na Faculdade, já faz um bom tempo que não paro para trabalhar no projeto. Mas este, com certeza, é um projeto que terei o prazer de finalizar!</p>
        <p class="meta-info" id="postagens">Postado em <strong>10 de Junho de 2025</strong> por <strong>Luiz R. Dererita</strong></p>
        """,
    },

    {
        "titulo": "Atualizações do Kitchen Rush — Novos sistemas e melhorias!",
        "data": datetime(2025, 10, 10),
        "autor": "Luiz R. Dererita",
        "nome_arquivo": "post2",
        "conteudo": """
        <h2>Atualizações do Kitchen Rush — Novos sistemas, animações e ideias tomando forma!</h2>

        <p>Olá, pessoal! Já faz um bom tempo desde a última atualização do <strong>Kitchen Rush</strong>, não é? 😅 Esse jogo foi um dos primeiros projetos que inauguraram o meu portfólio, e desde então muita coisa aconteceu. Desde a publicação do meu site, venho dividindo meu tempo entre inúmeros projetos, a faculdade, o trabalho e os compromissos pessoais do dia a dia. É muita coisa — e manter uma constância nos meus projetos acaba sendo um verdadeiro desafio.</p>
        <p>Mas... cá estamos nós novamente (risos). E, sim, <strong>o Kitchen Rush está vivo!</strong> 🌟 Nos últimos meses, consegui dedicar um bom tempo ao desenvolvimento do jogo e estou animado para compartilhar com vocês o que mudou desde o último post.</p>

        <h3 class="section-title mt-4">De ideias no papel a sistemas funcionais</h3>
        <p>Se você já conferiu o vídeo de demonstração na seção <strong>“Vídeos”</strong> do site, deve ter notado que até pouco tempo atrás o jogo ainda estava em um estágio bem inicial. No último post, apresentei várias ideias para o futuro do projeto — e, aos poucos, essas ideias estão finalmente começando a tomar forma.</p>
        <p>Antes, o jogo contava apenas com a <strong>tela do Menu Principal</strong> e um layout inicial da <strong>tela de gameplay</strong>. Não havia clientes de fato no salão — no lugar deles, existia apenas um <strong>protótipo do sistema de clientes</strong>, representado por pequenos blocos coloridos que apareciam aleatoriamente nas mesas. Esses blocos simbolizavam cada cliente, mas ainda não havia nenhuma representação visual do sistema de paciência (eles simplesmente apareciam e desapareciam quando a paciência acabava).</p>

        <h3 class="section-title mt-4">Sistema de paciência com barras visuais</h3>
        <p>Uma das principais adições é o novo <strong>sistema de paciência visível</strong>, agora representado por <strong>barras acima de cada mesa</strong>. Essas barras registram a <strong>paciência coletiva</strong> do grupo de clientes, e não a de cada cliente individualmente — ou seja, a barra de uma mesa representa o humor e a tolerância de todo o grupo.</p>
        <p>Por questões de boa UX e clareza visual, busquei criar uma interface minimalista, mas intuitiva. A barra começa verde e, conforme o tempo passa, <strong>muda gradualmente para o vermelho</strong>, sinalizando que os clientes estão perdendo a paciência. Isso traz identidade, urgência e clareza para o jogador, que consegue entender rapidamente o que está acontecendo no salão e agir antes que os clientes desistam do pedido.</p>

        <h3 class="section-title mt-4">Trilha sonora e ambientação</h3>
        <p>Na parte artística, o projeto também ganhou <strong>uma trilha sonora de fundo</strong> durante o gameplay. A música, com ritmo contagiante de <strong>jazz</strong>, cria uma atmosfera agradável e imersiva, transmitindo perfeitamente a <strong>vibe de um restaurante movimentado</strong>. O som ambiente e o ritmo da música ajudam a envolver o jogador e reforçam a identidade visual e sonora do <strong>Kitchen Rush</strong>.</p>

        <h3 class="section-title mt-4">Novas animações e fluidez na interface</h3>
        <p>Outra melhoria significativa foi a adição de <strong>novas animações e fluidez nas interações gráficas</strong>. Os botões usados para abrir telas intermediárias durante o gameplay (como o <strong>Cardápio</strong> ou o <strong>Supermercado</strong>) agora contam com <strong>transições suaves</strong>, tornando a navegação mais agradável e reforçando a sensação de qualidade e polimento na experiência visual do jogo.</p>

        <h3 class="section-title mt-4">Cardápio expandido, habilidades e previews de pratos</h3>
        <p>O <strong>Cardápio</strong> do jogo também recebeu bastante atenção. Agora ele está praticamente concluído e conta com <strong>muitos novos pratos</strong> adicionados ao sistema. Durante o gameplay, o jogador poderá <strong>expandir seu cardápio</strong> à medida que desbloquear <strong>novas receitas</strong>, tornando o gerenciamento da cozinha mais estratégico e recompensador.</p>
        <p>Alguns pratos <strong>possuem habilidades especiais</strong> que influenciam diretamente o andamento do jogo. Por exemplo, certos pratos podem <strong>melhorar a paciência dos clientes</strong> — especialmente quando o pedido inclui algo mais demorado. Se houver na sua equipe um <strong>garçom carismático</strong> o suficiente para convencer o cliente a experimentar um desses pratos, isso pode <strong>melhorar a experiência geral</strong> e até <strong>gerar gorjetas generosas</strong>. 💸</p>
        <p>Além disso, foi adicionada uma nova função de <strong>pré-visualização dos pratos</strong>. Agora, ao clicar em um prato no cardápio, o jogador vê uma <strong>arte ampliada</strong> do prato acompanhada de um <strong>campo descritivo</strong> com detalhes sobre ele, suas <strong>habilidades</strong> (quando houver), <strong>ingredientes utilizados</strong>, <strong>número de estrelas</strong> (indicando popularidade) e o <strong>preço</strong> correspondente. Essa adição deixa a experiência mais completa, visual e informativa.</p>
        <p>Você deve estar se perguntando: “Mas como tudo isso vai funcionar tecnicamente?” Para ser honesto... eu também não sei! (risos) Muita coisa ainda está sendo experimentada e ajustada conforme o projeto evolui — e essa é justamente a parte divertida de desenvolver um jogo independente: ter liberdade para improvisar e deixar o projeto se moldar naturalmente.</p>

        <h3 class="section-title mt-4">Tela do Supermercado e gerenciamento de recursos</h3>
        <p>Também comecei a trabalhar melhor na <strong>tela do Supermercado</strong>. Agora, <strong>os ingredientes comprados são subtraídos do dinheiro do jogador</strong>, tornando o gerenciamento de recursos mais tangível e próximo do que espero para a versão final. Esse sistema ainda está em estágio inicial, mas já é funcional e abre espaço para novos recursos relacionados à economia do jogo no futuro.</p>

        <h3 class="section-title mt-4">Seleção e criação de Restaurantes (sistema de saves)</h3>
        <p>Outra novidade é a <strong>tela intermediária</strong> antes de iniciar o gameplay, que funcionará como uma <strong>tela de seleção e criação de restaurantes</strong>. Ela será responsável por <strong>gerenciar os slots de salvamento</strong>, permitindo ao jogador criar e escolher diferentes restaurantes salvos — algo essencial para a progressão e rejogabilidade.</p>
        <p>Por enquanto, tanto essa tela quanto o sistema do Supermercado estão em <strong>fase inicial de desenvolvimento</strong>, mas já possuem <strong>estrutura funcional básica</strong>, o que me deixa bastante empolgado com o rumo do projeto.</p>

        <h3 class="section-title mt-4">Bastidores: melhorias no site e novas mídias em breve</h3>
        <p>Esse post também me fez perceber que o <strong>meu site portfólio</strong> precisa de uma refatoração. Atualmente, as postagens são criadas dinamicamente por meio de um <strong>módulo Python</strong>, o que facilita muito a publicação de atualizações. No entanto, percebi que ainda falta suporte adequado para <strong>imagens e vídeos nos posts</strong> devido a isso, não foi possível adicionar conteúdo visual à este post — e isso é algo que pretendo resolver em breve.</p>
        <p>Enquanto isso, convido vocês a visitarem as seções de <strong>“Imagens”</strong> e <strong>“Vídeos”</strong>, onde todo o conteúdo adicional (imagens e/ou vídeos) serão acrescentados ao projeto, para que vocês possam <strong>ver de perto as novidades</strong> mencionadas em cada post.</p>

        <h3 class="section-title mt-4">Encerrando</h3>
        <p>Muito obrigado por acompanharem o projeto até aqui! Essas pequenas evoluções significam muito para mim e mostram que, mesmo devagar, o <strong>Kitchen Rush</strong> está ganhando vida.</p>
        <p>Continuem acompanhando — e fiquem à vontade para deixar sugestões, ideias ou apenas uma mensagem de incentivo. Até a próxima atualização! 👋</p>

        <p class="meta-info" id="postagens">Postado em <strong>10 de Outubro de 2025</strong> por <strong>Luiz R. Dererita</strong></p>
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
    {"status": "concluido", "meta": "Criação da Splash Screen e Menu Principal"},
    {"status": "concluido", "meta": "Implementação da tela de gameplay com background e HUD"},
    {"status": "planejado", "meta": "Desenvolvimento do sistema de fases baseado em dias úteis"},
    {"status": "planejado", "meta": "Sistema de pausa e save/load de progresso"},
    {"status": "concluido", "meta": "Renderização e organização das mesas e cadeiras"},
    {"status": "concluido", "meta": "Programação de clientes com grupos variados e bosses"},
    {"status": "planejado", "meta": "Sistema de reputação e avaliação do restaurante"},
    {"status": "planejado", "meta": "Implementação de decorações e upgrades físicos"},
    {"status": "planejado", "meta": "Tela de contratação e designação de funcionários"},
    {"status": "concluido", "meta": "Classe `Employee` e subclasses `Waiter`, `Cook`, `Manager`, `Chef`"},
    {"status": "planejado", "meta": "Folha de pagamento e disponibilidade de funcionários"},
    {"status": "planejado", "meta": "Sistema de upgrades individuais para funcionários"},
    {"status": "concluido", "meta": "HUD com relógio funcional e contador de dinheiro"},
    {"status": "planejado", "meta": "Popup de Supermercado com sistema de compra de ingredientes"},
    {"status": "planejado", "meta": "Algoritmo de atendimento automático e rotinas dos funcionários"},
    {"status": "planejado", "meta": "Sistema de fases com eventos aleatórios e desafios por dia"},
    {"status": "planejado", "meta": "Implementação de feedbacks dos clientes"},
    {"status": "planejado", "meta": "Power-ups e itens temporários (como café, energia, etc.)"},
    {"status": "desenvolvimento", "meta": "Trilha sonora e efeitos sonoros personalizados"},
    {"status": "desenvolvimento", "meta": "Sistema de animação por bones e personalização dos personagens"},
    {"status": "planejado", "meta": "Build e adaptação para versão web/jogável no navegador"},
]

# ------------------------------------------------------------------------------
# Galeria de imagens
# ------------------------------------------------------------------------------
# Cada imagem deve conter:
# - src: caminho relativo à pasta static/
# - descricao: legenda exibida ao lado da imagem
# ------------------------------------------------------------------------------

imagens = [
    {"src": "img/kitchen-rush/gameplay.png", "descricao": "Gameplay da primeira fase"},
    {"src": "img/kitchen-rush/menu-principal.png", "descricao": "Menu principal do jogo"},
    {"src": "img/kitchen-rush/gameplay-2.png", "descricao": "Medidores de paciência adicionados às mesas"},
    {"src": "img/kitchen-rush/supermercado.png", "descricao": "Protótipo da tela do supermercado tomando forma"},
    {"src": "img/kitchen-rush/cardapio-2.png", "descricao": "Cardápio expandido com novos pratos e pré-visualização"},
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
        "youtube_id": "zfFwE3YUQB4",
        "descricao": "Breve demonstração de como está ficando o jogo"
    },

    {
        "youtube_id": "aED-1KFs2Bc",
        "descricao": "Novas atualizações do Kitchen Rush (Outubro de 2025)"
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

downloads = []

# ------------------------------------------------------------------------------
# Cartão de exibição na Home
# ------------------------------------------------------------------------------

home_card = {
    "resumo": "Protótipo de jogo de gerenciamento de restaurante com arte original e interface modular interativa.",
    "categoria": "jogos",
    "tecnologias": ["Python", "Pygame", "POO", "MVC"],
    "imagem": "img/kitchen_rush_preview.png",
    "ordem": 40,
}
