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

projeto = "ferramenta-pesquisa-ia"  # Exemplo: "meu-projeto-avancado"

# ------------------------------------------------------------------------------
# Ficha Técnica
# ------------------------------------------------------------------------------
# Informações exibidas na seção "Ficha Técnica" da página principal do projeto.
# Os campos podem ser deixados em branco ("") caso não se apliquem.
# ------------------------------------------------------------------------------

ficha_tecnica = {
    "nome": "Ferramenta de Pesquisa com IA",
    "linguagem": "Python, Javascript, HTML5, CSS3",
    "framework": "Boostrap 5, FastAPI",
    "paradigma": "Programação Orientada a Objetos (OOP)",
    "arquitetura": "",
    "tipo_projeto": "Questionário web com perguntas sobre saúde e instruções para melhora na qualidade de vida",
    "interface": "Interface Web responsiva e adaptável a Desktop e Mobile",
    "funcionalidades": [
        "Geração de dicas personalizadas de saúde e bem-estar com base nas respostas do usuário",
        "Texto gerado com recomendações práticas exibidas na tela e enviado por e-mail"
    ],
    "bibliotecas": ["pygame", "os", "random"],
    "banco_de_dados": "",
    "api_externa": [
        "API da OpenAI para geração de texto com IA",
        "Integração com <code>smtplib</code> para envio por e-mail do resultado"
    ],
    "plataforma": "Web (acesso via QR Code em dispositivos móveis)",
    "resolucao": "",
    "status": "Finalizado e aplicado com sucesso"
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
        "titulo": "Projeto de Extensão Universitária",
        "data": datetime(2025, 6, 12),
        "autor": "Luiz R. Dererita",
        "nome_arquivo": "post1",
        "conteudo": """
        <p>
          Este projeto foi desenvolvido como parte da minha <strong>Atividade de Extensão Universitária</strong> na <strong>Universidade Cruzeiro do Sul</strong>, onde atualmente curso Análise e Desenvolvimento de Sistemas (ADS). A proposta era realizar uma intervenção social relevante, e decidi unir <strong>tecnologia, saúde e inteligência artificial</strong> em um único sistema.
        </p>

        <h3 class="section-title mt-4">A Proposta</h3>
        <p>
          O projeto consistiu na criação de um <strong>aplicativo web</strong> que funcionava como um <strong>questionário de pesquisa sobre saúde e bem-estar</strong>. Ao final do preenchimento, os participantes recebiam um texto com <strong>dicas personalizadas</strong> com base em suas respostas. Essa mensagem era gerada automaticamente por uma <strong>IA conectada à API da OpenAI</strong>, oferecendo recomendações práticas de saúde, como alimentação, sono, exercícios físicos e controle emocional.
        </p>

        <h3 class="section-title mt-4">Como Funciona</h3>
        <ul>
          <li>O participante acessava um formulário digital via <strong>QR Code</strong>, impresso e plastificado como um crachá que eu mesmo usava.</li>
          <li>Após o preenchimento do questionário, os dados eram processados por um <strong>servidor em FastAPI</strong> com integração à <strong>API da OpenAI</strong>.</li>
          <li>O texto com dicas de saúde era gerado automaticamente e exibido na tela.</li>
          <li>Esse mesmo texto era também enviado para o <strong>e-mail do participante</strong>, possibilitando consulta futura.</li>
        </ul>

        <h3 class="section-title mt-4">Execução em Campo</h3>
        <p>
          A aplicação da pesquisa aconteceu presencialmente, em uma praça na região de <strong>Itaquera, São Paulo</strong>. Durante um fim de semana, abordei cerca de <strong>60 pessoas</strong>. Dessas, <strong>50 toparam responder</strong> o questionário e aproximadamente <strong>30 apresentaram respostas sérias e interessadas</strong> nas recomendações geradas pela IA.
        </p>
        <p>
          Foi uma experiência enriquecedora: além de desenvolver o sistema completo, tive que lidar com <strong>interação social, organização de dados, suporte técnico no local e validação prática</strong> do que estava propondo.
        </p>

        <h3 class="section-title mt-4">Aprendizados Técnicos</h3>
        <ul>
          <li>Uso da <strong>API da OpenAI</strong> para geração automática de conteúdo com base em respostas humanas.</li>
          <li>Criação de <strong>formulários web</strong> responsivos e intuitivos com HTML, CSS e Bootstrap.</li>
          <li>Implementação de backend com <strong>Python + FastAPI</strong>, tratamento de dados e integração com bibliotecas como <code>smtplib</code> para envio de e-mails.</li>
          <li>Gerenciamento de variáveis de ambiente com segurança (chaves da API e credenciais de e-mail).</li>
        </ul>

        <h3 class="section-title mt-4">Impacto Social</h3>
        <p>
          Este projeto uniu tecnologia e intervenção social. A proposta foi além do desenvolvimento técnico: tratou-se de criar uma ponte entre conhecimento acadêmico e benefício direto à comunidade. Muitos participantes demonstraram surpresa e entusiasmo ao receberem as recomendações personalizadas, e alguns me disseram que iriam seguir as dicas em seu cotidiano.
        </p>

        <h3 class="section-title mt-4">Reflexão Final</h3>
        <p>
          A <strong>Pesquisa-intervenção de Saúde e Bem-Estar</strong> foi uma das experiências mais completas que já tive como estudante. Pude desenvolver um sistema funcional, aplicar pessoalmente, interagir com a comunidade, promover a saúde e exercitar minhas habilidades de programação, design e comunicação. É um projeto que me orgulha profundamente e representa bem minha intenção de utilizar a tecnologia como ferramenta de transformação positiva.
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
    {"status": "concluido", "meta": "Definição do tema e metodologia da pesquisa de extensão universitária"},
    {"status": "concluido", "meta": "Criação do questionário com foco em saúde e bem-estar"},
    {"status": "concluido", "meta": "Integração com API da OpenAI para geração de recomendações personalizadas"},
    {"status": "concluido", "meta": "Implementação do backend com FastAPI para receber e processar os dados"},
    {"status": "concluido", "meta": "Envio automatizado das respostas por e-mail para os participantes"},
    {"status": "concluido", "meta": "Preparação de crachá com QR Code para acesso rápido ao sistema"},
    {"status": "concluido", "meta": "Aplicação presencial da pesquisa em praça pública"},
    {"status": "concluido", "meta": "Coleta de respostas e interação com cerca de 60 pessoas"},
]

# ------------------------------------------------------------------------------
# Galeria de imagens
# ------------------------------------------------------------------------------
# Cada imagem deve conter:
# - src: caminho relativo à pasta static/
# - descricao: legenda exibida ao lado da imagem
# ------------------------------------------------------------------------------

imagens = [
    {"src": "img/ferramenta-pesquisa-ia/pesquisa_1.jpeg", "descricao": "Gameplay da primeira fase"},
    {"src": "img/ferramenta-pesquisa-ia/pesquisa_2.JPG", "descricao": "Gameplay da primeira fase"},
    {"src": "img/ferramenta-pesquisa-ia/pesquisa_3.JPG", "descricao": "Gameplay da primeira fase"},
    {"src": "img/ferramenta-pesquisa-ia/pesquisa_4.jpeg", "descricao": "Gameplay da primeira fase"},
    {"src": "img/ferramenta-pesquisa-ia/print_1.jpeg", "descricao": "Gameplay da primeira fase"},
    {"src": "img/ferramenta-pesquisa-ia/print_2.jpeg", "descricao": "Gameplay da primeira fase"},
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
