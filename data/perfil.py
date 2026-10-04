"""
Dados de perfil exibidos na home do portfólio: Sobre, Jornada, Habilidades e
Certificados. Não é um módulo de projeto (sem `posts`/`ficha_tecnica`), por
isso é ignorado explicitamente pela descoberta automática em data/__init__.py.
"""

from datetime import datetime

# ------------------------------------------------------------------------------
# Sobre
# ------------------------------------------------------------------------------

sobre = {
    "texto": (
        "Sou Luiz, desenvolvedor de software com Python como base, atuando na construção "
        "de aplicações web, APIs, ferramentas desktop, jogos e soluções com IA. Trabalho "
        "com Django, Flask, JavaScript, PostgreSQL, Redis, PySide6 e Pygame, sempre buscando "
        "combinar código limpo, arquitetura modular e soluções adequadas a cada problema. "
        "Em 2026 ampliei meu escopo para dados e IA aplicada: análise e tratamento de dados "
        "com Python, SQL e ETL, IA generativa e engenharia de prompt, além de fundamentos de "
        "cibersegurança e DevSecOps. O principal marco é o Bootcamp Bradesco GenAI, Dados & "
        "Cyber (52h), que incluiu um projeto final de IA e cibersegurança para assistentes "
        "virtuais no mercado financeiro. Na reta final de ADS, sigo aprofundando engenharia "
        "de software e arquitetura de sistemas, transformando ideias em projetos funcionais "
        "e preparados para evoluir."
    ),
    "stats": [
        {"numero": "2026", "legenda": "reta final da faculdade de ADS"},
        {"numero": "Python", "legenda": "minha stack principal"},
        {"numero": "", "legenda": ""},  # preenchido ao fim do arquivo, a partir dos certificados
    ],
}

# ------------------------------------------------------------------------------
# Jornada
# ------------------------------------------------------------------------------

jornada = [
    {"ano": "2021", "descricao": "Início dos estudos em programação"},
    {"ano": "2023", "descricao": "Criação dos primeiros projetos pessoais e sistemas para empresas"},
    {"ano": "2024", "descricao": "Entrada na faculdade de Análise e Desenvolvimento de Sistemas e primeiro curso de Python certificado (Santander Open Academy)"},
    {"ano": "2025", "descricao": "Foco total na transição de carreira e construção de portfólio"},
    {"ano": "2026", "descricao": "Reta final da faculdade e trilha intensiva de estudos: Python avançando para dados, SQL e ETL, IA generativa, engenharia de prompt e cibersegurança, culminando no Bootcamp Bradesco GenAI, Dados & Cyber (52h) — evoluindo o portfólio sem parar"},
]

# ------------------------------------------------------------------------------
# Habilidades técnicas
# ------------------------------------------------------------------------------

