"""Lista de postagens do blog do Floux."""

from datetime import datetime

projeto = "tela-cadastro-login-multi-ui"

ficha_tecnica = {
    "nome": "Tela de Cadastro e Login Multi-UI",
    "linguagem": "Python",
    "framework": "Tkinter, PySide6, Kivy",
    "paradigma": "Programação Orientada a Objetos (OOP)",
    "arquitetura": "MVC modular com separação clara entre lógica, UI e persistência",
    "tipo_projeto": "rede social onde os usuários se conectam por meio de <strong>temas, ideias e interesses compartilhados</strong>, organizando conversas por fluxos de pensamento",
    "interface": "UI moderna com botões estilizados e foco em usabilidade",
    "funcionalidades": [
        "Proteção de senhas com bcrypt (hash + salt)",
        "Cadastro, login, validação de credenciais, persistência em banco de dados",
        "Seleção da interface gráfica via linha de comando"
    ],
    "bibliotecas": [],
    "banco_de_dados": "SQlite",
    "api_externa": "",
    "plataforma": "Desktop (Windows / Linux)",
    "resolucao": "",
    "status": "Finalizado (fase de estudo e referência pessoal)"
}

posts = [
    {
        "titulo": "Um Banco de Dados, Diferentes Interfaces",
        "data": datetime(2025, 6, 12),
        "autor": "Luiz R. Dererita",
        "nome_arquivo": "post1",
        "conteudo": """
        <p>Este projeto foi um divisor de águas na minha jornada de aprendizado com Python. A <strong>Tela de Cadastro e Login Multi-UI</strong> é um sistema simples de autenticação com banco de dados que oferece a possibilidade de ser executado com três interfaces gráficas diferentes: <strong>Tkinter, PySide6 e Kivy</strong>. A seleção da UI é feita diretamente pela linha de comando, o que me permitiu estudar de forma prática como diferentes frameworks gráficos se comportam para a mesma aplicação lógica.</p>

        <h2 class="section-title mt-4">Exploração de Tecnologias</h2>
        <p>O backend foi desenvolvido com <strong>SQLite</strong>, um banco leve e eficiente para projetos locais. Toda a lógica de cadastro e login foi implementada com base no padrão <strong>MVC</strong>, algo que eu estava começando a estudar com mais profundidade na época. Pela primeira vez, comecei a refletir sobre a separação de responsabilidades dentro de um sistema, o que me ajudou bastante em projetos posteriores.</p>
        <p>Outro aspecto marcante foi o uso de <strong>bcrypt</strong> para proteger as senhas dos usuários. Aprendi sobre <strong>hash</strong> e <strong>salt</strong>, e como implementá-los para dificultar o vazamento de dados sensíveis. Essa foi uma das primeiras vezes que me aproximei de conceitos de <strong>segurança da informação</strong> no desenvolvimento.</p>

        <h2 class="section-title mt-4">ChatGPT como Aliado</h2>
        <p>Este projeto também foi meu <strong>primeiro contato prático com o ChatGPT</strong> como ferramenta técnica. Durante o desenvolvimento, enfrentei diversos desafios — desde dúvidas sobre estruturação de arquivos até detalhes de lógica para hashing. Foi nesse momento que percebi o poder das <strong>ferramentas de IA</strong> no suporte ao desenvolvimento e aprendizagem.</p>

        <h2 class="section-title mt-4">Por que Multi-UI?</h2>
        <p>Uma das minhas motivações foi justamente entender as diferenças entre os frameworks. Com esse sistema, eu consegui observar como <strong>componentes equivalentes</strong> (como campos de entrada, botões, mensagens de erro) são implementados em diferentes bibliotecas.</p>
        <ul>
          <li><strong>Tkinter:</strong> Rápido para prototipagem, leve e nativo do Python.</li>
          <li><strong>PySide6:</strong> Interface moderna com visual mais profissional.</li>
          <li><strong>Kivy:</strong> Multiplataforma, com foco em touch e dispositivos móveis.</li>
        </ul>

        <h2 class="section-title mt-4">Reflexão Final</h2>
        <p>Mesmo sendo um projeto simples à primeira vista, esse CRUD me ensinou muito sobre <strong>estruturas robustas, boas práticas, modularização e segurança</strong>. É um projeto que guardo com muito carinho, pois representa o momento em que comecei a conectar os pontos entre front-end e back-end, e enxergar o desenvolvimento de forma mais completa e profissional.</p>
        
        <p class="meta-info">Postado em <strong>9 de Junho de 2025</strong> por <strong>Luiz R. Dererita</strong></p>
       
        """,
    },
]

# Lista de metas definidas para a conclusão do projeto
roadmap = [
    {"status": "concluido", "meta": "Interface gráfica finalizada"},
    {"status": "desenvolvimento", "meta": "Integração com API da OpenAI"},
    {"status": "planejado", "meta": "Envio automático de e-mails"},
    {"alerta": "Este projeto está em fase de desenvolvimento"}
]

imagens = [
    {"src": "img/tela-cadastro-login-multi-ui/tk_ui.jpg", "descricao": "Tela de Login com Tkinter"},
    {"src": "img/tela-cadastro-login-multi-ui/qt_ui.jpg", "descricao": "Tela de Cadastro de Usuário com PySide6"},
    {"src": "img/tela-cadastro-login-multi-ui/kv_ui.jpg", "descricao": "Tela de Login com Kivy"},
]

videos = []

downloads = []
