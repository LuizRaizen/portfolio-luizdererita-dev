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

projeto = "whats-clone" # Exemplo: "meu-projeto-avancado"

# ------------------------------------------------------------------------------
# Ficha Técnica
# ------------------------------------------------------------------------------
# Informações exibidas na seção "Ficha Técnica" da página principal do projeto.
# Os campos podem ser deixados em branco ("") caso não se apliquem.
# ------------------------------------------------------------------------------

ficha_tecnica = {
    "nome": "WhatsClone",
    "linguagem": "Python",
    "framework": "Kivy",
    "paradigma": "Programação Orientada a Objetos (OOP)",
    "arquitetura": "",
    "tipo_projeto": "Um simulador que tenta replicar visualmente a interface do WhatsApp",
    "interface": "Inicialmente projetado para dispositivos móveis",
    "funcionalidades": ["Telas de login, chat, contatos e conversas"],
    "bibliotecas": [],
    "banco_de_dados": "",
    "api_externa": "",
    "plataforma": "Mobile",
    "resolucao": "",
    "status": "Em pausa, com problemas de responsividade em dispositivos recentes"
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
        "titulo": "Replicando o Whatsapp",
        "data": datetime(2025, 6, 12),
        "autor": "Luiz R. Dererita",
        "nome_arquivo": "post1",
        "conteudo": """
        <p>
          O <strong>WhatsClone</strong> foi um experimento que nasceu da minha curiosidade em aprender mais sobre <strong>Kivy</strong>, uma biblioteca Python muito poderosa para a criação de interfaces multiplataforma, principalmente para dispositivos móveis. A ideia era simples, mas ambiciosa: criar um app que visualmente imitasse o WhatsApp, apenas como uma forma de estudo e domínio da criação de interfaces realistas.
        </p>

        <h2 class="section-title mt-4">A Experiência com Kivy</h2>
        <p>
          Eu desenvolvi a primeira versão do projeto utilizando um celular Android e o aplicativo de desenvolvimento <strong>WebCode</strong>, o que por si só já foi um desafio interessante. A experiência de programar direto pelo celular me forçou a entender bem a estrutura do <code>.kv</code> e como posicionar corretamente os elementos visuais.
        </p>
        <p>
          No início, consegui resultados bastante próximos do que eu queria. Consegui reproduzir a tela de login, a tela de chats e até mesmo o layout de mensagens com balões alinhados à esquerda e à direita. Mas com a troca de dispositivo, percebi que a responsividade era um problema: os elementos estavam fora de lugar e perdendo a estética.
        </p>

        <h2 class="section-title mt-4">Motivações</h2>
        <p>
          Eu queria, acima de tudo, testar meus limites. Sempre achei interessante como o WhatsApp é limpo, intuitivo e direto ao ponto — o desafio de replicar essa interface me motivou a estudar mais sobre UI/UX, espaçamento, responsividade, hierarquia visual e, claro, a lógica por trás dos aplicativos de mensagens.
        </p>
        <p>
          O WhatsClone é um projeto de estudo que, embora não tenha sido finalizado, foi extremamente enriquecedor. Ele me fez encarar de frente a complexidade de construir interfaces com múltiplos componentes interativos e me mostrou a importância de pensar em escalabilidade e adaptação desde o início.
        </p>

        <h2 class="section-title mt-4">Reflexão Final</h2>
        <p>
          O projeto está atualmente em pausa, mas pretendo retomá-lo com uma abordagem mais madura. A ideia é revisar todo o código, refatorar com boas práticas e aplicar conceitos que aprendi posteriormente — como a separação entre lógica e apresentação, uso de componentes reutilizáveis, e principalmente, a responsividade.
        </p>
        <p>
          Mesmo que nunca venha a ser uma cópia funcional do WhatsApp, o <strong>WhatsClone</strong> cumpriu seu papel como projeto formador. Hoje olho para ele com carinho, como uma representação de uma fase onde estava explorando e desbravando novas fronteiras com Python.
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
    {"alerta": "Criação da interface da conversa com mensagens enviadas e recebidas"},

    # METAS
    {"status": "concluido", "meta": "Criação do esqueleto do projeto com Kivy"},
    {"status": "desenvolvimento", "meta": "Implementação da tela de login"},
    {"status": "concluido", "meta": "Criação da tela de contatos e lista de chats"},
    {"status": "desenvolvimento", "meta": "Identificação de problemas de responsividade em novos dispositivos"},
    {"status": "desdenvolvimento", "meta": "Refatoração completa da estrutura do layout com foco em responsividade"},
    {"status": "concluido", "meta": "Separação de camadas (UI e lógica)"},
    {"status": "planejado", "meta": "Simulação de sistema de envio/recebimento de mensagens local"},
    {"status": "planejado", "meta": "Adição de suporte a múltiplos temas (modo claro e escuro)"},
]

# ------------------------------------------------------------------------------
# Galeria de imagens
# ------------------------------------------------------------------------------
# Cada imagem deve conter:
# - src: caminho relativo à pasta static/
# - descricao: legenda exibida ao lado da imagem
# ------------------------------------------------------------------------------

imagens = [
    {"src": "img/whats-clone/print.png", "descricao": "Testando o WhatsClone no Desktop"}
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