habilidades = [
    {
        "categoria": "Fundamentos & Arquitetura",
        "itens": [
            {"nome": "Programação Orientada a Objetos", "icone": "fas fa-shapes", "nivel": "Avançado"},
            {"nome": "Padrões de Projeto (State, MVC)", "icone": "fas fa-diagram-project", "nivel": "Avançado"},
            {"nome": "Programação Modular", "icone": "fas fa-puzzle-piece", "nivel": "Avançado"},
            {"nome": "Estruturas de Dados & Algoritmos", "icone": "fas fa-sitemap", "nivel": "Intermediário"},
            {"nome": "Arquitetura de Software", "icone": "fas fa-layer-group", "nivel": "Intermediário"},
        ],
    },
    {
        "categoria": "Desenvolvimento Web",
        "itens": [
            {"nome": "Desenvolvimento Full Stack", "icone": "fas fa-globe", "nivel": "Avançado"},
            {"nome": "APIs REST & Integrações", "icone": "fas fa-plug", "nivel": "Intermediário"},
            {"nome": "Autenticação & Segurança", "icone": "fas fa-shield-halved", "nivel": "Intermediário"},
            {"nome": "Integração com IA (LLMs)", "icone": "fas fa-robot", "nivel": "Intermediário"},
            {"nome": "Design Responsivo & UI", "icone": "fas fa-mobile-screen", "nivel": "Intermediário"},
        ],
    },
    {
        "categoria": "Dados & Infraestrutura",
        "itens": [
            {"nome": "Modelagem de Bancos de Dados", "icone": "fas fa-database", "nivel": "Avançado"},
            {"nome": "Versionamento de Código", "icone": "fas fa-code-branch", "nivel": "Avançado"},
            {"nome": "Processamento Assíncrono (filas, cache)", "icone": "fas fa-arrows-rotate", "nivel": "Intermediário"},
            {"nome": "Deploy & Integração Contínua", "icone": "fas fa-cloud-arrow-up", "nivel": "Intermediário"},
            {"nome": "Automação de Tarefas", "icone": "fas fa-gears", "nivel": "Intermediário"},
        ],
    },
    {
        "categoria": "Dados, IA & Segurança",
        "itens": [
            {"nome": "Análise e Limpeza de Dados com Python", "icone": "fas fa-chart-column", "nivel": "Intermediário"},
            {"nome": "SQL, ETL e Business Intelligence", "icone": "fas fa-table", "nivel": "Fundamentos"},
            {"nome": "IA Generativa & Engenharia de Prompt", "icone": "fas fa-wand-magic-sparkles", "nivel": "Intermediário"},
            {"nome": "Cibersegurança Aplicada", "icone": "fas fa-user-shield", "nivel": "Fundamentos"},
            {"nome": "DevSecOps, Sistemas Operacionais & VMs", "icone": "fas fa-server", "nivel": "Fundamentos"},
        ],
    },
    {
        "categoria": "Jogos & Interfaces",
        "itens": [
            {"nome": "Lógica de Jogos & Física 2D", "icone": "fas fa-gamepad", "nivel": "Avançado"},
            {"nome": "Boas Práticas & Clean Code", "icone": "fas fa-broom", "nivel": "Avançado"},
            {"nome": "Interfaces Gráficas Desktop", "icone": "fas fa-window-restore", "nivel": "Intermediário"},
            {"nome": "Prototipação de UI/UX", "icone": "fas fa-pen-ruler", "nivel": "Intermediário"},
            {"nome": "Depuração & Testes", "icone": "fas fa-bug", "nivel": "Intermediário"},
        ],
    },
]

# ------------------------------------------------------------------------------
# Certificados
# ------------------------------------------------------------------------------
# Campos (todos opcionais, exceto titulo e categoria; a home e /certificados se
# adaptam ao que existir):
#   instituicao, carga_horaria ("330h"), tipo ("curso", "módulo", "projeto",
#   "mentoria", "bootcamp"), tema (agrupa e filtra), destaque (True: card grande
#   na home), data (datetime: ordena, mostra o mês e alimenta o carrossel de
#   novidades), documento (PDF em static/), imagem_preview / imagem_thumb /
#   imagem_full (static/img/certificados; gere com tools/extrair_certificados.py).
# Sem documento nem imagem o certificado aparece, mas sem link de verificação.
# ------------------------------------------------------------------------------

TEMAS_CERTIFICADOS = ["Python", "Dados & SQL", "IA", "Cibersegurança", "DevOps & Infra", "Carreira", "Formação profissional", "Outros"]


def _certificado_pdf(arquivo, titulo, instituicao, data, horas, tema, tipo="curso", **extra):
    """Certificado cujo PDF está em static/docs/certificados/<arquivo>.pdf e cujas
    imagens foram geradas por tools/extrair_certificados.py (nomes em minúsculas)."""
    base = f"img/certificados/{arquivo.lower()}"
    return {
        "titulo": titulo,
        "instituicao": instituicao,
        "carga_horaria": f"{horas}h",
        "tipo": tipo,
        "tema": tema,
        "data": data,
        "categoria": "online",
        "imagem_preview": f"{base}.webp",
        "imagem_thumb": f"{base}-thumb.webp",
        "documento": f"docs/certificados/{arquivo}.pdf",
        **extra,
    }


