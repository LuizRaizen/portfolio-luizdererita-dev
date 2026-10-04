"""
Blog do projeto Guia Dev Web 2026 (NotebookLM) — caderno temático de estudos com IA.
Fonte das informações: repositório https://github.com/LuizRaizen/guia-dev-web-2026-notebooklm
"""

from datetime import datetime

# ------------------------------------------------------------------------------
# Nome do projeto (deve corresponder ao nome da pasta e à URL)
# ------------------------------------------------------------------------------

projeto = "guia-dev-web-2026-notebooklm"
repositorio = "https://github.com/LuizRaizen/guia-dev-web-2026-notebooklm"  # o repositório tem nome diferente do slug

# ------------------------------------------------------------------------------
# Ficha Técnica
# ------------------------------------------------------------------------------

ficha_tecnica = {
    "nome": "Guia Dev Web 2026",
    "linguagem": "",
    "framework": "NotebookLM",
    "paradigma": "Aprendizagem guiada por IA, com engenharia de prompts",
    "arquitetura": "Caderno temático: fontes curadas + prompt de professor virtual",
    "tipo_projeto": "Caderno de estudos sobre Desenvolvimento Web em 2026",
    "interface": "NotebookLM",
    "funcionalidades": [
        "Curadoria de cinco fontes públicas sobre desenvolvimento web em 2026",
        "Três versões do prompt: inicial, refinado e final",
        "Curso interativo com módulos, exercícios, provas e nota mínima 80 para avançar",
        "Tabela de problemas e soluções incorporadas ao prompt",
        "Miniguia de estudo, glossário e prompts reutilizáveis",
    ],
    "bibliotecas": ["NotebookLM", "Markdown", "Git", "GitHub"],
    "banco_de_dados": "",
    "api_externa": "",
    "plataforma": "NotebookLM (Google)",
    "resolucao": "",
    "status": "Concluído",
}

# ------------------------------------------------------------------------------
# Postagens do blog
# ------------------------------------------------------------------------------

