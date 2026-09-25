"""
Dados de perfil exibidos na home do portfólio: Sobre, Jornada, Habilidades e
Certificados. Não é um módulo de projeto (sem `posts`/`ficha_tecnica`), por
isso é ignorado explicitamente pela descoberta automática em data/__init__.py.
"""

# ------------------------------------------------------------------------------
# Sobre
# ------------------------------------------------------------------------------

sobre = {
    "texto": (
        "Estudante de Análise e Desenvolvimento de Sistemas em transição de carreira "
        "para a área de TI, com foco em desenvolvimento web full stack. Construo "
        "aplicações reais do início ao deploy — como este próprio portfólio, um "
        "sistema Flask com roteamento dinâmico, PostgreSQL e um blog técnico "
        "individual para cada projeto — e também exploro interfaces gráficas "
        "(Pygame, Tkinter, PySide6, Kivy) e integrações com APIs externas e IA. "
        "Gosto de estruturar código modular, documentar o processo de construção "
        "de cada projeto e aprender fazendo, um projeto de cada vez."
    ),
}

# ------------------------------------------------------------------------------
# Jornada
# ------------------------------------------------------------------------------

jornada = [
    {"ano": "2021", "descricao": "Início dos estudos em programação"},
    {"ano": "2023", "descricao": "Criação dos primeiros projetos pessoais e sistemas para empresas"},
    {"ano": "2024", "descricao": "Entrada na faculdade de Análise e Desenvolvimento de Sistemas"},
    {"ano": "2025", "descricao": "Foco total na transição de carreira e construção de portfólio"},
]

# ------------------------------------------------------------------------------
# Habilidades técnicas
# ------------------------------------------------------------------------------

habilidades = [
    {
        "categoria": "Linguagens e Tecnologias",
        "itens": [
            {"nome": "Python", "icone": "fab fa-python", "cor": "text-primary", "nivel": "Avançado"},
            {"nome": "HTML5", "icone": "fab fa-html5", "cor": "text-danger", "nivel": "Intermediário"},
            {"nome": "CSS3", "icone": "fab fa-css3-alt", "cor": "text-primary", "nivel": "Intermediário"},
            {"nome": "JavaScript", "icone": "fab fa-js-square", "cor": "text-warning", "nivel": "Intermediário"},
            {"nome": "SQL", "icone": "fas fa-code", "cor": "text-light", "nivel": "Intermediário"},
            {"nome": "C++", "icone": "fas fa-code", "cor": "text-primary", "nivel": "Intermediário"},
        ],
    },
    {
        "categoria": "Frameworks & Bibliotecas",
        "itens": [
            {"nome": "FastAPI", "icone": "fas fa-bolt", "cor": "text-info", "nivel": "Intermediário"},
            {"nome": "Bootstrap", "icone": "fab fa-bootstrap", "cor": "text-light", "nivel": "Intermediário"},
            {"nome": "Pygame", "icone": "fas fa-gamepad", "cor": "text-white", "nivel": "Avançado"},
            {"nome": "Tkinter / Kivy / PySide", "icone": "fas fa-window-restore", "cor": "text-success", "nivel": "Intermediário"},
            {"nome": "Django", "icone": "fab fa-python", "cor": "text-warning", "nivel": "Intermediário"},
            {"nome": "Pillow", "icone": "fas fa-image", "cor": "text-danger", "nivel": "Intermediário"},
            {"nome": "Jinja2", "icone": "fas fa-file-code", "cor": "text-secondary", "nivel": "Básico"},
            {"nome": "Flask", "icone": "fas fa-flask", "cor": "text-light", "nivel": "Intermediário"},
        ],
    },
    {
        "categoria": "Banco de Dados",
        "itens": [
            {"nome": "SQLite / MySQL", "icone": "fas fa-database", "cor": "text-success", "nivel": "Intermediário"},
            {"nome": "PostgreSQL", "icone": "fas fa-database", "cor": "text-success", "nivel": "Intermediário"},
        ],
    },
    {
        "categoria": "Ferramentas & Ambientes de Desenvolvimento",
        "itens": [
            {"nome": "Git / GitHub", "icone": "fab fa-github", "cor": "text-light", "nivel": "Avançado"},
            {"nome": "Vercel / Render", "icone": "fas fa-cloud-upload-alt", "cor": "text-info", "nivel": "Intermediário"},
            {"nome": "CLI / Linha de Comando", "icone": "fas fa-terminal", "cor": "text-secondary", "nivel": "Intermediário"},
            {"nome": "bcrypt / Segurança", "icone": "fas fa-shield-alt", "cor": "text-danger", "nivel": "Intermediário"},
            {"nome": "IA + ChatGPT", "icone": "fas fa-robot", "cor": "text-light", "nivel": "Básico"},
            {"nome": "Linux / Vim", "icone": "fab fa-linux", "cor": "text-light", "nivel": "Avançado"},
            {"nome": "VS Code / Visual Studio", "icone": "fas fa-laptop-code", "cor": "text-info", "nivel": "Intermediário"},
            {"nome": "Railway (Deploy)", "icone": "fas fa-rocket", "cor": "text-warning", "nivel": "Intermediário"},
        ],
    },
]

# ------------------------------------------------------------------------------
# Certificados
# ------------------------------------------------------------------------------

certificados = [
    {
        "titulo": "Operador de Computador - Obra Social Dom Bosco",
        "descricao": "Curso profissionalizante de 330h de carga horária.",
        "categoria": "presencial",
        "imagem_thumb": "img/certificados/mt-computador.webp",
        "imagem_full": "img/certificados/op-computador.jpg",
    },
    {
        "titulo": "Montador e Reparador de Computador - Obra Social Dom Bosco",
        "descricao": "Curso profissionalizante de 330h de carga horária.",
        "categoria": "presencial",
        "imagem_thumb": "img/certificados/mt-computador.webp",
        "imagem_full": "img/certificados/mt-computador.jpg",
    },
    {
        "titulo": "Auxiliar Administrativo - Obra Social Dom Bosco",
        "descricao": "Curso profissionalizante de 330h de carga horária.",
        "categoria": "presencial",
        "imagem_thumb": "img/certificados/ass-administrativo.webp",
        "imagem_full": "img/certificados/ass-administrativo.jpg",
    },
    {
        "titulo": "Programador de Sistemas - Obra Social Dom Bosco",
        "descricao": "Curso profissionalizante com 330h de carga horária.",
        "categoria": "online",
        "imagem_thumb": "img/certificados/certificado_python.webp",
        "documento": "docs/certificados/822_luizdererita@gmail.com.pdf",
    },
    {
        "titulo": "Python - Santander OpenAcademy",
        "descricao": "Curso introdutório com 8h de carga horária.",
        "categoria": "online",
        "imagem_thumb": "img/certificados/certificado_python.webp",
        "documento": "docs/certificados/822_luizdererita@gmail.com.pdf",
    },
]
