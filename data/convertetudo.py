"""
Módulo de configuração do projeto para exibição dinâmica no portfólio/blog.

Este módulo define as informações estruturadas sobre um projeto específico,
incluindo dados técnicos, posts, roadmap, imagens, vídeos e arquivos para download.
Ele será importado dinamicamente pelo sistema Flask do site.

Exemplo de uso:
    from data import convertetudo
    dados = carregar_projeto(convertetudo)
"""

from datetime import datetime

# ------------------------------------------------------------------------------
# Nome do projeto (deve corresponder ao nome da pasta e à URL)
# ------------------------------------------------------------------------------

projeto = "convertetudo"  # slug usado na pasta e na rota /blogs/convertetudo

# O banner.png deste projeto já tem o logo e o nome "ConverteTudo" desenhados
# na própria imagem — por isso a capa do blog não deve sobrepor um <h1> extra.
banner_tem_titulo = True

# ------------------------------------------------------------------------------
# Ficha Técnica
# ------------------------------------------------------------------------------

ficha_tecnica = {
    "nome": "ConverteTudo",
    "linguagem": "Python",
    "framework": "Django",
    "paradigma": "MVT (Model-View-Template) + módulos JS (fetch/AJAX)",
    "arquitetura": "Monólito web com apps por ferramenta",
    "tipo_projeto": "Plataforma web de conversão de arquivos (foco inicial em imagens)",
    "interface": "Web responsiva, multilíngue (i18n) com acessibilidade",
    "funcionalidades": [
        "Conversão em lote de imagens (JPG, PNG, WEBP, TIFF...)",
        "UI com arrastar-e-soltar e barra de progresso",
        "Limites de tamanho e quantidade com tratamento elegante de erros",
        "Suporte a múltiplos idiomas e SEO técnico (titles, hreflang)",
        "Estrutura pronta para AdSense e blocos de anúncios",
    ],
    "bibliotecas": ["Pillow (PIL)", "Django i18n", "Redis (fila de tarefas)", "Gunicorn + UvicornWorker"],
    "banco_de_dados": "",
    "api_externa": "",
    "plataforma": "Web (Desktop / Mobile) — deploy em Render",
    "resolucao": "",
    "status": "Em produção (MVP em evolução)"
}

# ------------------------------------------------------------------------------
# Postagens do blog
# ------------------------------------------------------------------------------

