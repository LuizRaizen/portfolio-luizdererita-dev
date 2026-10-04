"""
Blog do projeto Sentinela — agente de IA generativa para segurança de pagamentos Pix.
Fonte das informações: repositório https://github.com/LuizRaizen/dio-lab-bia-do-futuro
(README, docs/01 a docs/05, src/README e dados mockados).
"""

from datetime import datetime

# ------------------------------------------------------------------------------
# Nome do projeto (deve corresponder ao nome da pasta e à URL)
# ------------------------------------------------------------------------------

projeto = "sentinela-ai-agent"
repositorio = "https://github.com/LuizRaizen/dio-lab-bia-do-futuro"  # o repositório tem nome diferente do slug

# ------------------------------------------------------------------------------
# Ficha Técnica
# ------------------------------------------------------------------------------

ficha_tecnica = {
    "nome": "Sentinela",
    "linguagem": "Python",
    "framework": "Streamlit",
    "paradigma": "Agente conversacional: LLM para linguagem, regras determinísticas para decisões",
    "arquitetura": "Orquestrador + gateway de dados + motor de regras + validação de resposta + fallback humano",
    "tipo_projeto": "Agente de IA generativa para prevenção a golpes no Pix (projeto final do bootcamp)",
    "interface": "Chat web em Streamlit, com perfil do cliente e avisos de segurança na barra lateral",
    "funcionalidades": [
        "Triagem de relatos de golpe e orientação sobre o Mecanismo Especial de Devolução (MED)",
        "Alerta contra o golpe do “Pix errado” (nunca devolver para outra conta)",
        "Recusa segura: nunca pede senha, PIN, código OTP, token ou CVV",
        "Respostas baseadas só nos dados fornecidos, com admissão de limites quando não há informação",
        "Encaminhamento para atendimento humano em casos de risco ou incerteza",
    ],
    "bibliotecas": ["Streamlit"],
    "banco_de_dados": "Arquivos JSON e CSV (dados mockados)",
    "api_externa": ["Gemini API (configurável)"],
    "plataforma": "Web (execução local)",
    "resolucao": "",
    "status": "Protótipo concluído (projeto final do bootcamp)",
}

# ------------------------------------------------------------------------------
# Postagens do blog
# ------------------------------------------------------------------------------

