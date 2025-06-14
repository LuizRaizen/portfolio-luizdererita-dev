"""Lista de postagens do blog do Kitchen Rush."""

from datetime import datetime

# Nome do projeto para ser identificado na URL
projeto = "kitchen-rush"

# Informações qu aparecem na seção "Ficha Técnica" da Página Inicial
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

# Lista de postagens feitas no blog
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
]

# Lista de metas definidas para a conclusão do projeto
roadmap = [
    {"status": "concluido", "meta": "Interface gráfica finalizada"},
    {"status": "desenvolvimento", "meta": "Integração com API da OpenAI"},
    {"status": "planejado", "meta": "Envio automático de e-mails"},
    {"alerta": "Este projeto está em fase de desenvolvimento"}
]

# Lista de imagens do projeto que aparecem na página "Imagens"
imagens = [
    {"src": "img/kitchen-rush/gameplay.png", "descricao": "Gameplay da primeira fase"},
    {"src": "img/kitchen-rush/menu-principal.png", "descricao": "Menu principal do jogo"},
]

# Lista de vídeos do projeto que aparecem na página "Vídeos"
videos = [
    {"src": "https://www.youtube.com/embed/zfFwE3YUQB4?si=Pi0l-95VyOLGyctC", "descricao": "Video demonstrativo do jogo"},
]

# Lista de arquivos disponíveis para download na página "Downloads"
downloads = []
