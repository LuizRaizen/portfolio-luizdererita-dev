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

projeto = "zappi"  # Exemplo: "meu-projeto-avancado"

# ------------------------------------------------------------------------------
# Ficha Técnica
# ------------------------------------------------------------------------------
# Informações exibidas na seção "Ficha Técnica" da página principal do projeto.
# Os campos podem ser deixados em branco ("") caso não se apliquem.
# ------------------------------------------------------------------------------

ficha_tecnica = {
    "nome": "Zappi",
    "linguagem": "Python",
    "framework": "Django",
    "paradigma": "Programação Orientada a Objetos (OOP)",
    "arquitetura": "MVC com escalabilidade modular para múltiplas instâncias",
    "tipo_projeto": "Sistema de E-commerce escalável para SaaS de criação de lojas virtuais",
    "interface": "Frontend responsivo e personalizável com HTML, CSS, JavaScript e Tailwind",
    "funcionalidades": [
        "Criação e gerenciamento de e-commerces",
        "Painel administrativo para lojistas",
        "Catálogo de produtos com imagens e categorias",
        "Carrinho de compras, checkout e pedidos",
        "Sistema de planos e personalização por assinatura"
    ],
    "bibliotecas": ["Django", "Gunicorn", "TailwindCSS", "WeasyPrint", "JavaScript Vanilla"],
    "banco_de_dados": "PostgreSQL",
    "api_externa": "Integrações planejadas com gateways de pagamento e serviços de envio",
    "plataforma": "Web",
    "resolucao": "Responsivo (desktop, tablet e mobile)",
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
        "titulo": 'Zappi: O Início de um E-commerce Inteligente e Escalável',
        "data": datetime(2025, 8, 4),
        "autor": "Luiz R. Dererita",
        "nome_arquivo": "lancamento-zappi",
        "conteudo": """
        <p>
          Zappi é mais do que um sistema de e-commerce: é uma plataforma pensada desde o início para evoluir 
          para um modelo SaaS completo, onde qualquer pessoa poderá criar sua própria loja virtual com total 
          liberdade de personalização.
        </p>

        <h3 class="section-title mt-4">Do E-commerce Tradicional ao SaaS de Lojas</h3>
        <p>
          A proposta inicial do Zappi é funcionar como um sistema robusto de e-commerce com todas as funções 
          essenciais: catálogo, carrinho, pedidos, gerenciamento de usuários e painel administrativo. Mas seu 
          diferencial está na arquitetura escalável que permitirá que ele se torne um verdadeiro <strong>construtor 
          de e-commerces por assinatura</strong>.
        </p>

        <h3 class="section-title mt-4">Personalização no Centro de Tudo</h3>
        <p>
          O grande foco do Zappi é oferecer uma experiência visualmente livre para o lojista: será possível 
          escolher layouts, cores, banners e elementos gráficos únicos, tudo sem sair da plataforma. Com isso, 
          cada loja criada será realmente única.
        </p>

        <h3 class="section-title mt-4">Próximos Passos</h3>
        <p>
          No momento, o projeto está em desenvolvimento, com foco na primeira versão funcional do sistema base 
          de e-commerce. Em seguida, será implementado o módulo de criação de lojas dinâmicas e os planos 
          escalonados.
        </p>

        <p class="meta-info">Postado em <strong>4 de Agosto de 2025</strong> por <strong>Luiz R. Dererita</strong></p>
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
    {"alerta": "O Zappi está em fase ativa de desenvolvimento e expansão para SaaS"},
    {"status": "concluido", "meta": "Arquitetura inicial do sistema de e-commerce com Django"},
    {"status": "concluido", "meta": "Modelos base de produtos, usuários e pedidos"},
    {"status": "desenvolvimento", "meta": "Painel administrativo para lojistas"},
    {"status": "desenvolvimento", "meta": "Sistema de personalização visual de lojas"},
    {"status": "desenvolvimento", "meta": "Módulo de planos e assinatura mensal"},
    {"status": "planejado", "meta": "Editor visual de temas e layouts para lojas"},
    {"status": "planejado", "meta": "Exportação automática de relatórios e dados em PDF"},
    {"status": "planejado", "meta": "Integração com métodos de pagamento (ex: Stripe, Pix, MercadoPago)"},
    {"status": "planejado", "meta": "Sistema de templates prontos para novos lojistas"},
    {"status": "planejado", "meta": "Hospedagem e subdomínio automático para cada loja criada"},
    {"status": "planejado", "meta": "Versão mobile progressiva (PWA)"},
    {"status": "planejado", "meta": "Painel de métricas e insights de vendas para lojistas"}
]

# ------------------------------------------------------------------------------
# Galeria de imagens
# ------------------------------------------------------------------------------
# Cada imagem deve conter:
# - src: caminho relativo à pasta static/
# - descricao: legenda exibida ao lado da imagem
# ------------------------------------------------------------------------------

imagens = [
    {"src": "img/zappi/preview-home.png", "descricao": "Layout inicial da homepage do Zappi"},
    {"src": "img/zappi/preview-login.png", "descricao": "Página de login"},
    {"src": "img/zappi/preview-product.png", "descricao": "Detalhe do Produto (em desenvolvimento)"},
    {"src": "img/zappi/preview-account.png", "descricao": "Painel da conta do cliente"},
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
        "youtube_id": "Ok-Zc7fdU20",
        "descricao": "Breve demonstração do sistema",
    },
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
