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

projeto = "crud-cadastro-empresas"  # Exemplo: "meu-projeto-avancado"

# ------------------------------------------------------------------------------
# Ficha Técnica
# ------------------------------------------------------------------------------
# Informações exibidas na seção "Ficha Técnica" da página principal do projeto.
# Os campos podem ser deixados em branco ("") caso não se apliquem.
# ------------------------------------------------------------------------------

ficha_tecnica = {
    "nome": "CRUD de Cadastro de Empresas",
    "linguagem": "Python",
    "framework": "PySide6",
    "paradigma": "Programação Orientada a Objetos (OOP)",
    "arquitetura": "Modular, com separação entre UI, lógica e integração de API",
    "tipo_projeto": "Um CRUD para cadastrar e consultar empresas através da API da Receita Federal",
    "interface": "UI de desktop com múltiplas janelas estilizadas e campos interativos",
    "funcionalidades": [
        "Cadastro e consulta",
        "Cautomática de CNPJ",
        "Edição e exclusão de empresas"
    ],
    "bibliotecas": [],
    "banco_de_dados": "SQLite (armazenamento local das empresas cadastradas)",
    "api_externa": "ReceitaWS (consulta pública de CNPJ via API)",
    "plataforma": "Desktop (Windows / Linux)",
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
        "titulo": 'Nada se Cria, Tudo se Copia',
        "data": datetime(2025, 6, 14),
        "autor": "Luiz R. Dererita",
        "nome_arquivo": "post1",
        "conteudo": """
        <p>
          Este projeto é, talvez, um dos mais genéricos e diretos que já comecei — mas isso não é um problema. Na verdade, foi justamente o objetivo. O CRUD para cadastro de empresas foi criado seguindo o passo a passo de uma <strong>série de aulas do canal Pytax no YouTube</strong>. Eu queria me aprofundar mais em <strong>interfaces com PySide6</strong> e também <strong>praticar integração com APIs reais</strong>.
        </p>

        <h3 class="section-title mt-4">Aprendizado Prático com PySide6</h3>
        <p>
          O projeto é um <strong>aplicativo desktop em Python</strong>, com foco em cadastro, listagem, edição e exclusão de empresas. Toda a interface foi construída com <strong>PySide6</strong>, o que me permitiu explorar de forma prática a criação de janelas, campos de entrada, botões estilizados e até mesmo comunicação entre formulários e tabelas de dados.
        </p>
        <p>
          Ainda estou usando o <strong>logo original do canal Pytax</strong> como placeholder, já que a estética ainda está em fase inicial. Porém, minha intenção é justamente usar essa base funcional para desenvolver uma <strong>nova identidade visual</strong>, mais alinhada ao meu estilo e com melhorias na usabilidade.
        </p>

        <h3 class="section-title mt-4">Integração com a Receita Federal</h3>
        <p>
          Uma das funcionalidades mais legais deste projeto é a <strong>consulta automática de dados de empresas através da API da Receita Federal</strong>. Com apenas o CNPJ, o sistema já preenche várias informações como razão social, nome fantasia, endereço e situação cadastral. Isso torna o sistema muito mais prático, rápido e preciso para o usuário.
        </p>
        <p>
          Esse tipo de integração me fez refletir sobre o quanto APIs públicas podem transformar sistemas simples em ferramentas realmente úteis e profissionais.
        </p>

        <h3 class="section-title mt-4">O Que Eu Pretendo Melhorar</h3>
        <p>
          O sistema ainda não está funcional, comecei apenas a interface. Mesmo assim, ainda há muito espaço para melhorias. Não pretendo seguir a risca o projeto estudado. Quero refatorar parte do código para torná-lo mais modular, repensar a identidade visual do app, adicionar uma opção de exportação em PDF ou CSV e talvez até implementar um <strong>sistema de permissões por usuário</strong> em uma versão futura.
        </p>
        <p>
          Também pretendo fazer uma <strong>validação mais robusta de dados</strong> e melhorar o tratamento de exceções, especialmente nas consultas da API (em caso de falhas de conexão ou CNPJ inválido).
        </p>

        <h3 class="section-title mt-4">Reflexão Final</h3>
        <p>
          Mesmo sendo um projeto simples e baseado em tutoriais, este CRUD de empresas me ensinou muita coisa na prática. Aprendi mais sobre a arquitetura de aplicações desktop com PySide6, entendi melhor como lidar com APIs reais e comecei a pensar em como transformar um sistema didático em um produto com cara profissional.
        </p>
        <p>
          É o tipo de projeto que me faz olhar para trás e perceber o quanto evoluí. Ainda que o ponto de partida tenha sido um vídeo no YouTube, o destino pode ser algo muito mais autoral — e é exatamente esse o plano.
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
    {"alerta": "Este projeto está em fase de desenvolvimento"},

    # METAS
    {"status": "concluido", "meta": "Base do CRUD criada com PySide6 seguindo o tutorial do canal Pytax"},
    {"status": "desenvolvimento", "meta": "Sistema de banco de dados SQLite funcional para armazenar cadastros"},
    {"status": "planejado", "meta": "Integração com API da Receita Federal (ReceitaWS) para consulta automática por CNPJ"},
    {"status": "planejado", "meta": "Base do CRUD criada com PySide6 seguindo o tutorial do canal Pytax"},
    {"status": "planejado", "meta": "Aprimoramento da interface visual com identidade própria"},
    {"status": "planejado", "meta": "Implementação de tela inicial personalizada com branding do projeto"},
    {"status": "planejado", "meta": "Inclusão de modo escuro e responsividade básica para diferentes resoluções"},
    {"status": "planejado", "meta": "Validação de CNPJ com feedback ao usuário"},
    {"status": "planejado", "meta": "Implementação de sistema de filtros e ordenação dos dados cadastrados"},
    {"status": "planejado", "meta": "Exportação de registros em CSV ou PDF"},
    {"status": "planejado", "meta": "Refatoração do código para maior separação entre UI e lógica de negócios"},
    {"status": "planejado", "meta": "Documentação interna e externa (README e comentários)"},
    {"status": "planejado", "meta": "Criação de instalador para Windows e Linux"},
    {"status": "planejado", "meta": "Versão executável standalone com empacotamento via PyInstaller ou semelhante"},
]

# ------------------------------------------------------------------------------
# Galeria de imagens
# ------------------------------------------------------------------------------
# Cada imagem deve conter:
# - src: caminho relativo à pasta static/
# - descricao: legenda exibida ao lado da imagem
# ------------------------------------------------------------------------------

imagens = [
    {"src": "img/crud-cadastro-empresas/print.png", "descricao": "Tela principal do CRUD de Cadastro de Empresas"}
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
