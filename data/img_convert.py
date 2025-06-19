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

projeto = "img-convert" # Exemplo: "meu-projeto-avancado"

# ------------------------------------------------------------------------------
# Ficha Técnica
# ------------------------------------------------------------------------------
# Informações exibidas na seção "Ficha Técnica" da página principal do projeto.
# Os campos podem ser deixados em branco ("") caso não se apliquem.
# ------------------------------------------------------------------------------


ficha_tecnica = {
    "nome": "IMG Convert",
    "linguagem": "Python",
    "framework": "PySide6",
    "paradigma": "Programação Orientada a Objetos (OOP)",
    "arquitetura": "Modular, com foco em escalabilidade",
    "tipo_projeto": "rede social onde os usuários se conectam por meio de <strong>temas, ideias e interesses compartilhados</strong>, organizando conversas por fluxos de pensamento",
    "interface": "UI moderna com botões estilizados e foco em usabilidade",
    "funcionalidades": ["Suporte a formatos comuns como PNG, JPG, BMP, WEBP, entre outros"],
    "bibliotecas": ["Biblioteca Pillow (PIL)", "os"],
    "banco_de_dados": "",
    "api_externa": "",
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
        "titulo": "Manipulaçao de Imagens com Python",
        "data": datetime(2025, 6, 12),
        "autor": "Luiz R. Dererita",
        "nome_arquivo": "post1",
        "conteudo": """
        O <strong>IMG Convert</strong> foi um projeto curioso. Ele nasceu durante uma fase muito especial da minha jornada com a programação, quando eu estava aprendendo Python com entusiasmo e descobrindo um universo totalmente novo. Era como se cada nova biblioteca que eu conhecia abrisse uma nova janela para possibilidades que eu nem imaginava antes.
        </p>
        <p>
        Eu me encontrava em uma fase intensa de experimentação. Testava scripts, automatizava coisas simples, e cada pequena vitória me dava vontade de explorar mais. Foi nesse contexto que descobri a biblioteca <code>PIL</code> (Python Imaging Library), que permite manipular imagens com Python. Aquilo me fascinou! De repente, eu podia redimensionar, converter, rotacionar e até transformar imagens programaticamente.
        </p>

        <h2 class="section-title mt-4">A Primeira Versão</h2>
        <p>
        A primeira versão do IMG Convert surgiu como um simples módulo de linha de comando. Eu queria algo rápido e objetivo para converter imagens entre formatos diferentes sem precisar abrir um editor. Era algo só meu, para uso pessoal. Mas como eu também estava começando a estudar interfaces gráficas com <code>Tkinter</code>, tive a ideia de transformar aquele módulo em um pequeno aplicativo.
        </p>
        <p>
        Com a interface feita em Tkinter, o usuário podia escolher uma imagem (ou uma pasta com várias), definir o diretório de saída e o formato desejado. Simples, direto ao ponto — mas já me deixava orgulhoso. Aquilo representava meu primeiro passo na criação de softwares com interface real.
        </p>

        <h2 class="section-title mt-4">Evoluindo com o PySide</h2>
        <p>
        Depois de algum tempo, descobri o <strong>PySide</strong>, um framework baseado no Qt que permite criar aplicações com aparência moderna e nativa para Desktop. Foi amor à primeira vista. Era tudo que eu procurava para dar um toque mais profissional às minhas criações.
        </p>
        <p>
        Decidi então reformular a interface do IMG Convert usando PySide6. Mantive a simplicidade do funcionamento, mas dei um salto na experiência do usuário. Agora, com design escuro, botões bem posicionados e responsividade adequada, o programa ficou mais robusto, intuitivo e visualmente agradável.
        </p>
        <p>
        Também reorganizei o código em módulos, implementei controles de validação e deixei o projeto mais preparado para receber funcionalidades futuras — como redimensionamento em lote, marca d'água e filtros.
        </p>

        <h2 class="section-title mt-4">Aprendizados Técnicos</h2>
        <ul>
        <li>Manipulação de imagens com <strong>PIL / Pillow</strong>: conversão, redimensionamento, detecção de formato.</li>
        <li>Criação de interfaces com <strong>Tkinter</strong> e depois <strong>PySide6</strong>, entendendo a diferença entre UIs básicas e modernas.</li>
        <li>Tratamento de múltiplos arquivos, gerenciamento de diretórios e extensões.</li>
        <li>Organização de código em módulos reutilizáveis, boas práticas e manutenção futura.</li>
        <li>Criação de aplicações Desktop que funcionam sem dependência de navegadores ou servidores.</li>
        </ul>

        <h2 class="section-title mt-4">Reflexão Pessoal</h2>
        <p>
        Para mim, o <strong>IMG Convert</strong> representa uma fase de descobertas, onde tudo era novo, empolgante e desafiador. Ele carrega a essência de quem está começando, mas já se sente movido por uma paixão real: <strong>criar ferramentas úteis com tecnologia</strong>.
        </p>
        <p>
        Python sempre terá um espaço especial na minha trajetória. Foi com ele que eu aprendi o que era lógica, o que era modularização, como pensar como desenvolvedor. O IMG Convert é fruto direto dessa relação — e mesmo hoje, com mais experiência, ainda tenho carinho imenso por esse pequeno projeto. Ele foi um passo importante na minha caminhada como programador.
        </p>
        <p>
        Espero que, de alguma forma, esse projeto também inspire outras pessoas que estão começando, mostrando que não é preciso algo gigante para criar algo útil, funcional e feito com dedicação.
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
    {"status": "concluido", "meta": "Criação do módulo base para conversão de imagens usando a biblioteca PIL"},
    {"status": "concluido", "meta": "Implementação da versão CLI (linha de comando) para uso rápido e direto"},
    {"status": "concluido", "meta": "Desenvolvimento de uma interface simples com Tkinter"},
    {"status": "concluido", "meta": "Planejamento para manter a UI Tkinter como parte alternativa “histórica” do projeto"},
    {"status": "concluido", "meta": "Modelagem das novas telas com Qt Designer"},
    {"status": "concluido", "meta": "Tela principal com navegação fluida entre módulos"},
    {"status": "concluido", "meta": "Tela de seleção de imagem individual"},
    {"status": "concluido", "meta": "Tela de seleção de pasta e diretório de saída"},
    {"status": "concluido", "meta": "Tela de conversão com barra de progresso animada"},
    {"status": "desenvolvimento", "meta": "Integração do backend de conversão com as telas do PySide6"},
    {"status": "planejado", "meta": "Suporte para múltiplos formatos (PNG, JPG, BMP, WEBP...)"},
    {"status": "planejado", "meta": "Conversão em lote de imagens em pastas inteiras"},
    {"status": "planejado", "meta": "Mensagens de status e feedbacks visuais ao usuário"},
    {"status": "planejado", "meta": "Melhoria na experiência do usuário (UX/UI)"},
    {"status": "planejado", "meta": "Criação de ícone do app e splash screen inicial"},
    {"status": "planejado", "meta": "Geração de executável com PyInstaller"},
]

# ------------------------------------------------------------------------------
# Galeria de imagens
# ------------------------------------------------------------------------------
# Cada imagem deve conter:
# - src: caminho relativo à pasta static/
# - descricao: legenda exibida ao lado da imagem
# ------------------------------------------------------------------------------

imagens = [
    {"src": "img/img-convert/print.png", "descricao": "Tela principal do IMG Convert"},
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
