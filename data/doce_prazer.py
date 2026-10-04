"""
Blog do projeto Doce Prazer — cardápio digital para uma confeitaria artesanal.
Fonte das informações: repositório https://github.com/LuizRaizen/doce-prazer-site
"""

from datetime import datetime

# ------------------------------------------------------------------------------
# Nome do projeto (deve corresponder ao nome da pasta e à URL)
# ------------------------------------------------------------------------------

projeto = "doce-prazer"
repositorio = "https://github.com/LuizRaizen/doce-prazer-site"  # o repositório tem nome diferente do slug

# ------------------------------------------------------------------------------
# Ficha Técnica
# ------------------------------------------------------------------------------

ficha_tecnica = {
    "nome": "Doce Prazer",
    "linguagem": "JavaScript",
    "framework": "",
    "paradigma": "Programação orientada a eventos (DOM)",
    "arquitetura": "Front-end estático: HTML, CSS e JavaScript puros, sem framework",
    "tipo_projeto": "Cardápio digital com carrinho e pedido por PIX e WhatsApp",
    "interface": "Web responsiva (celular, tablet, notebook e desktop)",
    "funcionalidades": [
        "Cardápio de ovos de Páscoa organizado por categoria",
        "Escolha de sabores com validação antes de adicionar ao carrinho",
        "Carrinho flutuante com total, salvo no navegador (localStorage)",
        "Pagamento por PIX com QR Code gerado na própria página",
        "Envio do resumo do pedido pelo WhatsApp",
        "Seção de ajuda com o passo a passo do pedido",
    ],
    "bibliotecas": ["Font Awesome", "Google Fonts (Playfair Display e Poppins)", "Biblioteca de QR Code"],
    "banco_de_dados": "",
    "api_externa": ["WhatsApp (link de pedido)"],
    "plataforma": "Web (celular e desktop)",
    "resolucao": "",
    "status": "Concluído (edição de Páscoa)",
}

# ------------------------------------------------------------------------------
# Postagens do blog
# ------------------------------------------------------------------------------

