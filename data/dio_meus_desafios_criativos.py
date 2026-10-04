"""
Blog do projeto DIO - Meus Desafios Criativos — repositório dos desafios do bootcamp
Bradesco (Análise de Dados, GenAI e Cyber) da DIO.me.
Fonte das informações: repositório https://github.com/LuizRaizen/dio-meus-desafios-criativos
"""

from datetime import datetime

# ------------------------------------------------------------------------------
# Nome do projeto (deve corresponder ao nome da pasta e à URL)
# ------------------------------------------------------------------------------

projeto = "dio-meus-desafios-criativos"
repositorio = "https://github.com/LuizRaizen/dio-meus-desafios-criativos"  # o repositório tem nome diferente do slug

# ------------------------------------------------------------------------------
# Ficha Técnica
# ------------------------------------------------------------------------------

ficha_tecnica = {
    "nome": "Meus Desafios Criativos",
    "linguagem": "Python (Jupyter Notebook)",
    "framework": "",
    "paradigma": "Análise exploratória de dados e aprendizado de máquina supervisionado",
    "arquitetura": "Repositório de desafios: um item (notebook ou documento) por entrega",
    "tipo_projeto": "Repositório dos desafios do Bootcamp Bradesco - GenAI, Dados & Cyber (DIO.me)",
    "interface": "Notebooks no Google Colab e documentos em Markdown",
    "funcionalidades": [
        "Detecção de anomalias em transações com Regressão Logística e Random Forest",
        "Avaliação com Precision, Recall, F1-Score e curvas ROC e Precision-Recall",
        "Prompt estruturado para análise de feedback de marketing",
    ],
    "bibliotecas": ["NumPy", "pandas", "scikit-learn", "Matplotlib", "seaborn"],
    "banco_de_dados": "",
    "api_externa": "",
    "plataforma": "Google Colab",
    "resolucao": "",
    "status": "Em andamento (recebe os desafios do bootcamp)",
}

# ------------------------------------------------------------------------------
# Postagens do blog
# ------------------------------------------------------------------------------