posts = [
    {
        "titulo": "Estudando Desenvolvimento Web em 2026 com um professor virtual no NotebookLM",
        "data": datetime(2026, 7, 10),
        "autor": "Luiz R. Dererita",
        "nome_arquivo": "apresentando-o-guia-dev-web-2026",
        "imagem": "img/guia_dev_web_notebooklm_preview.webp",
        "resumo": "Um caderno temático no NotebookLM para estudar Desenvolvimento Web em 2026: fontes curadas, três versões de prompt e um professor virtual que só me deixa avançar com nota 80.",
        "tags": ["IA generativa", "Engenharia de prompt", "NotebookLM", "Estudos"],
        "conteudo": """
        <p>
          Este projeto não tem uma linha de código de aplicação, e mesmo assim é um dos que mais me ensinou sobre trabalhar com IA.
          Durante o bootcamp, construí um <strong>Caderno Temático no NotebookLM</strong> sobre <strong>Desenvolvimento Web em 2026</strong>.
          O objetivo nunca foi ter só um resumo do assunto: eu queria aprender a usar uma IA como ferramenta de pesquisa,
          de organização de conhecimento e de apoio aos estudos.
        </p>

        <h3 class="section-title mt-4">O que eu quis aprender</h3>
        <ul>
          <li>entender de verdade o tema escolhido;</li>
          <li>usar o NotebookLM de forma estratégica;</li>
          <li>praticar engenharia de prompts;</li>
          <li>criar um material de estudo que eu possa reutilizar;</li>
          <li>desenvolver pensamento crítico sobre as respostas de uma IA;</li>
          <li>montar um guia de revisão para consultas futuras.</li>
        </ul>

        <h3 class="section-title mt-4">Curadoria de fontes</h3>
        <p>
          O NotebookLM responde com base nas fontes que você entrega, então a qualidade do caderno depende da curadoria.
          Selecionei <strong>cinco fontes abertas</strong>, de acesso livre, que cobrem ameaças cibernéticas impulsionadas por IA em 2026,
          conformidade de acessibilidade (WCAG e ADA), o WCAG 3.0 e testes de acessibilidade, e engenharia de back-end para escala,
          desempenho e confiabilidade. A lista completa está no repositório.
        </p>

        <h3 class="section-title mt-4">Três versões de um prompt</h3>
        <p>O coração do projeto foi iterar o prompt e registrar o que cada versão entregava.</p>
        <p>
          <strong>Prompt inicial.</strong> Pedi uma trilha de estudos em módulos, do iniciante ao avançado. A resposta veio bem organizada,
          com progressão, projetos e comparações entre tecnologias. Mas era mais um <em>roadmap</em> do que um curso: faltavam explicações
          profundas, exemplos, exercícios e critérios de avaliação. Alguns temas avançados também apareciam antes de os fundamentos estarem consolidados.
        </p>
        <p>
          <strong>Prompt refinado.</strong> Passei a exigir um <em>curso completo, aprofundado e progressivo</em>, com objetivos de aprendizagem,
          exemplos de código comentados, boas práticas, erros comuns, comparações e um projeto ao fim de cada módulo.
          As respostas ficaram mais detalhadas, mais contextualizadas e mais bem organizadas.
        </p>
        <p>
          <strong>Prompt final.</strong> Aqui a IA deixa de entregar conteúdo e passa a <strong>conduzir o ensino</strong>, como um professor rigoroso:
        </p>
        <ul>
          <li>cada módulo traz pré-requisitos, teoria antes da prática, demonstrações e código totalmente comentado;</li>
          <li>cada assunto é classificado como <strong>Essencial</strong>, <strong>Importante</strong> ou <strong>Complementar</strong>, com justificativa;</li>
          <li>os exercícios têm dificuldade crescente (conceituais, leitura de código, programação e <em>debug</em>) e <strong>as respostas nunca vêm antes da minha tentativa</strong>;</li>
          <li>a IA corrige, explica cada erro e atribui <strong>nota de 0 a 100</strong>;</li>
          <li>só posso avançar de módulo com <strong>nota mínima de 80</strong>; abaixo disso recebo revisão personalizada e uma nova avaliação;</li>
          <li>ao concluir tudo, o curso gera um <strong>certificado simbólico</strong> e um prompt para criar a imagem dele.</li>
        </ul>

        <h3 class="section-title mt-4">As “cicatrizes”</h3>
        <p>
          Cada problema que encontrei virou uma regra no prompt. Respostas genéricas e resumos superficiais deram origem à exigência de profundidade e contexto.
          Conceitos confusos pediram analogias e exemplos do mundo real. Texto demais pediu títulos, tabelas e resumos estruturados.
          A dificuldade de fixação trouxe exercícios progressivos e projetos, e o avanço prematuro foi resolvido com a nota mínima. Tudo isso está numa tabela no repositório.
        </p>

        <h3 class="section-title mt-4">O material de apoio</h3>
        <p>
          Além do prompt, montei um <strong>miniguia de estudo</strong>, um <strong>glossário</strong> com conceitos como front-end, back-end,
          arquitetura de software, API e avaliação formativa e somativa, e cinco <strong>prompts reutilizáveis</strong> para explicar, resumir,
          comparar, gerar exercícios e fazer quizzes de revisão.
        </p>

        <h3 class="section-title mt-4">O que fica</h3>
        <p>
          Desenvolvi curadoria de conteúdo, engenharia de prompts, pensamento crítico, pesquisa assistida por IA, organização de conhecimento
          e documentação técnica. Mais do que obter respostas, aprendi que o ganho está em <strong>saber fazer as perguntas certas</strong>
          e em não aceitar a primeira resposta como a melhor.
        </p>
        <p>
          O caderno está documentado no GitHub: <a href="https://github.com/LuizRaizen/guia-dev-web-2026-notebooklm" target="_blank" rel="noopener">LuizRaizen/guia-dev-web-2026-notebooklm</a>.
        </p>
        """,
    },
]

# ------------------------------------------------------------------------------
# Roadmap do projeto
# ------------------------------------------------------------------------------

roadmap = [
    {"status": "concluido", "meta": "Curadoria de cinco fontes públicas sobre Desenvolvimento Web em 2026"},
    {"status": "concluido", "meta": "Prompt inicial e análise de pontos positivos e limitações"},
    {"status": "concluido", "meta": "Prompt refinado: curso completo e aprofundado"},
    {"status": "concluido", "meta": "Prompt final: professor interativo com provas e nota mínima 80"},
    {"status": "concluido", "meta": "Tabela de problemas e soluções incorporadas ao prompt"},
    {"status": "concluido", "meta": "Miniguia de estudo, glossário e prompts reutilizáveis"},
]

# ------------------------------------------------------------------------------
# Galeria de imagens
# ------------------------------------------------------------------------------

imagens = []

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
    "resumo": "Caderno temático no NotebookLM para estudar Desenvolvimento Web em 2026: fontes curadas, três versões de prompt e um professor virtual que avalia cada módulo.",
    "categoria": "ia",
    "tecnologias": ["NotebookLM", "Markdown", "GitHub", "Engenharia de Prompt"],
    "imagem": "img/guia_dev_web_notebooklm_preview.webp",
    "ordem": 3,
}