posts = [
    {
        "titulo": "Lançamento do ConverteTudo — Um Novo Capítulo",
        "data": datetime(2025, 10, 19),
        "autor": "Luiz R. Dererita",
        "nome_arquivo": "lancamento-convertetudo",
        "imagem": "img/convertetudo_preview.webp",
        "conteudo": """
        <p>
          Hoje eu finalmente posso dizer com orgulho: o <strong>ConverteTudo</strong> está no ar! 🚀
          Esse projeto nasceu de um desejo antigo de criar algo útil, bonito e acessível para qualquer pessoa,
          mas também de uma vontade muito pessoal: me destacar como desenvolvedor, e quem sabe,
          transformar isso em algo que possa gerar frutos reais no futuro.
        </p>

        <p>
          O ConverteTudo é um site de <strong>ferramentas online para conversão de arquivos</strong>,
          começando por imagens (JPG, PNG, WEBP, TIFF e outros), mas com planos muito maiores pela frente.
          A ideia é simples: permitir que qualquer pessoa converta, comprima ou edite seus arquivos
          diretamente do navegador — de forma rápida, intuitiva e segura.
          E o melhor: ele já está no ar em produção, acessível através do domínio oficial
          <a href="https://converte-tudo-online.com.br" target="_blank" rel="noopener">
          converte-tudo-online.com.br</a>.
        </p>

        <h2 class="section-title mt-4">Por que eu criei o ConverteTudo</h2>
        <p>
          Essa ideia surgiu em um momento em que eu queria unir aprendizado, propósito e visão de futuro.
          Eu sabia que existem diversas ferramentas de conversão na internet, mas eu queria fazer algo diferente:
          algo que tivesse <strong>minha identidade</strong>, que refletisse cuidado com design,
          performance, privacidade e usabilidade. 
        </p>
        <p>
          Além disso, eu queria construir uma base sólida — um projeto real, que pudesse me destacar
          não só no mercado de trabalho, mas também abrir portas para um possível investimento futuro.
          O ConverteTudo é, ao mesmo tempo, uma vitrine das minhas habilidades e um passo concreto
          em direção à independência criativa e financeira.
        </p>

        <h2 class="section-title mt-4">Das origens: o IMG Convert</h2>
        <p>
          O ConverteTudo tem uma origem muito especial. Ele nasceu a partir de um outro projeto
          que também está no meu portfólio: o 
          <a href="http://luizdererita-dev.up.railway.app/blogs/img-convert" target="_blank"><strong>IMG Convert</strong></a>.
          O IMG Convert foi meu primeiro conversor de imagens — uma aplicação <strong>desktop</strong> feita com 
          <code>Python</code>, utilizando a biblioteca <strong>PIL</strong> (Pillow) para o processamento das imagens
          e <strong>PySide6</strong> para a interface gráfica.
        </p>
        <p>
          A ideia do ConverteTudo surgiu justamente da vontade de levar essa experiência do desktop para a web,
          tornando-a acessível para qualquer pessoa, em qualquer lugar. Foi um desafio técnico e criativo:
          eu precisei adaptar o núcleo de conversão do IMG Convert e reescrevê-lo em uma arquitetura voltada
          para <strong>Django</strong>, com um backend sólido e um frontend dinâmico, controlado via 
          <code>JavaScript (fetch/AJAX)</code>.
        </p>
        <p>
          Mas o mais interessante é que a versão original do IMG Convert <strong>não será descartada</strong>.
          Pelo contrário — ela vai evoluir junto. Meu plano é transformá-la em uma 
          <strong>versão Desktop oficial do ConverteTudo</strong>, totalmente repaginada e com a identidade visual atual,
          unificando os dois projetos sob o mesmo ecossistema.
        </p>

        <h2 class="section-title mt-4">Tecnologia e Estrutura</h2>
        <p>
          O site foi construído em <strong>Django</strong> (Python) e segue o padrão MVT (Model-View-Template).
          Todo o fluxo de upload e conversão acontece de forma assíncrona, com 
          <code>JavaScript</code> controlando o envio de arquivos e a atualização da barra de progresso —
          tudo isso sem recarregar a página. 
        </p>
        <p>
          O deploy foi feito na plataforma <strong>Render</strong>, utilizando <code>Gunicorn</code> com 
          <code>UvicornWorker</code>, garantindo estabilidade e boa performance mesmo em múltiplas requisições simultâneas.
        </p>
        <p>
          E claro, o projeto já está preparado para <strong>Google AdSense</strong> e futuras campanhas de monetização.
          Os espaços publicitários estão estrategicamente posicionados e pensados para não atrapalhar a navegação,
          mantendo a experiência do usuário como prioridade.
        </p>

        <h2 class="section-title mt-4">Multilíngue, SEO e alcance internacional</h2>
        <p>
          Um dos diferenciais do ConverteTudo é seu sistema <strong>multilinguagem completo</strong>.
          Ele foi implementado com <code>Django i18n</code> e permite traduzir toda a interface do site —
          desde os textos principais até os títulos, metatags e mensagens de acessibilidade.
        </p>
        <p>
          Esse sistema não é apenas um recurso estético: ele tem um propósito estratégico.
          Foi planejado para ampliar o <strong>alcance internacional do site</strong>,
          otimizando a indexação em motores de busca (SEO) e tornando o ConverteTudo visível em diferentes idiomas.
          Hoje, ele já conta com suporte para <strong>Português, Inglês e Espanhol</strong>,
          com planos de expansão para mais idiomas conforme o público crescer.
        </p>
        <p>
          Esse detalhe técnico pode parecer pequeno, mas é o tipo de cuidado que faz diferença
          para quem quer que o projeto seja encontrado por pessoas de todo o mundo.
        </p>

        <h2 class="section-title mt-4">O que vem a seguir</h2>
        <p>
          O ConverteTudo ainda está em seu <strong>MVP</strong> (Produto Mínimo Viável),
          mas já está totalmente funcional e preparado para crescer. As próximas ferramentas previstas
          incluem um conversor de <strong>PDF</strong>, compactador de arquivos, ferramentas para 
          <strong>áudio e vídeo</strong> e muitas outras ideias que já estão no meu roteiro de desenvolvimento.
        </p>
        <p>
          Cada nova ferramenta será adicionada diretamente ao site, mantendo a mesma proposta: 
          simplicidade, eficiência e compatibilidade com qualquer dispositivo.
        </p>

        <h2 class="section-title mt-4">Um projeto com propósito</h2>
        <p>
          Eu acredito de verdade que o ConverteTudo pode se destacar.
          Não apenas por ser uma ferramenta funcional, mas por carregar uma filosofia de desenvolvimento honesta:
          oferecer algo de qualidade, gratuito, e feito com dedicação. 
        </p>
        <p>
          É um projeto que me motiva, que representa meu crescimento como desenvolvedor
          e que, ao mesmo tempo, pode ser útil para muita gente.
          Mesmo sabendo que existem dezenas de ferramentas parecidas por aí,
          o que eu quero é construir algo que tenha <strong>personalidade</strong>, 
          <strong>identidade visual própria</strong> e uma <strong>proposta transparente</strong>.
        </p>

        <p>
          E esse é só o começo. 💡
        </p>

        <p class="meta-info">
          Postado em <strong>19 de outubro de 2025</strong> por <strong>Luiz R. Dererita</strong>
        </p>
        """
    }
]

