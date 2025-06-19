"""
Módulo de configuração do projeto para exibição dinâmica no portfólio/blog.

Este módulo define as informações estruturadas sobre um projeto específico,
incluindo dados técnicos, posts, roadmap, imagens, vídeos e arquivos para download.
Ele será importado dinamicamente pelo sistema Flask do site.

Exemplo de uso:
    from data import nome_do_projeto
    dados = carregar_projeto(nome_do_projeto)
"""

# ------------------------------------------------------------------------------
# Nome do projeto (deve corresponder ao nome da pasta e à URL)
# ------------------------------------------------------------------------------

from datetime import datetime # Exemplo: "meu-projeto-avancado"

# ------------------------------------------------------------------------------
# Ficha Técnica
# ------------------------------------------------------------------------------
# Informações exibidas na seção "Ficha Técnica" da página principal do projeto.
# Os campos podem ser deixados em branco ("") caso não se apliquem.
# ------------------------------------------------------------------------------

projeto = "floux"

ficha_tecnica = {
    "nome": "Floux",
    "linguagem": "Python, Javascript, HTML5, CSS3",
    "framework": "Bootrstrap 5, Django (a confirmar)",
    "paradigma": "Programação Orientada a Objetos (OOP)",
    "arquitetura": "Modular, com foco em escalabilidade",
    "tipo_projeto": "rede social onde os usuários se conectam por meio de <strong>temas, ideias e interesses compartilhados</strong>, organizando conversas por fluxos de pensamento",
    "interface": "Interface Web responsiva e adaptável a Desktop e Mobile",
    "funcionalidades": ["Perfis, postagens por assunto, conexões temáticas, curadoria de conteúdo e recomendação inteligente"],
    "bibliotecas": ["pygame", "os", "random"],
    "banco_de_dados": "",
    "api_externa": "",
    "plataforma": "Web (Desktop / Mobile)",
    "resolucao": "",
    "status": "Em fase conceitual e de planejamento"
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
        "titulo": "Um Projeto Ambicioso",
        "data": datetime(2025, 6, 12),
        "autor": "Luiz R. Dererita",
        "nome_arquivo": "post1",
        "conteudo": """
        <p>
          O <strong>Floux</strong> é, sem dúvidas, um dos projetos mais ambiciosos que já concebi até o momento. Diferente de outras iniciativas que surgiram como experimentos, estudos ou homenagens pessoais, este projeto nasceu de uma visão concreta: a de construir uma <strong>plataforma completa</strong>, com potencial para se tornar uma aplicação web de verdade, capaz de escalar, evoluir e talvez até impactar a vida de outras pessoas algum dia.
        </p>
        <p>
          Atualmente, o Floux ainda está em sua fase inicial — com a interface sendo projetada e ajustada com todo cuidado. Trata-se de um sistema web que, por enquanto, é completamente estático. Mas essa é apenas a fundação. A ideia é que ele cresça e ganhe corpo à medida que eu evoluo como desenvolvedor.
        </p>

        <h3 class="section-title mt-4">Motivações</h3>
        <p>
          Sempre sonhei em construir algo meu. Algo que não apenas funcionasse, mas que fosse útil, bonito, escalável e tecnicamente bem estruturado. E, talvez mais importante do que tudo isso: algo que me desafiasse a colocar em prática tudo aquilo que venho aprendendo ao longo da minha jornada de estudos em programação. O Floux representa exatamente isso.
        </p>
        <p>
          Este projeto é um reflexo direto do meu desejo de crescer na área de desenvolvimento web, sair da zona de conforto dos sites estáticos e dar os primeiros passos no universo das aplicações completas, robustas e profissionais. Ele não é só um portfólio ou uma vitrine — ele será, na essência, uma aplicação viva.
        </p>

        <h3 class="section-title mt-4">Tecnologias e Futuro com Django</h3>
        <p>
          Meu plano é utilizar o <strong>Django</strong> como principal framework para o backend do Floux. Escolhi o Django por ser uma tecnologia robusta, madura e extremamente poderosa quando o assunto é <em>desenvolvimento de aplicações web escaláveis</em>. Com ele, pretendo implementar funcionalidades como autenticação de usuários, banco de dados dinâmico, painéis administrativos e lógica de negócios complexas.
        </p>
        <p>
          Quero que o Floux seja mais do que um simples projeto pessoal: quero que ele me obrigue a dominar <strong>CRUDs completos</strong>, <strong>arquitetura MVC</strong>, <strong>boas práticas com Python</strong> e toda a estrutura que envolve aplicações modernas baseadas em servidor. Isso inclui <strong>APIs RESTful</strong>, consumo de serviços externos, integração com frontend dinâmico e responsivo, e até mesmo deploy profissional em servidores como Heroku ou Render.
        </p>

        <h3 class="section-title mt-4">O Potencial do Projeto</h3>
        <p>
          O Floux é uma aplicação modular, que pode se adaptar a diversas finalidades. Ele pode ser um sistema de gestão, um gerador de conteúdo, um painel administrativo, ou até uma central de ferramentas online para freelancers, devs e criadores. Ainda estou estruturando suas direções, mas o importante é que o código será projetado para ser <strong>reutilizável e extensível</strong>. Tudo será feito com foco em <strong>manutenabilidade e crescimento</strong>.
        </p>
        <p>
          O grande diferencial do Floux, para mim, é que ele não nasceu pronto — ele está nascendo junto comigo. À medida que aprendo, aplico. À medida que erro, corrijo. À medida que descubro novas possibilidades, adapto a arquitetura e melhoro o escopo. Isso torna o projeto não só pessoal, mas vivo. Ele se transforma na mesma velocidade que eu me transformo como desenvolvedor.
        </p>

        <h3 class="section-title mt-4">Habilidades Envolvidas</h3>
        <p>
          Para tirar o Floux do papel e levá-lo até o nível que pretendo, sei que terei que reunir uma série de conhecimentos e habilidades:
        </p>
        <ul>
          <li>Domínio de <strong>HTML, CSS e JavaScript</strong> puro para a base da interface;</li>
          <li>Aplicação de <strong>Bootstrap</strong> ou frameworks de UI modernos para prototipagem e responsividade;</li>
          <li>Uso extensivo de <strong>Python</strong> com o framework <strong>Django</strong> para todo o backend;</li>
          <li>Gerenciamento de <strong>banco de dados relacionais</strong>, principalmente com PostgreSQL e SQLite;</li>
          <li>Implementação de <strong>autenticação de usuários</strong>, perfis e dashboards personalizados;</li>
          <li>Criação de <strong>componentes reutilizáveis</strong> e rotas limpas;</li>
          <li>Consumo e criação de <strong>APIs REST</strong> com Django REST Framework;</li>
          <li>Testes unitários e integração com CI/CD para profissionalizar o processo;</li>
          <li>Hospedagem em servidores escaláveis com suporte a <strong>Docker</strong>, Git e versionamento contínuo.</li>
        </ul>

        <h3 class="section-title mt-4">O Caminho pela Frente</h3>
        <p>
          O Floux ainda está longe de sua forma final. Mas tudo bem. Porque ele não precisa ser perfeito agora — ele precisa ser consistente, sincero e real. Pretendo trabalhar nesse projeto com paciência, aplicando os conhecimentos conforme vou adquirindo, sem pular etapas. O importante é construir algo sólido, e não apressado.
        </p>
        <p>
          O Floux está no meu portfólio como uma promessa. Um lembrete constante de que estou construindo algo grande, mesmo que ainda esteja em seus tijolos iniciais. E esse compromisso — comigo mesmo — é o que me motiva todos os dias a continuar estudando, programando e acreditando no que posso construir.
        </p>

        <p class="meta-info">Postado em <strong>8 de Junho de 2025</strong> por <strong>Luiz R. Dererita</strong></p>
        
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
    {"alerta": "Este projeto ainda está em fase de planejamento e amadurecimento da ideia"},

    # METAS
    {"status": "concluido", "meta": "Pesquisa de referências de redes sociais (Instagram, Threads, Reddit, Mastodon...)"},
    {"status": "desenvolvimento", "meta": "Documentação da visão do produto e diferenciais da Floux"},
    {"status": "desenvolvimento", "meta": "Estudo sobre conexões temáticas e fluxos de conteúdo entre usuários"},
    {"status": "planejado", "meta": "Criação dos primeiros wireframes (perfil, feed, postagem por assunto)"},
    {"status": "planejado", "meta": "Planejamento de funcionalidades principais e mapa de navegação"},
    {"status": "planejado", "meta": "Escolha definitiva do backend (Django ou outro)"},
    {"status": "planejado", "meta": "Modelagem inicial do banco de dados e estrutura modular"},
    {"status": "planejado", "meta": "Sistema de autenticação e criação de perfis"},
    {"status": "planejado", "meta": "Implementação do feed com postagens temáticas conectadas"},
    {"status": "planejado", "meta": "Criação de sistema de curadoria e tags inteligentes"},
    {"status": "planejado", "meta": "Testes de usabilidade e ajustes com feedback real"},
    {"status": "planejado", "meta": "Integração com API de recomendação baseada em interesses"},
    {"status": "planejado", "meta": "Implementação de notificações e mensagens privadas"},
    {"status": "planejado", "meta": "Lançamento Alpha fechado para usuários convidados"},
]

# ------------------------------------------------------------------------------
# Galeria de imagens
# ------------------------------------------------------------------------------
# Cada imagem deve conter:
# - src: caminho relativo à pasta static/
# - descricao: legenda exibida ao lado da imagem
# ------------------------------------------------------------------------------

imagens = [
    {"src": "img/floux/print_1.png", "descricao": "Tela Inicial do Floux (Em desenvolvimento)"},
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