posts = [
    {
        "titulo": "Meus Desafios Criativos: o que aprendi com dados, prompts e fraudes no bootcamp da DIO",
        "data": datetime(2026, 9, 25),
        "autor": "Luiz R. Dererita",
        "nome_arquivo": "apresentando-meus-desafios-criativos",
        "imagem": "img/dio_meus_desafios_preview.webp",
        "resumo": "O repositório onde guardo os desafios do Bootcamp Bradesco - GenAI, Dados & Cyber: um prompt de análise de marketing e um notebook de detecção de fraudes em que o Random Forest superou a Regressão Logística.",
        "tags": ["Ciência de dados", "scikit-learn", "Engenharia de prompt", "Bootcamp DIO"],
        "conteudo": """
        <p>
          O <strong>dio-meus-desafios-criativos</strong> é o repositório em que guardo, organizo e documento as soluções dos desafios propostos pela
          <a href="https://www.dio.me/" target="_blank" rel="noopener">DIO.me</a> no bootcamp <strong>Bradesco - GenAI, Dados &amp; Cyber</strong>.
          Cada item do repositório é a entrega de um desafio prático, e é por ele que consigo mostrar, com código e documentação, o que estudei.
        </p>

        <h3 class="section-title mt-4">Os três pilares do bootcamp</h3>
        <ul>
          <li><strong>Análise de Dados:</strong> transformar e interpretar dados para apoiar decisões.</li>
          <li><strong>IA Generativa (GenAI):</strong> aplicar IA na resolução prática de problemas.</li>
          <li><strong>Cibersegurança:</strong> conceitos e práticas essenciais para proteger dados e sistemas.</li>
        </ul>
        <p>Os dois desafios que já estão no repositório tocam nesses três pilares. Vou apresentá-los.</p>

        <h3 class="section-title mt-4">Desafio 1: um prompt para analisar feedback de marketing</h3>
        <p>
          O primeiro entregável não é código: é um <strong>prompt</strong>. Escrevi um prompt em que a IA atua como <em>analista de dados de marketing</em>
          e analisa comentários de clientes em redes sociais sobre o lançamento de um produto, para identificar a percepção da marca e oportunidades de engajamento.
        </p>
        <p>O que mais me ensinou foi a <strong>anatomia</strong> do prompt. Ele tem papel, tarefa, contexto de uso, dados disponíveis (comentários, canal, curtidas e compartilhamentos), instruções de análise e formato de resposta:</p>
        <ul>
          <li>resumo executivo em até cinco linhas;</li>
          <li>tabela com tema, sentimento, evidência e ação sugerida;</li>
          <li>três recomendações prioritárias.</li>
        </ul>
        <p>
          E, principalmente, <strong>restrições</strong>: usar apenas os dados fornecidos, não inventar números, causas ou conclusões,
          não expor dados pessoais e informar as limitações quando os dados forem insuficientes. É a mesma disciplina contra alucinação
          que apliquei depois no <a href="/blogs/sentinela-ai-agent">Sentinela</a>.
        </p>

        <h3 class="section-title mt-4">Desafio 2: detecção de anomalias em transações</h3>
        <p>
          O segundo é um <strong>notebook no Google Colab</strong> para prever transações fraudulentas em um conjunto de dados público de cartão de crédito
          (<code>creditcard.csv</code>, disponibilizado pelo TensorFlow). O ponto de partida é o que torna fraude um problema difícil:
          <strong>as classes são muito desbalanceadas</strong>. Fraudes são raríssimas diante do total de transações.
        </p>
        <p>
          Por isso, acurácia não serve como régua. Um modelo que dissesse “nenhuma transação é fraude” teria acurácia altíssima e valor zero.
          Avaliei com <strong>Precision, Recall e F1-Score</strong> da classe de fraude.
        </p>

        <h4 class="mt-4">O caminho que segui</h4>
        <ol>
          <li><strong>Engenharia de features:</strong> apliquei <code>np.log1p</code> à coluna <code>Amount</code> para reduzir o peso de valores extremos e, depois, <code>StandardScaler</code> para padronizá-la.</li>
          <li><strong>Divisão estratificada:</strong> 70% para treino e 30% para teste, com <code>stratify</code> e <code>random_state=42</code>, para manter a proporção de fraudes nos dois conjuntos.</li>
          <li><strong>Baseline com Regressão Logística:</strong> na classe de fraude, precision de 0,84, recall de 0,65 e F1 de 0,73. O teste tinha 148 fraudes entre 85.443 transações.</li>
          <li><strong>Tentativas de melhora:</strong> o aviso de convergência persistiu mesmo aumentando <code>max_iter</code> para 2.500, e uma segunda padronização de <code>Amount</code> quase não mudou o resultado (0,85, 0,64 e 0,73). Registrei isso no notebook, porque saber o que <em>não</em> melhora um modelo também é resultado.</li>
          <li><strong>Random Forest:</strong> com 100 árvores e <code>class_weight='balanced'</code>, a classe de fraude foi para precision de 0,97, recall de 0,71 e F1 de 0,82.</li>
          <li><strong>Curvas ROC e Precision-Recall:</strong> comparei os dois modelos graficamente. A Precision-Recall é a mais informativa em dados desbalanceados, e nela o Random Forest também ficou à frente.</li>
        </ol>

        <h4 class="mt-4">Resultado e leitura crítica</h4>
        <table class="table table-dark table-bordered mt-3">
          <thead><tr><th>Modelo (classe fraude)</th><th>Precision</th><th>Recall</th><th>F1</th></tr></thead>
          <tbody>
            <tr><td>Regressão Logística</td><td>0,84</td><td>0,65</td><td>0,73</td></tr>
            <tr><td>Random Forest (balanceado)</td><td>0,97</td><td>0,71</td><td>0,82</td></tr>
          </tbody>
        </table>
        <p>
          O Random Forest foi o melhor dos dois. Mas o número que mais me chamou a atenção foi o <strong>recall de 0,71</strong>: em um sistema real,
          cerca de três em cada dez fraudes ainda passariam. Esse é o tipo de lição que um desafio como este entrega e que um tutorial não mostra:
          um bom F1 não significa um problema resolvido.
        </p>

        <h3 class="section-title mt-4">O que levo daqui</h3>
        <ul>
          <li>Prompt bom tem estrutura, formato de saída e <strong>restrições explícitas</strong>.</li>
          <li>Em dados desbalanceados, a escolha da <strong>métrica</strong> decide se a conclusão é honesta.</li>
          <li>Documentar tentativas que não funcionaram faz parte do trabalho.</li>
          <li>Um repositório organizado por desafio vira, ao mesmo tempo, diário de estudo e portfólio.</li>
        </ul>
        <p>
          O repositório continua recebendo os desafios do bootcamp: <a href="https://github.com/LuizRaizen/dio-meus-desafios-criativos" target="_blank" rel="noopener">LuizRaizen/dio-meus-desafios-criativos</a>.
        </p>
        """,
    },
]

# ------------------------------------------------------------------------------
# Roadmap do projeto
# ------------------------------------------------------------------------------

roadmap = [
    {"alerta": "Este repositório recebe os desafios do bootcamp à medida que são concluídos"},

    {"status": "concluido", "meta": "Prompt de análise de feedback de marketing"},
    {"status": "concluido", "meta": "Notebook de detecção de anomalias em transações (Regressão Logística e Random Forest)"},
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
    "resumo": "Repositório dos desafios do Bootcamp Bradesco - GenAI, Dados & Cyber: detecção de fraudes com scikit-learn e um prompt estruturado de análise de marketing.",
    "categoria": "dados",
    "tecnologias": ["Python", "scikit-learn", "pandas", "Google Colab", "Engenharia de Prompt"],
    "imagem": "img/dio_meus_desafios_preview.webp",
    "ordem": 2,
}