# ------------------------------------------------------------------------------
# Roadmap
# ------------------------------------------------------------------------------

roadmap = [
    {"alerta": "MVP em produção; novas ferramentas serão habilitadas conforme validação de uso."},
    {"status": "concluido", "meta": "Deploy no Render com pipeline de build e logging"},
    {"status": "concluido", "meta": "Conversor de imagens com suporte a múltiplos formatos"},
    {"status": "concluido", "meta": "UI de arrastar-e-soltar, barra de progresso e feedback de erros"},
    {"status": "concluido", "meta": "Estrutura multilíngue (Django i18n) e títulos traduzíveis"},
    {"status": "concluido", "meta": "Espaços reservados para AdSense e SEO técnico inicial"},
    {"status": "desenvolvimento", "meta": "Hreflang e sitemap por idioma"},
    {"status": "desenvolvimento", "meta": "Presets de qualidade e redimensionamento no conversor de imagens"},
    {"status": "desenvolvimento", "meta": "Página inicial com destaque de ferramentas e blog integrado"},
    {"status": "planejado", "meta": "Ferramentas para PDF (mesclar, comprimir, converter)"},
    {"status": "planejado", "meta": "Ferramentas para áudio e vídeo (converter, extrair áudio)"},
    {"status": "planejado", "meta": "Fila de tarefas para lotes grandes (escala e robustez)"},
    {"status": "planejado", "meta": "Dark mode elegante e preferências salvas no navegador"},
    {"status": "planejado", "meta": "Métricas de uso e experimentos de UX para aumentar conversão"},
]

# ------------------------------------------------------------------------------
# Galeria
# ------------------------------------------------------------------------------

imagens = [
    {
        "src": "img/convertetudo/ct_preview.png",
        "descricao": "Prévia geral do ConverteTudo — homepage e identidade visual principal da plataforma."
    },
    {
        "src": "img/convertetudo/ct_languages.png",
        "descricao": "Sistema multilíngue em funcionamento — interface adaptada para diferentes idiomas e SEO internacional."
    },
    {
        "src": "img/convertetudo/ct_dark_mode.png",
        "descricao": "Visual moderno do modo escuro — interface refinada com contraste e design responsivo."
    },
    {
        "src": "img/convertetudo/ct_mobile.png",
        "descricao": "Versão mobile do ConverteTudo — interface otimizada para smartphones e tablets."
    },
]

# ------------------------------------------------------------------------------
# Vídeos
# ------------------------------------------------------------------------------

videos = []

# ------------------------------------------------------------------------------
# Downloads
# ------------------------------------------------------------------------------

downloads = [
    {
        "nome": "robots.txt (modelo)",
        "descricao": "Modelo usado na configuração inicial para buscadores.",
        "arquivo": "downloads/convertetudo/convertetudo_robots.txt"
    },
    {
        "nome": "ads.txt (modelo)",
        "descricao": "Modelo base para verificação do Google AdSense.",
        "arquivo": "downloads/convertetudo/convertetudo_ads.txt"
    },
]

# ------------------------------------------------------------------------------
# Cartão de exibição na Home
# ------------------------------------------------------------------------------

home_card = {
    "resumo": "Plataforma web de ferramentas online para conversão de imagens, documentos, áudios e vídeos. O projeto prioriza velocidade, privacidade e acessibilidade — com suporte a múltiplos idiomas e otimização para SEO e Google AdSense.",
    "categoria": "web",
    "tecnologias": ["Python", "Django", "Redis", "JavaScript", "HTML5", "CSS3"],
    "imagem": "img/convertetudo_preview.webp",
    "ordem": 10,
    "destaque": True,
}