posts = [
    {
        "titulo": "Sentinela: um agente de IA que ajuda o cliente a reagir a golpes no Pix",
        "data": datetime(2026, 9, 27),
        "autor": "Luiz R. Dererita",
        "nome_arquivo": "apresentando-o-sentinela",
        "imagem": "img/sentinela-ai-agent/print_1.png",
        "resumo": "Meu projeto final do Bootcamp Bradesco - GenAI, Dados & Cyber: um agente que orienta o cliente diante de um golpe no Pix sem decidir sozinho o que é fraude e sem nunca pedir credenciais.",
        "tags": ["IA generativa", "Segurança", "Pix", "Streamlit", "Bootcamp DIO"],
        "conteudo": """
        <p>
          O <strong>Sentinela</strong> é o meu projeto final do bootcamp <strong>Bradesco - GenAI, Dados &amp; Cyber</strong>, da DIO.
          O desafio era idealizar e prototipar um agente financeiro com IA generativa capaz de antecipar necessidades,
          personalizar sugestões, construir soluções de forma consultiva e, principalmente, <strong>garantir segurança e confiabilidade</strong>
          nas respostas, ou seja, evitar alucinações. Eu escolhi um problema específico e urgente: <strong>golpes envolvendo Pix</strong>.
        </p>
        <p>
          Também gravei um vídeo apresentando o projeto: <a href="https://www.youtube.com/watch?v=brxeV607BMY" target="_blank" rel="noopener">assista no YouTube</a>
          ou na página de <a href="/blogs/sentinela-ai-agent/videos">vídeos</a> deste blog.
        </p>

        <h3 class="section-title mt-4">O problema que quis resolver</h3>
        <p>
          Quando alguém cai em um golpe, o relógio corre. O Banco Central orienta que, em suspeita de fraude no Pix, o cliente procure sua instituição
          o mais rápido possível e peça a contestação pelo <strong>MED (Mecanismo Especial de Devolução)</strong>, que não garante a devolução e depende
          da análise do caso. Só que a pessoa está sob estresse, tem dificuldade para distinguir uma transação legítima de um golpe e não sabe
          qual procedimento seguir.
        </p>
        <p>
          O Sentinela ataca exatamente esse intervalo: <strong>reduzir o tempo entre a percepção de um possível golpe e a adoção das medidas corretas</strong>.
          Ele responde a perguntas como “acho que caí em um golpe, o que faço agora?” e “recebi uma mensagem pedindo para devolver um Pix, como sei se é verdade?”.
        </p>

        <h3 class="section-title mt-4">Princípio central: o agente não decide sozinho</h3>
        <p>
          A regra que guiou o projeto está na documentação logo no início: <strong>o agente não decide que uma transação é fraude</strong>.
          Ele coleta evidências, explica sinais de risco, consulta sistemas autorizados, orienta o cliente e encaminha o caso para os mecanismos formais do banco.
          Para mim, essa é a diferença entre um chatbot que impressiona e um agente em que se pode confiar. Cada parte do sistema tem uma função:
        </p>
        <ul>
          <li><strong>LLM:</strong> compreensão e comunicação;</li>
          <li><strong>regras:</strong> decisões determinísticas;</li>
          <li><strong>APIs bancárias:</strong> dados reais;</li>
          <li><strong>antifraude:</strong> avaliação especializada de risco;</li>
          <li><strong>autenticação e autorização:</strong> controle das ações;</li>
          <li><strong>humano:</strong> decisões complexas e exceções.</li>
        </ul>
        <p>Resumindo numa frase que repito na documentação: <em>o LLM é um componente de linguagem, não a autoridade financeira</em>.</p>

        <h3 class="section-title mt-4">Como o Sentinela atua</h3>
        <ol>
          <li><strong>Identifica a situação:</strong> fraude, golpe, Pix errado, cobrança suspeita, e faz só as perguntas necessárias.</li>
          <li><strong>Avalia o contexto:</strong> consulta, quando autorizado, dados estruturados da transação, sem deixar o modelo inventar o que não existe.</li>
          <li><strong>Responde de imediato:</strong> orienta a agir rápido e a seguir o fluxo oficial de contestação, sem prometer recuperação.</li>
          <li><strong>Previne novos danos:</strong> indica medidas de segurança e, se preciso, autenticação reforçada ou atendimento humano.</li>
          <li><strong>Encaminha:</strong> o que exige análise, bloqueio ou devolução vai para o sistema ou setor responsável.</li>
          <li><strong>Acompanha:</strong> informa o status de um protocolo a partir de dados oficiais, nunca de estimativas do modelo.</li>
        </ol>

        <h3 class="section-title mt-4">Arquitetura em camadas</h3>
        <p>
          Desenhei a arquitetura com um <strong>orquestrador</strong> no centro, que controla a conversa, as ferramentas e as permissões. Em volta dele:
          gerenciamento de sessão e identidade, o LLM, um <strong>motor de regras</strong>, um <strong>gateway de dados bancários</strong>
          (para que o modelo nunca acesse um banco de dados diretamente), a base de conhecimento, uma <strong>validação de resposta</strong> antes de
          qualquer mensagem chegar ao cliente, um <em>fallback</em> para atendimento humano e uma trilha de auditoria.
          Se a resposta não for considerada segura, ela não vai para o cliente: o caso é encaminhado.
        </p>

        <h3 class="section-title mt-4">Segurança e anti-alucinação</h3>
        <p>No setor financeiro, uma resposta “não sei” vale mais do que uma resposta inventada. Por isso o projeto define seis camadas de proteção:</p>
        <ol>
          <li><strong>Autenticação:</strong> dados individuais só dentro de uma sessão autenticada.</li>
          <li><strong>Autorização:</strong> estar autenticado não dá ao LLM acesso a tudo; cada ferramenta tem permissões explícitas.</li>
          <li><strong>Ferramentas controladas:</strong> o modelo pede uma operação (como consultar uma transação) e recebe só os campos autorizados.</li>
          <li><strong>Regras determinísticas:</strong> decisões críticas não saem de texto gerado.</li>
          <li><strong>Validação:</strong> checagem de fatos, números, promessas indevidas e pedidos de credenciais antes de responder.</li>
          <li><strong>Escalonamento:</strong> sem segurança para responder, o agente para de improvisar e encaminha.</li>
        </ol>
        <p>
          O Sentinela <strong>nunca pede senha, PIN, código OTP, token ou CVV</strong>, nunca promete que o dinheiro será recuperado e nunca recomenda
          devolver um Pix para uma conta diferente da origem, golpe clássico alertado pelo próprio Banco Central. Esses avisos aparecem na barra lateral da aplicação.
          A documentação também lista as limitações declaradas: o agente não decide fraude, não garante contestação aceita, não altera limites nem bloqueia contas.
        </p>

        <h3 class="section-title mt-4">Persona e tom de voz</h3>
        <p>
          Quem está sendo golpeado não precisa de juridiquês nem de alarmismo. O Sentinela é <strong>calmo, objetivo, protetivo e não julgador</strong>:
          nunca culpa o cliente, explica termos como o MED na primeira vez em que aparecem e prefere a opção mais segura quando há incerteza.
        </p>

        <h3 class="section-title mt-4">Prompts</h3>
        <p>
          O <em>system prompt</em> define o papel do agente e cinco regras: nunca inventar dados, ser calmo e resolutivo, colocar a segurança em primeiro lugar,
          deixar as limitações claras e orientar corretamente o caso do Pix errado. Completam o prompt exemplos de interação e <strong>casos-limite</strong>:
          pergunta fora do escopo (como a previsão do tempo), tentativa de fazer o agente alterar senha ou aprovar uma transação bloqueada,
          e pedido de recomendação de investimento sem contexto. Dois ajustes importantes: reforcei que o agente não declara fraude nem garante devolução,
          e acrescentei diretrizes sobre o golpe do “Pix errado” depois de constatar tentativas recorrentes de engenharia social nos testes.
        </p>

        <h3 class="section-title mt-4">Dados e aplicação</h3>
        <p>
          Usei <strong>dados mockados</strong> (fictícios): perfil do cliente, produtos financeiros, transações e histórico de atendimento, em JSON e CSV,
          o que garante consistência e evita dados sensíveis. A documentação também descreve como o gateway forneceria transações Pix com destinatário mascarado,
          sinais antifraude e políticas bancárias.
        </p>
        <p>
          A aplicação é um chat em <strong>Streamlit</strong>, dividido em <code>app.py</code> (interface), <code>agente.py</code> (lógica do agente e <em>system prompts</em>)
          e <code>config.py</code> (configurações e variáveis de ambiente). A chave da API é lida de um arquivo <code>.env</code>, com o modelo configurável (o exemplo do README usa o Gemini).
          Nos testes, o perfil e os produtos mockados serviram para validar a leitura de contexto pelo agente.
        </p>

        <h3 class="section-title mt-4">Avaliação</h3>
        <p>Executei quatro testes estruturados e todos ficaram como corretos:</p>
        <ul>
          <li><strong>Consulta de gastos:</strong> somou corretamente os lançamentos de alimentação (R$ 450,00 de supermercado e R$ 120,00 de restaurante) e informou R$ 570,00.</li>
          <li><strong>Recomendação de produto:</strong> respeitou o perfil moderado cadastrado.</li>
          <li><strong>Pergunta fora do escopo:</strong> recusou educadamente.</li>
          <li><strong>Informação inexistente:</strong> admitiu que não havia dados sobre o produto e encaminhou para atendimento humano, em vez de inventar.</li>
        </ul>
        <p>
          Dei a mim mesmo nota 5 em assertividade, segurança e coerência. É uma autoavaliação sobre um conjunto pequeno de testes controlados, não um benchmark.
          Anotei também o que falta: uma janela de contexto maior para contestações complexas e melhor tratamento de gírias e formas coloquiais de relatar golpes.
          As métricas de latência e consumo de tokens que registrei são estimativas de simulação (cerca de 350 ms até o primeiro token e 1,8 s por resposta),
          feitas com modelo local e temperatura 0,3.
        </p>

        <h3 class="section-title mt-4">Para onde isso pode ir</h3>
        <p>
          O MVP foi desenhado para fazer quatro coisas bem: identificar suspeita de golpe no Pix, consultar a transação com segurança, orientar o próximo passo oficial
          e encaminhar para contestação ou atendimento humano. A documentação prevê uma versão 2, com acompanhamento de protocolos, integração com sinais antifraude e painéis
          de qualidade, e uma versão 3, com detecção proativa de risco, desde que passe por validação de segurança e governança.
        </p>

        <h3 class="section-title mt-4">O que o Sentinela me ensinou</h3>
        <p>
          Construir um agente de IA é, em grande parte, decidir <strong>o que ele não pode fazer</strong>. No Sentinela, boa parte do trabalho foi desenhar essas fronteiras:
          o que o modelo diz, o que as regras decidem e o que um humano precisa assumir. Saio desse projeto com uma visão mais madura de segurança em IA generativa,
          que une engenharia de prompt, arquitetura e governança.
        </p>
        <p>
          O código e toda a documentação estão no GitHub: <a href="https://github.com/LuizRaizen/dio-lab-bia-do-futuro" target="_blank" rel="noopener">LuizRaizen/dio-lab-bia-do-futuro</a>.
        </p>
        """,
    },
]