def _dio(arquivo, titulo, tipo, data, horas, tema, **extra):
    inst = "DIO · Bradesco" if "Bradesco" in titulo else "DIO"
    return _certificado_pdf(arquivo, titulo, inst, data, horas, tema, tipo, **extra)


certificados = [
    # --- Em destaque (cards grandes na home) --------------------------------
    {
        "titulo": "Programador de Sistemas",
        "instituicao": "Obra Social Dom Bosco",
        "carga_horaria": "330h",
        "tipo": "curso",
        "tema": "Formação profissional",
        "categoria": "presencial",
        "destaque": True,
        "descricao": "Curso profissionalizante com 330h de carga horária.",
        # TODO: adicionar o PDF/imagem deste certificado (hoje não há arquivo).
    },
    _dio("TETGNXX0", "Bootcamp Bradesco - GenAI, Dados & Cyber", "bootcamp", datetime(2026, 9, 27), 52, "IA",
         destaque=True, descricao="Bootcamp de IA generativa, dados e cibersegurança, com projeto final aplicado ao mercado financeiro."),
    _certificado_pdf("certificado-LUIZ-RICARDO-Fundamentos-compactado", "Python Impressionador: Fundamentos", "Hashtag Treinamentos",
                     datetime(2026, 7, 21), 13, "Python", destaque=True,
                     descricao="Nível Fundamentos: variáveis, condições, laços, strings, listas, tuplas e dicionários, com projeto prático."),
    {
        "titulo": "Python",
        "instituicao": "Santander Open Academy",
        "carga_horaria": "8h",
        "tipo": "curso",
        "tema": "Python",
        "data": datetime(2024, 10, 20),  # conforme o próprio certificado
        "categoria": "online",
        "destaque": True,
        "descricao": "Curso introdutório de Python: 2 módulos com autoavaliação.",
        "imagem_preview": "img/certificados/santander-python.webp",
        "imagem_thumb": "img/certificados/santander-python-thumb.webp",
        "documento": "docs/certificados/822_luizdererita@gmail.com.pdf",
    },

    # --- Formação profissional presencial --------------------------------------
    {
        "titulo": "Operador de Computador",
        "instituicao": "Obra Social Dom Bosco",
        "carga_horaria": "330h",
        "tipo": "curso",
        "tema": "Formação profissional",
        "categoria": "presencial",
        "imagem_thumb": "img/certificados/op-computador-thumb.webp",
        "imagem_full": "img/certificados/op-computador.jpg",
    },
    {
        "titulo": "Montador e Reparador de Computador",
        "instituicao": "Obra Social Dom Bosco",
        "carga_horaria": "330h",
        "tipo": "curso",
        "tema": "Formação profissional",
        "categoria": "presencial",
        "imagem_thumb": "img/certificados/mt-computador-thumb.webp",
        "imagem_full": "img/certificados/mt-computador.jpg",
    },
    {
        "titulo": "Auxiliar Administrativo",
        "instituicao": "Obra Social Dom Bosco",
        "carga_horaria": "330h",
        "tipo": "curso",
        "tema": "Formação profissional",
        "categoria": "presencial",
        "imagem_thumb": "img/certificados/ass-administrativo-thumb.webp",
        "imagem_full": "img/certificados/ass-administrativo.jpg",
    },

    # --- Outros ----------------------------------------------------------------
    _certificado_pdf("certificado", "Felicidade e Qualidade de Vida (Mês da Felicidade)", "Cruzeiro do Sul Educacional",
                     datetime(2026, 6, 27), 60, "Outros"),

    # --- IA ------------------------------------------------------------------------
    _certificado_pdf("intensivao-claude-hashtag", "Intensivão de Claude", "Hashtag Treinamentos",
                     datetime(2026, 9, 17), 8, "IA", tipo="evento"),

    # --- DIO (cursos, módulos, projetos e mentoria) -------------------------------
    _dio("J1FAXARR", "Boas-vindas ao Bootcamp Bradesco - GenAI, Dados & Cyber", "curso", datetime(2026, 6, 19), 1, "IA"),
    _dio("POKXUWGQ", "Tendências em IA e Cibersegurança Aplicadas ao Projeto Final", "mentoria", datetime(2026, 9, 27), 1, "IA"),
    _dio("NLWHEKUU", "Projeto Final: IA e Cibersegurança para Assistentes Virtuais no Mercado Financeiro", "módulo", datetime(2026, 9, 27), 2, "IA"),
    _dio("5GDDNOXW", "Construa seu Assistente Virtual com Inteligência Artificial", "projeto", datetime(2026, 9, 27), 1, "IA"),
    _dio("ES7NIVC3", "Cibersegurança Essencial: Bases para Seus Projetos com Dados e IA", "módulo", datetime(2026, 9, 26), 8, "Cibersegurança"),
    _dio("IUYLQVWR", "Introdução ao DevSecOps", "curso", datetime(2026, 9, 26), 1, "DevOps & Infra"),
    _dio("RQPXRZ37", "Tópicos em Engenharia Social", "curso", datetime(2026, 9, 26), 1, "Cibersegurança"),
    _dio("TSI702ML", "Introdução à Coleta e Análise de Segurança Cibernética", "curso", datetime(2026, 9, 26), 2, "Cibersegurança"),
    _dio("VZRK1QG9", "Conceitos e Práticas de Sistemas Operacionais e Máquinas Virtuais", "curso", datetime(2026, 9, 26), 2, "DevOps & Infra"),
    _dio("RKL8SSOA", "Princípios da Cibersegurança", "curso", datetime(2026, 9, 25), 2, "Cibersegurança"),
    _dio("6DUXDAQU", "Detecção de Anomalias em Transações em Python", "projeto", datetime(2026, 9, 25), 1, "Dados & SQL"),
    _dio("TMIFYMTU", "Análise de Dados com Python: Da Preparação à Aplicação com Segurança", "módulo", datetime(2026, 9, 25), 8, "Dados & SQL"),
    _dio("RCHL1CEV", "Boas Práticas, Testes e Otimização de Código em Python", "curso", datetime(2026, 9, 24), 1, "Python"),
    _dio("DFGBAGXE", "Visualização Avançada de Dados com Python", "curso", datetime(2026, 9, 23), 1, "Dados & SQL"),
    _dio("ZMXKOPTX", "Automação de Processos e Análises com Python", "curso", datetime(2026, 9, 23), 1, "Python"),
    _dio("U9W2ONRO", "Processamento e Limpeza de Dados em Python", "curso", datetime(2026, 9, 22), 1, "Dados & SQL"),
    _dio("PZICFMRW", "Bibliotecas Essenciais de Python para Análise de Dados", "curso", datetime(2026, 9, 21), 1, "Dados & SQL"),
    _dio("VOHDCMTG", "Tratamento de Exceções e Depuração de Código em Python", "curso", datetime(2026, 9, 21), 1, "Python"),
    _dio("JMGPI0PM", "Trabalhando com Arquivos e Dados Externos em Python", "curso", datetime(2026, 9, 20), 1, "Python"),
    _dio("4F0G6DIW", "Dominando Funções Python", "curso", datetime(2026, 9, 17), 1, "Python"),
    _dio("AHX16ZRI", "Estruturas em Python: Dados, Coleções e Funções", "módulo", datetime(2026, 9, 17), 6, "Python"),
    _dio("JQFPXACW", "Aprendendo a Utilizar Dicionários em Python", "curso", datetime(2026, 9, 15), 1, "Python"),
    _dio("FC4HL37C", "Conhecendo Tuplas em Python", "curso", datetime(2026, 9, 14), 1, "Python"),
    _dio("YUTFFGNI", "Explorando Conjuntos em Python", "curso", datetime(2026, 9, 14), 1, "Python"),
    _dio("17JILZJT", "Tipos de Operadores com Python", "curso", datetime(2026, 9, 13), 2, "Python"),
    _dio("2NRN1CXR", "Desafios de Código: Aperfeiçoe Sua Lógica e Pensamento Computacional", "curso", datetime(2026, 9, 13), 1, "Python"),
    _dio("30ZXCYBS", "Extraindo Insights do Feedback de Clientes Bancários", "módulo", datetime(2026, 9, 13), 1, "Dados & SQL"),
    _dio("5WCQQGOK", "Manipulando Strings com Python", "curso", datetime(2026, 9, 13), 2, "Python"),
    _dio("AXEV1TFE", "Fundamentos de Dados: Excel, SQL e Business Intelligence", "módulo", datetime(2026, 9, 13), 9, "Dados & SQL"),
    _dio("CVGFZHRK", "Trabalhando com Listas em Python", "curso", datetime(2026, 9, 13), 1, "Python"),
    _dio("G7YNVDWN", "Utilizando Microsoft Copilot para Escrever Consultas SQL", "curso", datetime(2026, 9, 13), 2, "Dados & SQL"),
    _dio("RSDPCCGJ", "Conhecendo a Linguagem de Programação Python", "curso", datetime(2026, 9, 13), 2, "Python"),
    _dio("RYQJAM4C", "Estruturas Condicionais e de Repetição em Python", "curso", datetime(2026, 9, 13), 2, "Python"),
    _dio("W5AHOWTW", "Ambiente de Desenvolvimento e Primeiros Passos com Python", "curso", datetime(2026, 9, 13), 1, "Python"),
    _dio("WGVNKHTG", "Criando um Processo de ETL com Excel e Power Query", "curso", datetime(2026, 9, 13), 1, "Dados & SQL"),
    _dio("XKYJZIBE", "Introdução ao Python: Primeiros Passos e Fundamentos", "módulo", datetime(2026, 9, 13), 11, "Python"),
    _dio("KFIFOCTD", "Introdução a Banco de Dados Relacionais", "curso", datetime(2026, 9, 6), 3, "Dados & SQL"),
    _dio("VKFRZ9IR", "IA Generativa: Fundamentos, Prompting e Aplicações", "módulo", datetime(2026, 7, 9), 12, "IA"),
    _dio("D5CJTTXK", "Treinando uma IA de Aprendizagem: Explore o Poder do NotebookLM", "projeto", datetime(2026, 7, 9), 4, "IA"),
    _dio("9CU3BT6C", "Introdução ao Excel 365", "curso", datetime(2026, 7, 16), 1, "Dados & SQL"),
    _dio("EKHCUSEU", "Trabalhando com Microsoft Copilot", "curso", datetime(2026, 7, 16), 1, "IA"),
    _dio("EY3BSUJP", "Técnicas de Engenharia de Prompt", "curso", datetime(2026, 7, 1), 2, "IA"),
    _dio("VMASXVZF", "Desafios de Projetos: Crie Um Portfólio Vencedor", "curso", datetime(2026, 7, 1), 1, "Carreira"),
    _dio("MXZ0FREZ", "Introdução à Engenharia de Prompts", "curso", datetime(2026, 6, 25), 1, "IA"),
    _dio("AVRIUFN1", "Fundamentos de Modelos de Linguagem de Grande Escala", "curso", datetime(2026, 6, 23), 1, "IA"),
    _dio("UX9OLFXE", "Fundamentos da IA Moderna: Machine Learning, LLMs, IA Generativa e Agentes", "curso", datetime(2026, 6, 21), 2, "IA"),
]


# Estatística do "Sobre" derivada dos próprios certificados (não desatualiza).
_horas_total = sum(int(c["carga_horaria"][:-1]) for c in certificados if c.get("carga_horaria"))
sobre["stats"][2] = {
    "numero": str(len(certificados)),
    "legenda": f"certificações e {_horas_total:,}h de estudo".replace(",", "."),
}
