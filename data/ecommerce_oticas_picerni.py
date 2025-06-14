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

projeto = "ecommerce-oticas-picerni"  # Exemplo: "meu-projeto-avancado"

# ------------------------------------------------------------------------------
# Ficha Técnica
# ------------------------------------------------------------------------------
# Informações exibidas na seção "Ficha Técnica" da página principal do projeto.
# Os campos podem ser deixados em branco ("") caso não se apliquem.
# ------------------------------------------------------------------------------

ficha_tecnica = {
    "nome": "E-commerce Óticas Picerni", 
    "linguagem": "HTML5, CSS3, JavaScript",
    "framework": "Bootstrap 5",
    "paradigma": "",
    "arquitetura": "",
    "tipo_projeto": "Plataforma digital para venda de óculos e acessórios ópticos",
    "interface": "App Web com Layout Responsivo, moderno e acessível",
    "funcionalidades": [],
    "bibliotecas": ["pygame", "os", "random"],
    "banco_de_dados": "",
    "api_externa": "",
    "plataforma": "Web (Desktop / Mobile)",
    "resolucao": "",
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
        "titulo": "O Poder da Gratidão",
        "data": datetime(2025, 6, 12),
        "autor": "Luiz R. Dererita",
        "nome_arquivo": "post1",
        "conteudo": """
        <p>
          Este projeto é muito mais do que uma simples página de uma ótica. Ele é uma homenagem, uma forma de gratidão e um registro simbólico de uma fase essencial da minha trajetória como desenvolvedor. Estou falando do site da <strong>Óticas Picerni</strong>, um protótipo de e-commerce que iniciei como forma de retribuir a confiança de pessoas muito especiais que acreditaram em mim quando eu ainda era apenas um curioso na área da tecnologia.
        </p>

        <h3 class="section-title mt-4">Uma Experiência que Mudaria Tudo</h3>
        <p>
          Antes de mergulhar de vez na programação, tive uma experiência marcante trabalhando em uma ótica física. O dono, um microempreendedor batalhador, confiou em mim para assumir um papel estratégico na empresa — ele sabia do meu interesse por tecnologia e decidiu apostar no meu potencial. Na época, minha experiência era voltada principalmente para o <strong>Design Gráfico</strong>, com conhecimentos em ferramentas como <code>Photoshop</code> e <code>Adobe Illustrator</code>, mas minha bagagem com <strong>Marketing Digital</strong> era ainda bastante rasa.</p>
        <p>Para ser honesto, eu nem sequer trabalhava com tecnologia. Tinha acabado de sair de um contrato de <em>Jovem Aprendiz</em>, e sido efetivado como <em>Auxiliar Adminsitrativo</em> no <strong>Sindicato das Costureiras e Alfaiates de São Paulo e Osasco</strong>. Além de minhas aspirações pessoais com desenvolvimento de jogos, que até então era um hobbye para mim, eu não sabia nada sobre trabalhar com computadores.</p>
        <p>
          Mesmo assim, ele me deu uma oportunidade única: fui convidado a ser o braço direito dele na implantação do setor de marketing da empresa. Ele acreditava que eu poderia, futuramente, me tornar o gerente desse setor — e não mediu esforços para me apoiar. Fui encarregado de escolher o notebook que seria usado exclusivamente para essa área e tive total liberdade para utilizar o aparelho durante os horários vagos para estudar.
        </p>

        <h3 class="section-title mt-4">Horas a Mais, Sonhos a Caminho</h3>
        <p>
          Todos os dias, eu chegava quase duas horas mais cedo na loja. E quando o expediente terminava, eu ainda ficava mais duas ou três horas estudando, testando códigos, rabiscando ideias, tentando entender como tudo funcionava. Foi ali, naquele ambiente silencioso depois do fechamento, que a sementinha da programação brotou de verdade no meu coração.
        </p>
        <p>
          Comprei diversos cursos na <strong>Udemy</strong>, e embora eu admita (com um sorriso meio sem graça) que ainda não concluí todos eles, posso dizer com certeza que foi essa fase que me moldou. Foi ali que eu decidi, de vez, que queria ser programador.
        </p>

        <h3 class="section-title mt-4">Fracasso Técnico, Crescimento Pessoal</h3>
        <p>
          Infelizmente, apesar de todos os esforços, não consegui atender completamente às demandas da empresa como profissional de Marketing Digital. Era uma época difícil: pandemia, vendas baixas, desafios de adaptação ao ambiente digital... E mesmo com tudo que aprendi e me esforcei, a verdade é que a empresa também não estava totalmente preparada para os desafios que enfrentávamos naquele cenário.
        </p>
        <p>
          Acabei me desligando, com um sentimento de frustração por não ter conseguido entregar tudo o que gostaria. Mas com muito respeito, carinho e gratidão por tudo o que vivi com aquele casal que me acolheu como parte da família. Cultivamos uma relação de amizade verdadeira, e sou eternamente grato por cada gesto de confiança que recebi naquele lugar.
        </p>

        <h3 class="section-title mt-4">Um Projeto por Gratidão</h3>
        <p>
          Foi pensando nisso tudo que decidi criar esse projeto. Mesmo que eu nunca tenha tido tempo para voltar lá, ou nem mesmo tenha contado para eles que comecei esse site, eu queria expressar minha gratidão de alguma forma. É por isso que comecei o desenvolvimento do site da <strong>Óticas Picerni</strong>, ainda que simples, como uma homenagem.
        </p>
        <p>
          Por enquanto, trata-se apenas de uma <strong>página estática</strong> que simula a presença online da ótica. Mas minha intenção é continuar o projeto aos poucos e, futuramente, transformá-lo em um <strong>e-commerce funcional</strong>, com sistema de catálogo, carrinho de compras, login de cliente, entre outros recursos. Quero entregar algo real, completo, como presente para o meu ex-patrão — uma forma de retribuir tudo que ele acreditou que eu poderia ser.
        </p>

        <h3 class="section-title mt-4">Inspiração Técnica</h3>
        <p>
          O projeto teve início a partir de um <strong>material em PDF da Alura</strong> sobre desenvolvimento web, que encontrei e estudei por conta própria. Peguei como base as instruções e conceitos apresentados no material e fui adaptando, personalizando e aplicando meus próprios estilos, conceitos de design e identidade visual, sempre pensando no universo de uma ótica real.
        </p>
        <p>
          Apesar da simplicidade inicial, o projeto demonstra minhas habilidades como <strong>Desenvolvedor Front-end</strong> e mostra meu cuidado com estruturação, layout, responsividade e clareza visual. É um projeto que, por mais modesto que pareça à primeira vista, representa uma ponte entre o que fui, o que estou me tornando e o que ainda quero ser.
        </p>

        <h3 class="section-title mt-4">Reflexão Final</h3>
        <p>
          Esse projeto representa, para mim, muito mais do que um código. É memória, é gratidão, é aprendizado. Ele faz parte do meu portfólio não apenas pelo que é agora, mas pelo que representa — como experiência humana, como símbolo da minha caminhada e como prova de que cada passo conta, mesmo quando ainda estamos engatinhando.
        </p>
        <p>
          Continuarei este e outros projetos conforme o tempo permitir. Sempre carregando comigo as pessoas que, de alguma forma, me ajudaram a chegar até aqui — mesmo quando nem elas sabiam o quanto estavam fazendo por mim.
        </p>

        <p class="meta-info" id="postagens">Postado em <strong>8 de Junho de 2025</strong> por <strong>Luiz R. Dererita</strong></p>

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
    {"status": "concluido", "meta": "Criação do layout da página principal"},
    {"status": "concluido", "meta": "Criação de identidade visual e paleta de cores personalizada"},
    {"status": "desenvolvimento", "meta": "Desenvolvimento responsivo com Bootstrap 5"},
    {"status": "planejado", "meta": "Design das páginas internas (produtos, contato, carrinho, etc.)"},
    {"status": "planejado", "meta": "Escolha do framework backend (Django, Laravel, ou outra solução)"},
    {"status": "planejado", "meta": "Configuração do ambiente de desenvolvimento backend"},
    {"status": "planejado", "meta": "Modelagem do banco de dados"},
    {"status": "planejado", "meta": "Estruturação das rotas e componentes principais"},
    {"status": "planejado", "meta": "Cadastro e visualização de produtos"},
    {"status": "planejado", "meta": "Filtro por categoria, gênero e tipo de armação"},
    {"status": "planejado", "meta": "Sistema de busca inteligente"},
    {"status": "planejado", "meta": "Implementação do carrinho de compras"},
    {"status": "planejado", "meta": "Sistema de cadastro/login de clientes"},
    {"status": "planejado", "meta": "Integração com meios de pagamento (Pix, boleto e cartão)"},
    {"status": "planejado", "meta": "Criação de painel administrativo para a equipe da ótica"},
    {"status": "planejado", "meta": "Otimização para SEO e performance mobile"},
    {"status": "planejado", "meta": "Testes gerais e validação de usabilidade"},
    {"status": "planejado", "meta": "Publicação do site em ambiente de produção"},
]

# ------------------------------------------------------------------------------
# Galeria de imagens
# ------------------------------------------------------------------------------
# Cada imagem deve conter:
# - src: caminho relativo à pasta static/
# - descricao: legenda exibida ao lado da imagem
# ------------------------------------------------------------------------------

imagens = [
    {"src": "img/ecommerce-oticas-picerni/print_1.png", "descricao": "Tela de boas-vindas do E-commerce"},
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