# ------------------------------------------------------------------------------
# Roadmap do projeto
# ------------------------------------------------------------------------------

roadmap = [
    {"alerta": "Protótipo concluído como projeto final do bootcamp. Os próximos passos abaixo vêm da documentação do projeto"},

    {"status": "concluido", "meta": "Documentação do agente: caso de uso, persona, arquitetura e segurança"},
    {"status": "concluido", "meta": "Base de conhecimento com dados mockados"},
    {"status": "concluido", "meta": "System prompt, exemplos de interação e casos-limite"},
    {"status": "concluido", "meta": "Aplicação de chat em Streamlit integrada a um LLM"},
    {"status": "concluido", "meta": "Testes estruturados e avaliação de métricas"},
    {"status": "concluido", "meta": "Pitch em vídeo apresentando o projeto"},
    {"status": "planejado", "meta": "Versão 2: acompanhamento de protocolos e integração com sinais antifraude"},
    {"status": "planejado", "meta": "Versão 2: painéis de qualidade e segurança"},
    {"status": "planejado", "meta": "Versão 3: detecção proativa de risco e alertas antes de operações (com validação de segurança)"},
]

# ------------------------------------------------------------------------------
# Galeria de imagens
# ------------------------------------------------------------------------------

imagens = [
    {"src": "img/sentinela-ai-agent/print_1.png", "descricao": "Tela inicial: perfil do cliente, avisos de segurança e a consulta “Quanto gastei com alimentação?”"},
    {"src": "img/sentinela-ai-agent/print_2.png", "descricao": "Recomendação de produto respeitando o perfil moderado do cliente"},
    {"src": "img/sentinela-ai-agent/print_3.png", "descricao": "Pergunta fora do escopo (previsão do tempo) recusada com educação"},
    {"src": "img/sentinela-ai-agent/print_4.png", "descricao": "Consulta sobre um produto de risco alto, com aviso de que o perfil cadastrado é moderado"},
    {"src": "img/sentinela-ai-agent/print_5.png", "descricao": "Produto inexistente: o agente admite que não tem a informação e indica o atendimento humano"},
]

# ------------------------------------------------------------------------------
# Vídeos do projeto
# ------------------------------------------------------------------------------

videos = [
    {
        "youtube_id": "brxeV607BMY",
        "descricao": "Apresentação do projeto Sentinela (Bootcamp DIO.me: Bradesco - GenAI, Dados & Cyber)",
    },
]

# ------------------------------------------------------------------------------
# Arquivos disponíveis para download
# ------------------------------------------------------------------------------

downloads = []

# ------------------------------------------------------------------------------
# Cartão de exibição na Home
# ------------------------------------------------------------------------------

home_card = {
    "resumo": "Agente de IA generativa que orienta clientes diante de golpes no Pix, sem decidir sozinho o que é fraude e sem nunca pedir senhas ou códigos. Projeto final do Bootcamp Bradesco - GenAI, Dados & Cyber.",
    "categoria": "ia",
    "tecnologias": ["Python", "Streamlit", "IA Generativa", "Engenharia de Prompt", "Segurança"],
    "imagem": "img/sentinela_ai_agent_preview.webp",
    "ordem": 1,
    "destaque": True,
}