posts = [
    {
        "titulo": "Doce Prazer: o cardápio digital que fiz para a confeitaria da minha esposa",
        "data": datetime(2026, 3, 13),
        "autor": "Luiz R. Dererita",
        "nome_arquivo": "apresentando-o-doce-prazer",
        "imagem": "img/doce-prazer/cardapio.webp",
        "resumo": "Um cardápio interativo para os ovos de Páscoa da confeitaria da minha esposa: o cliente escolhe sabores, monta o carrinho, paga por PIX e envia o pedido pelo WhatsApp.",
        "tags": ["Front-end", "JavaScript", "PIX", "Projeto real"],
        "conteudo": """
        <p>
          O <strong>Doce Prazer</strong> é um projeto diferente dos outros que mostro aqui, porque nasceu de uma necessidade real:
          minha esposa é confeiteira e, na Páscoa, estava vendendo ovos de chocolate artesanais.
          Eu quis ajudar do jeito que sei, e criei um cardápio digital para a confeitaria dela.
        </p>

        <h3 class="section-title mt-4">O que é</h3>
        <p>
          Um <strong>cardápio interativo online</strong> para uma confeitaria artesanal. A cliente abre o link no celular,
          escolhe os ovos, personaliza o pedido, paga por PIX e manda tudo para a confeiteira pelo WhatsApp.
          O visual segue a identidade da marca, com rosa e dourado, <em>Playfair Display</em> nos títulos e <em>Poppins</em> no texto.
        </p>

        <h3 class="section-title mt-4">O cardápio</h3>
        <p>
          São cinco categorias, com preços de <strong>R$ 15,00 a R$ 150,00</strong>:
        </p>
        <ul>
          <li><strong>Ovos Chocolate Blend (Casca)</strong></li>
          <li><strong>Ovos Recheados</strong></li>
          <li><strong>Caixa Mini Ovos Recheados</strong></li>
          <li><strong>Ovos de Colher</strong></li>
          <li><strong>Ovos Quatro Sabores (Bem Recheados)</strong></li>
        </ul>
        <p>
          Cada produto tem botões de quantidade e, quando leva recheio, um seletor de sabor. Há também uma seção com os sabores disponíveis.
        </p>

        <h3 class="section-title mt-4">Do carrinho ao pagamento</h3>
        <p>O fluxo foi pensado para ser simples para quem compra e confiável para quem vende:</p>
        <ol>
          <li>O cliente escolhe os ovos. Se o produto tem sabor, o site <strong>não deixa adicionar sem escolher um sabor</strong>, o que evita pedido incompleto.</li>
          <li>Um <strong>carrinho flutuante</strong> mostra os itens e o total o tempo todo. O carrinho fica salvo no navegador (<code>localStorage</code>), então não se perde se a página for recarregada.</li>
          <li>O <strong>resumo do pedido</strong> mostra os itens, os sabores escolhidos e o valor final.</li>
          <li>O <strong>pagamento por PIX</strong> gera um QR Code com o valor do pedido, mostra a chave e orienta o envio do comprovante.</li>
          <li>O pedido segue para o <strong>WhatsApp</strong> da confeiteira, já com o resumo montado.</li>
        </ol>
        <p>
          Um detalhe técnico de que gosto: o código do PIX (o chamado <em>BR Code</em>) é montado na própria página, no formato do Banco Central,
          com cálculo do <strong>CRC16</strong>, e vira o QR Code. Não há servidor nem intermediário de pagamento.
        </p>

        <h3 class="section-title mt-4">Tecnologia</h3>
        <p>
          Usei só <strong>HTML, CSS e JavaScript</strong>, sem framework. Para um cardápio com carrinho, a escolha manteve o site leve, rápido no celular
          e fácil de hospedar. O layout é responsivo, com ajustes para telas pequenas, tablets, notebooks e desktops.
          O repositório também traz um <code>manifest.json</code> e um <code>sw.js</code> (service worker simples, com cache) e a configuração do
          <strong>Wrangler</strong>, que deixa o projeto pronto para ser publicado na Cloudflare.
        </p>

        <h3 class="section-title mt-4">Por que ele é especial para mim</h3>
        <p>
          Aqui o usuário final é real: a confeiteira usa o cardápio para vender e os clientes o abrem no celular para pedir.
          O fluxo é curto, o sabor é obrigatório quando o produto tem recheio e o pagamento fica a poucos toques do carrinho.
          Gosto de ver código resolvendo um problema do dia a dia de alguém que me é próximo.
        </p>
        <p>
          O código está no GitHub: <a href="https://github.com/LuizRaizen/doce-prazer-site" target="_blank" rel="noopener">LuizRaizen/doce-prazer-site</a>.
        </p>
        """,
    },
]

# ------------------------------------------------------------------------------
# Roadmap do projeto
# ------------------------------------------------------------------------------

roadmap = [
    {"status": "concluido", "meta": "Estrutura do cardápio com categorias, preços e quantidades"},
    {"status": "concluido", "meta": "Identidade visual rosa e dourado, responsiva (celular a desktop)"},
    {"status": "concluido", "meta": "Seletor de sabores com validação antes de adicionar ao carrinho"},
    {"status": "concluido", "meta": "Carrinho flutuante salvo no navegador"},
    {"status": "concluido", "meta": "Resumo do pedido e pagamento por PIX com QR Code"},
    {"status": "concluido", "meta": "Envio do pedido pelo WhatsApp"},
    {"status": "concluido", "meta": "Seção de ajuda com o passo a passo do pedido"},
]

# ------------------------------------------------------------------------------
# Galeria de imagens
# ------------------------------------------------------------------------------

imagens = [
    {"src": "img/doce-prazer/hero.webp", "descricao": "Página inicial do Doce Prazer, com o convite para a Páscoa"},
    {"src": "img/doce-prazer/cardapio.webp", "descricao": "Cardápio com os ovos Chocolate Blend, preços e controle de quantidade"},
]

# ------------------------------------------------------------------------------
# Vídeos do projeto
# ------------------------------------------------------------------------------

videos = []

# ------------------------------------------------------------------------------
# Arquivos disponíveis para download
# ------------------------------------------------------------------------------

downloads = []

# ------------------------------------------------------------------------------
# Cartão de exibição na Home
# ------------------------------------------------------------------------------

home_card = {
    "resumo": "Cardápio digital para a confeitaria da minha esposa: o cliente escolhe sabores, monta o carrinho, paga por PIX com QR Code e envia o pedido pelo WhatsApp.",
    "categoria": "web",
    "tecnologias": ["HTML", "CSS", "JavaScript", "PIX", "WhatsApp"],
    "imagem": "img/doce_prazer_preview.webp",
    "ordem": 4,
}
