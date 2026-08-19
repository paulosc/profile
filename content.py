# -*- coding: utf-8 -*-
"""Every translatable string on the site, in one place.

Key naming: <page-or-block>.<slug>. English is the source of truth and is what
gets written into the HTML, so the site still reads correctly if JavaScript
never runs.
"""

S = {}


def add(key, en, pt, es):
    S[key] = {"en": en, "pt": pt, "es": es}


# ---------------------------------------------------------------- navigation
add("nav.work", u"Work", u"Trabalhos", u"Trabajos")
add("nav.experience", u"Experience", u"Trajetória", u"Trayectoria")
add("nav.about", u"About", u"Sobre", u"Sobre mí")
add("nav.services", u"Services &amp; pricing", u"Serviços e preços", u"Servicios y precios")
add("nav.services_short", u"Services", u"Serviços", u"Servicios")
add("nav.quote", u"Get a quote", u"Pedir orçamento", u"Pedir presupuesto")

# ---------------------------------------------------------------- home hero
add("home.status", u"Open to new projects", u"Disponível para novos projetos", u"Disponible para nuevos proyectos")
add("home.h1", u"Paulo Carvalho.<br><span class=\"accent\">Java backend engineer.</span>",
    u"Paulo Carvalho.<br><span class=\"accent\">Engenheiro backend Java.</span>",
    u"Paulo Carvalho.<br><span class=\"accent\">Ingeniero backend Java.</span>")
add("home.lede1",
    u"Eighteen years building and repairing production backends. Telecom systems for Ericsson, banking microservices for Ita&uacute;, five years on healthcare platforms for a Canadian software company, and seven years that also covered firmware on devices nobody could restart remotely.",
    u"Dezoito anos construindo e consertando backends em produção. Sistemas de telecomunicações para a Ericsson, microsserviços bancários para o Ita&uacute;, cinco anos em plataformas de saúde para uma empresa canadense, e sete anos que também envolveram firmware em dispositivos que ninguém conseguia reiniciar remotamente.",
    u"Dieciocho años construyendo y reparando backends en producción. Sistemas de telecomunicaciones para Ericsson, microservicios bancarios para Ita&uacute;, cinco años en plataformas de salud para una empresa canadiense, y siete años que también incluyeron firmware en dispositivos que nadie podía reiniciar en remoto.")
add("home.lede2",
    u"These days I work in Java and Spring Boot with Kafka and AWS, and I build and run products of my own on the side.",
    u"Hoje trabalho com Java e Spring Boot, Kafka e AWS, e mantenho produtos próprios rodando em paralelo.",
    u"Hoy trabajo con Java y Spring Boot, Kafka y AWS, y mantengo productos propios en marcha en paralelo.")
add("home.cta1", u"See the work", u"Ver os trabalhos", u"Ver los trabajos")
add("home.cta2", u"What I can build for you", u"O que posso construir para você", u"Lo que puedo construir para ti")

add("cred.ericsson", u"TELECOM &middot; VIA ICC", u"TELECOM &middot; VIA ICC", u"TELECOM &middot; VÍA ICC")
add("cred.itau", u"BANKING &middot; VIA ZUP", u"BANCOS &middot; VIA ZUP", u"BANCA &middot; VÍA ZUP")
add("cred.policy", u"CANADA &middot; HEALTHCARE", u"CANADÁ &middot; SAÚDE", u"CANADÁ &middot; SALUD")
add("cred.years_n", u"18 years", u"18 anos", u"18 años")
add("cred.years", u"SINCE 2008", u"DESDE 2008", u"DESDE 2008")
add("cred.postgrad_n", u"Postgraduate", u"Pós-graduação", u"Posgrado")
add("cred.postgrad", u"INATEL &middot; ENG.", u"INATEL &middot; ENG.", u"INATEL &middot; ING.")

# ---------------------------------------------------------------- work
add("work.label", u"Selected work", u"Trabalhos selecionados", u"Trabajos seleccionados")
add("work.h2", u"Things I built and still run.", u"Coisas que construí e ainda mantenho.", u"Cosas que construí y todavía mantengo.")

add("work.itau.h", u"Banking platform for Ita&uacute;", u"Plataforma bancária para o Ita&uacute;", u"Plataforma bancaria para Ita&uacute;")
add("work.itau.meta", u"Via Zup &middot; 2023&mdash;present", u"Via Zup &middot; 2023&mdash;hoje", u"Vía Zup &middot; 2023&mdash;hoy")
add("work.itau.p1",
    u"Microservices in Java and Spring Boot for Ita&uacute;, one of the largest banks in Brazil, delivered through Zup &mdash; event-driven communication over Kafka and AWS SQS, with Python Lambdas handling asynchronous work at the edges.",
    u"Microsserviços em Java e Spring Boot para o Ita&uacute;, um dos maiores bancos do Brasil, entregues através da Zup &mdash; comunicação orientada a eventos com Kafka e AWS SQS, e Lambdas em Python cuidando do trabalho assíncrono nas bordas.",
    u"Microservicios en Java y Spring Boot para Ita&uacute;, uno de los mayores bancos de Brasil, entregados a través de Zup &mdash; comunicación orientada a eventos con Kafka y AWS SQS, con Lambdas en Python encargadas del trabajo asíncrono en los bordes.")
add("work.itau.p2",
    u"Unit, integration and synthetic tests under TDD and BDD, running through CI/CD on every change. In a bank, “we&rsquo;ll fix it in the next deploy” is not an available answer, and the test suite is what makes that survivable.",
    u"Testes unitários, de integração e sintéticos sob TDD e BDD, rodando em CI/CD a cada mudança. Em banco, “arrumamos no próximo deploy” não é uma resposta disponível, e é a suíte de testes que torna isso sustentável.",
    u"Pruebas unitarias, de integración y sintéticas bajo TDD y BDD, ejecutadas en CI/CD en cada cambio. En un banco, “lo arreglamos en el próximo despliegue” no es una respuesta disponible, y la suíte de pruebas es lo que lo hace sostenible.")

add("work.policy.h", u"PolicyMedical &amp; Acuma Health", u"PolicyMedical e Acuma Health", u"PolicyMedical y Acuma Health")
add("work.policy.meta", u"Canada &middot; healthcare &middot; 2018&mdash;2023", u"Canadá &middot; saúde &middot; 2018&mdash;2023", u"Canadá &middot; salud &middot; 2018&mdash;2023")
add("work.policy.p1",
    u"Five years with a Canadian healthcare software company &mdash; later acquired by RL Datix &mdash; on clinical document and policy management for hospitals. Java 11 and Spring Boot on the backend, with MySQL, MongoDB and Elasticsearch/OpenSearch behind search that had to return the right document, not a plausible one.",
    u"Cinco anos em uma empresa canadense de software para saúde &mdash; depois comprada pela RL Datix &mdash; em gestão de documentos clínicos e políticas hospitalares. Java 11 e Spring Boot no backend, com MySQL, MongoDB e Elasticsearch/OpenSearch por trás de uma busca que precisava devolver o documento certo, não um plausível.",
    u"Cinco años en una empresa canadiense de software para salud &mdash; después adquirida por RL Datix &mdash; en gestión de documentos clínicos y políticas hospitalarias. Java 11 y Spring Boot en el backend, con MySQL, MongoDB y Elasticsearch/OpenSearch detrás de una búsqueda que tenía que devolver el documento correcto, no uno plausible.")
add("work.policy.p2",
    u"This is where the architecture moved decisively toward microservices, and where I also built the front ends in Vue and Angular &mdash; which is why I can usually tell whether a problem is really in the backend before anyone opens a ticket.",
    u"Foi aí que a arquitetura migrou de vez para microsserviços, e onde também construí os front ends em Vue e Angular &mdash; por isso costumo saber se o problema está mesmo no backend antes de alguém abrir chamado.",
    u"Fue ahí donde la arquitectura migró definitivamente a microservicios, y donde también construí los front ends en Vue y Angular &mdash; por eso suelo saber si el problema está realmente en el backend antes de que alguien abra un ticket.")

add("work.icc.h", u"Telecom systems for Ericsson", u"Sistemas de telecom para a Ericsson", u"Sistemas de telecom para Ericsson")
add("work.icc.meta", u"Via ICC &mdash; Inatel Competence Center &middot; 2011&mdash;2018", u"Via ICC &mdash; Inatel Competence Center &middot; 2011&mdash;2018", u"Vía ICC &mdash; Inatel Competence Center &middot; 2011&mdash;2018")
add("work.icc.p1",
    u"Seven years at the Inatel Competence Center in Santa Rita do Sapuca&iacute;, much of it on telecom projects delivered for Ericsson &mdash; Java with JSF and PrimeFaces, in the era when the stack was far more tightly coupled than it is today. It included three months on site in Sweden with the client team.",
    u"Sete anos no Inatel Competence Center, em Santa Rita do Sapuca&iacute;, boa parte deles em projetos de telecomunicações entregues para a Ericsson &mdash; Java com JSF e PrimeFaces, na época em que o stack era bem mais acoplado do que hoje. Incluiu três meses na Suécia junto do time do cliente.",
    u"Siete años en el Inatel Competence Center, en Santa Rita do Sapuca&iacute;, buena parte en proyectos de telecomunicaciones entregados para Ericsson &mdash; Java con JSF y PrimeFaces, en la época en que el stack era mucho más acoplado que hoy. Incluyó tres meses en Suecia junto al equipo del cliente.")
add("work.icc.p2",
    u"The same years covered embedded work: C on FreeRTOS and Embedded Linux. That teaches a habit that never leaves you &mdash; there is no restarting the process on a device already installed in the field, so you get the resource handling and the failure paths right the first time. It is why I write the error branch before the happy path.",
    u"Os mesmos anos cobriram trabalho embarcado: C sobre FreeRTOS e Linux embarcado. Isso ensina um hábito que nunca vai embora &mdash; não existe reiniciar o processo num dispositivo já instalado em campo, então você acerta o uso de recursos e os caminhos de falha de primeira. É por isso que escrevo o ramo de erro antes do caminho feliz.",
    u"Esos mismos años incluyeron trabajo embebido: C sobre FreeRTOS y Linux embebido. Eso enseña un hábito que no se olvida &mdash; no existe reiniciar el proceso en un dispositivo ya instalado en campo, así que aciertas el manejo de recursos y las rutas de fallo a la primera. Por eso escribo la rama de error antes del camino feliz.")

add("work.pedifood.h", u"PediFood", u"PediFood", u"PediFood")
add("work.pedifood.meta", u"Own product", u"Produto próprio", u"Producto propio")
add("work.pedifood.p1",
    u"A delivery platform built for small towns rather than capitals &mdash; the places the big apps ignore because the order volume does not justify their commission. Java and Spring Boot on the backend, Angular on the front, running on AWS.",
    u"Uma plataforma de delivery feita para cidades pequenas, e não para capitais &mdash; os lugares que os aplicativos grandes ignoram porque o volume de pedidos não justifica a comissão deles. Java e Spring Boot no backend, Angular no front, rodando na AWS.",
    u"Una plataforma de delivery hecha para pueblos pequeños, no para capitales &mdash; los lugares que las apps grandes ignoran porque el volumen de pedidos no justifica su comisión. Java y Spring Boot en el backend, Angular en el front, corriendo en AWS.")

# ---------------------------------------------------------------- timeline
add("hist.label", u"Full history", u"Trajetória completa", u"Trayectoria completa")
add("hist.zup.h", u"Zup &mdash; Java Backend Developer", u"Zup &mdash; Desenvolvedor Backend Java", u"Zup &mdash; Desarrollador Backend Java")
add("hist.zup.p", u"Banking microservices for Ita&uacute;. Java, Spring Boot, Kafka, AWS, Docker, TDD/BDD, Scrum.",
    u"Microsserviços bancários para o Ita&uacute;. Java, Spring Boot, Kafka, AWS, Docker, TDD/BDD, Scrum.",
    u"Microservicios bancarios para Ita&uacute;. Java, Spring Boot, Kafka, AWS, Docker, TDD/BDD, Scrum.")
add("hist.policy.h", u"PolicyMedical (Canada) &mdash; Backend &amp; Full Stack Developer",
    u"PolicyMedical (Canadá) &mdash; Desenvolvedor Backend e Full Stack",
    u"PolicyMedical (Canadá) &mdash; Desarrollador Backend y Full Stack")
add("hist.policy.p", u"Healthcare document platforms; company later acquired by RL Datix. Java 11, Spring Boot, MySQL, MongoDB, Elasticsearch, Vue, Angular, Kafka, SQS, Jenkins, AWS.",
    u"Plataformas de documentos para saúde; empresa depois comprada pela RL Datix. Java 11, Spring Boot, MySQL, MongoDB, Elasticsearch, Vue, Angular, Kafka, SQS, Jenkins, AWS.",
    u"Plataformas de documentos para salud; empresa después adquirida por RL Datix. Java 11, Spring Boot, MySQL, MongoDB, Elasticsearch, Vue, Angular, Kafka, SQS, Jenkins, AWS.")
add("hist.icc.h", u"ICC &mdash; Inatel Competence Center &mdash; Embedded &amp; Full Stack Developer",
    u"ICC &mdash; Inatel Competence Center &mdash; Desenvolvedor Embarcado e Full Stack",
    u"ICC &mdash; Inatel Competence Center &mdash; Desarrollador Embebido y Full Stack")
add("hist.icc.p", u"Telecom projects for Ericsson, including three months on site in Sweden. Java, JSF and PrimeFaces; plus C, FreeRTOS and Embedded Linux.",
    u"Projetos de telecom para a Ericsson, incluindo três meses na Suécia. Java, JSF e PrimeFaces; além de C, FreeRTOS e Linux embarcado.",
    u"Proyectos de telecom para Ericsson, incluidos tres meses en Suecia. Java, JSF y PrimeFaces; además de C, FreeRTOS y Linux embebido.")
add("hist.imagem.h", u"Imagem &mdash; Java Backend Developer", u"Imagem &mdash; Desenvolvedor Backend Java", u"Imagem &mdash; Desarrollador Backend Java")
add("hist.imagem.p", u"Geoprocessing systems with Java, ArcGIS and MongoDB.",
    u"Sistemas de geoprocessamento com Java, ArcGIS e MongoDB.",
    u"Sistemas de geoprocesamiento con Java, ArcGIS y MongoDB.")
add("hist.kiq.h", u"Kiq Software &mdash; where it started", u"Kiq Software &mdash; onde tudo começou", u"Kiq Software &mdash; donde empezó todo")
add("hist.kiq.p", u"First Java projects, as an intern.", u"Primeiros projetos em Java, como estagiário.", u"Primeros proyectos en Java, como pasante.")
add("hist.pronatec.h", u"Pronatec &mdash; volunteer programming instructor", u"Pronatec &mdash; instrutor voluntário de programação", u"Pronatec &mdash; instructor voluntario de programación")
add("hist.pronatec.p", u"Taught logic and programming to teenagers in a social project.",
    u"Ensinei lógica e programação para adolescentes em um projeto social.",
    u"Enseñé lógica y programación a adolescentes en un proyecto social.")

# ---------------------------------------------------------------- education
add("edu.label", u"Education", u"Formação", u"Formación")
add("edu.post.h", u"Postgraduate, Electronic Systems Engineering, Automation &amp; Industrial Control",
    u"Pós-graduação em Engenharia de Sistemas Eletrônicos, Automação e Controle Industrial",
    u"Posgrado en Ingeniería de Sistemas Electrónicos, Automatización y Control Industrial")
add("edu.bach.h", u"Bachelor&rsquo;s Degree, Information Systems", u"Bacharelado em Sistemas de Informação", u"Licenciatura en Sistemas de Información")

# ---------------------------------------------------------------- about
add("about.label", u"About", u"Sobre", u"Sobre mí")
add("about.h2", u"How I got here.", u"Como cheguei aqui.", u"Cómo llegué hasta aquí.")
add("about.p1",
    u"I started in 2008 as an intern writing Java, and the path since then has been unusually wide: geoprocessing first, then seven years at the Inatel Competence Center on telecom work for Ericsson alongside embedded firmware in C, then five years on healthcare software for a Canadian company, and now banking microservices.",
    u"Comecei em 2008 como estagiário escrevendo Java, e o caminho desde então foi incomumente largo: geoprocessamento primeiro, depois sete anos no Inatel Competence Center em trabalho de telecom para a Ericsson junto com firmware embarcado em C, depois cinco anos em software de saúde para uma empresa canadense, e agora microsserviços bancários.",
    u"Empecé en 2008 como pasante escribiendo Java, y el camino desde entonces ha sido inusualmente amplio: geoprocesamiento primero, luego siete años en el Inatel Competence Center en trabajo de telecom para Ericsson junto con firmware embebido en C, después cinco años en software de salud para una empresa canadiense, y ahora microservicios bancarios.")
add("about.p2",
    u"That range is the point. Having written code for a device you cannot reach once it ships changes how you write a web service &mdash; you stop assuming the happy path and start writing the failure branch first.",
    u"Essa amplitude é justamente o ponto. Ter escrito código para um dispositivo que você não alcança depois de enviado muda o jeito de escrever um serviço web &mdash; você para de presumir o caminho feliz e passa a escrever o ramo de falha primeiro.",
    u"Ese rango es justamente el punto. Haber escrito código para un dispositivo que no puedes alcanzar una vez enviado cambia cómo escribes un servicio web &mdash; dejas de asumir el camino feliz y empiezas escribiendo la rama de fallo.")
add("about.p3",
    u"I have worked in English daily since the Ericsson years, including three months on site with the client team in Sweden.",
    u"Trabalho em inglês diariamente desde os anos de Ericsson, incluindo três meses presenciais com o time do cliente na Suécia.",
    u"Trabajo en inglés a diario desde los años de Ericsson, incluidos tres meses presenciales con el equipo del cliente en Suecia.")
add("about.stack", u"Core stack", u"Stack principal", u"Stack principal")
add("about.also", u"Also worked with", u"Também trabalhei com", u"También he trabajado con")
add("about.langs", u"Languages", u"Idiomas", u"Idiomas")
add("about.langs.p", u"Portuguese &mdash; native<br>English &mdash; advanced, daily use with international teams",
    u"Português &mdash; nativo<br>Inglês &mdash; avançado, uso diário com times internacionais",
    u"Portugués &mdash; nativo<br>Inglés &mdash; avanzado, uso diario con equipos internacionales")

# ---------------------------------------------------------------- hire band
add("hire.label", u"Available for contract work", u"Disponível para projetos", u"Disponible para proyectos")
add("hire.h2", u"Need something built, upgraded or unstuck?", u"Precisa construir, atualizar ou destravar algo?", u"¿Necesitas construir, actualizar o desatascar algo?")
add("hire.p", u"I take on fixed-scope projects &mdash; API integrations, legacy Java upgrades, and the bug your team has been circling for weeks. Price agreed before I start.",
    u"Aceito projetos de escopo fechado &mdash; integrações de API, atualização de Java legado, e aquele bug que seu time circula há semanas. Preço combinado antes de eu começar.",
    u"Acepto proyectos de alcance cerrado &mdash; integraciones de API, actualización de Java heredado, y ese bug que tu equipo lleva semanas rodeando. Precio acordado antes de empezar.")
add("hire.cta", u"See services &amp; pricing", u"Ver serviços e preços", u"Ver servicios y precios")

# ---------------------------------------------------------------- services hero
add("svc.status", u"Taking work &middot; fixed price", u"Aceitando projetos &middot; preço fechado", u"Aceptando proyectos &middot; precio cerrado")
add("svc.h1", u"What I can<br><span class=\"accent\">build for you.</span>",
    u"O que posso<br><span class=\"accent\">construir para você.</span>",
    u"Lo que puedo<br><span class=\"accent\">construir para ti.</span>")
add("svc.lede", u"Fixed scope, fixed price, tested code. Price your project below in about a minute &mdash; no discovery call needed just to find out roughly what it costs.",
    u"Escopo fechado, preço fechado, código testado. Calcule seu projeto abaixo em cerca de um minuto &mdash; sem precisar de reunião só para descobrir quanto custa.",
    u"Alcance cerrado, precio cerrado, código probado. Calcula tu proyecto abajo en cerca de un minuto &mdash; sin necesidad de una reunión solo para saber cuánto cuesta.")
add("svc.cta1", u"Price your project", u"Calcular meu projeto", u"Calcular mi proyecto")
add("svc.cta2", u"See my background", u"Ver minha trajetória", u"Ver mi trayectoria")

add("svc.label", u"What I sell", u"O que eu vendo", u"Lo que vendo")
add("svc.h2", u"Fixed scope. Fixed price.", u"Escopo fechado. Preço fechado.", u"Alcance cerrado. Precio cerrado.")
add("svc.intro", u"No hourly billing, no open-ended retainers. You buy a defined outcome, you know the number before I start, and you get tests that prove it works.",
    u"Sem cobrança por hora, sem contrato aberto. Você compra um resultado definido, sabe o valor antes de eu começar, e recebe testes que provam que funciona.",
    u"Sin cobro por hora, sin contratos abiertos. Compras un resultado definido, sabes el número antes de que empiece, y recibes pruebas que demuestran que funciona.")
add("svc.from", u"from", u"a partir de", u"desde")

# service cards
_CARDS = [
    ("api", u"Integration", u"Integração", u"Integración",
     u"Third-party API integration", u"Integração de API de terceiros", u"Integración de API de terceros",
     [(u"OAuth2, API keys, JWT &mdash; handled properly", u"OAuth2, chaves de API, JWT &mdash; feito direito", u"OAuth2, claves de API, JWT &mdash; hecho bien"),
      (u"Retry with backoff and rate-limit handling", u"Retry com backoff e tratamento de rate limit", u"Reintentos con backoff y manejo de rate limit"),
      (u"Webhooks and idempotency", u"Webhooks e idempotência", u"Webhooks e idempotencia"),
      (u"Tests that fail loudly when the provider changes", u"Testes que falham alto quando o fornecedor muda", u"Pruebas que fallan de forma evidente cuando el proveedor cambia")]),
    ("upgrade", u"Modernization", u"Modernização", u"Modernización",
     u"Legacy Java &amp; Spring upgrade", u"Atualização de Java e Spring legado", u"Actualización de Java y Spring heredado",
     [(u"Java 8/11 &rarr; 17 or 21", u"Java 8/11 &rarr; 17 ou 21", u"Java 8/11 &rarr; 17 o 21"),
      (u"Spring Boot 2 &rarr; 3, including javax &rarr; jakarta", u"Spring Boot 2 &rarr; 3, incluindo javax &rarr; jakarta", u"Spring Boot 2 &rarr; 3, incluyendo javax &rarr; jakarta"),
      (u"Dependency conflicts and CVEs resolved", u"Conflitos de dependência e CVEs resolvidos", u"Conflictos de dependencias y CVEs resueltos"),
      (u"Green build and passing suite before handover", u"Build verde e suíte passando antes da entrega", u"Build en verde y suíte pasando antes de la entrega")]),
    ("bug", u"Rescue", u"Resgate", u"Rescate",
     u"The bug nobody can find", u"O bug que ninguém acha", u"El bug que nadie encuentra",
     [(u"Race conditions, leaks, timeouts, lock contention", u"Condições de corrida, vazamentos, timeouts, contenção de lock", u"Condiciones de carrera, fugas, timeouts, contención de locks"),
      (u"Reproduced first &mdash; that is the part people skip", u"Reproduzido primeiro &mdash; é a parte que as pessoas pulam", u"Reproducido primero &mdash; es la parte que la gente se salta"),
      (u"Fixed with a test that fails without the fix", u"Corrigido com um teste que falha sem a correção", u"Corregido con una prueba que falla sin el arreglo"),
      (u"If I can&rsquo;t find it, I tell you instead of billing guesses", u"Se eu não achar, eu te digo em vez de cobrar por palpite", u"Si no lo encuentro, te lo digo en vez de cobrarte conjeturas")]),
    ("ai", u"AI", u"IA", u"IA",
     u"AI feature in an existing product", u"Recurso de IA em um produto existente", u"Función de IA en un producto existente",
     [(u"Retrieval, extraction, classification, tool use", u"Retrieval, extração, classificação, uso de ferramentas", u"Retrieval, extracción, clasificación, uso de herramientas"),
      (u"Eval harness so you know when quality regresses", u"Suíte de eval para você saber quando a qualidade cai", u"Suíte de evaluación para saber cuándo baja la calidad"),
      (u"Cost per request measured, not guessed", u"Custo por requisição medido, não estimado", u"Coste por solicitud medido, no estimado"),
      (u"Built on your data and your systems", u"Construído sobre seus dados e seus sistemas", u"Construido sobre tus datos y tus sistemas")]),
    ("data", u"Data", u"Dados", u"Datos",
     u"Scraper &amp; scheduled pipeline", u"Scraper e pipeline agendado", u"Scraper y pipeline programado",
     [(u"Extraction, normalization, relational storage", u"Extração, normalização, armazenamento relacional", u"Extracción, normalización, almacenamiento relacional"),
      (u"Scheduled re-checks with drift alerts", u"Reverificação agendada com alerta de mudança", u"Reverificación programada con alertas de cambio"),
      (u"Optional dashboard", u"Painel opcional", u"Panel opcional")]),
    ("cicd", u"Infrastructure", u"Infraestrutura", u"Infraestructura",
     u"CI/CD from zero", u"CI/CD do zero", u"CI/CD desde cero",
     [(u"Build, test, deploy, rollback", u"Build, teste, deploy, rollback", u"Build, prueba, despliegue, rollback"),
      (u"GitHub Actions or GitLab CI", u"GitHub Actions ou GitLab CI", u"GitHub Actions o GitLab CI"),
      (u"Environments and secrets done sanely", u"Ambientes e segredos organizados com san&iacute;dade", u"Entornos y secretos organizados con sensatez")]),
    ("review", u"Advisory", u"Consultoria", u"Consultoría",
     u"Architecture review", u"Revisão de arquitetura", u"Revisión de arquitectura",
     [(u"I read the repository, not a slide deck", u"Eu leio o repositório, não uma apresentação", u"Leo el repositorio, no una presentación"),
      (u"Risks, bottlenecks, scaling limits and cost", u"Riscos, gargalos, limites de escala e custo", u"Riesgos, cuellos de botella, límites de escala y coste"),
      (u"Written so a non-technical board can follow it", u"Escrito para uma diretoria não técnica acompanhar", u"Escrito para que una directiva no técnica pueda seguirlo"),
      (u"Optional remediation plan, sequenced by effort", u"Plano de correção opcional, sequenciado por esforço", u"Plan de corrección opcional, secuenciado por esfuerzo")]),
]
for cid, e1, p1, s1, e2, p2, s2, bullets in _CARDS:
    add("card.%s.tag" % cid, e1, p1, s1)
    add("card.%s.h" % cid, e2, p2, s2)
    for i, (be, bp, bs) in enumerate(bullets):
        add("card.%s.b%d" % (cid, i), be, bp, bs)

# ---------------------------------------------------------------- quote block
add("q.label", u"Instant quote", u"Orçamento instantâneo", u"Presupuesto instantáneo")
add("q.h2", u"Price your project now.", u"Calcule seu projeto agora.", u"Calcula tu proyecto ahora.")
add("q.intro", u"Pick what you need. The price and delivery date update as you go &mdash; no discovery call required to find out roughly what this costs.",
    u"Escolha o que precisa. Preço e prazo se atualizam conforme você marca &mdash; sem reunião só para descobrir a ordem de grandeza.",
    u"Elige lo que necesitas. El precio y el plazo se actualizan sobre la marcha &mdash; sin reunión solo para saber el orden de magnitud.")
add("q.step1", u"What do you need?", u"Do que você precisa?", u"¿Qué necesitas?")
add("q.step2", u"Scope", u"Escopo", u"Alcance")
add("q.step3", u"Timing", u"Prazo", u"Plazo")
add("q.rush.t", u"Rush delivery", u"Entrega acelerada", u"Entrega acelerada")
add("q.rush.d", u"Cuts the timeline roughly in half. I reshuffle other work to do it.",
    u"Corta o prazo praticamente pela metade. Eu reorganizo outros trabalhos para isso.",
    u"Reduce el plazo casi a la mitad. Reorganizo otros trabajos para lograrlo.")
add("q.yours", u"Your quote", u"Seu orçamento", u"Tu presupuesto")
add("q.terms", u"USD &middot; fixed price &middot; 50% to start", u"USD &middot; preço fechado &middot; 50% para começar", u"USD &middot; precio cerrado &middot; 50% para empezar")
add("q.delivery", u"Delivery", u"Entrega", u"Entrega")
add("q.revisions", u"Revisions", u"Revisões", u"Revisiones")
add("q.send", u"Send this brief", u"Enviar este briefing", u"Enviar este briefing")
add("q.copy", u"Copy brief", u"Copiar briefing", u"Copiar briefing")
add("q.copied", u"Brief copied", u"Briefing copiado", u"Briefing copiado")
add("q.fine", u"Quote holds for 14 days. Before either of us commits, we do a 20-minute call so I can confirm the scope is what you actually need &mdash; sometimes it isn&rsquo;t, and I&rsquo;ll say so.",
    u"O orçamento vale por 14 dias. Antes de qualquer compromisso, fazemos uma conversa de 20 minutos para eu confirmar se o escopo é o que você realmente precisa &mdash; às vezes não é, e eu vou dizer.",
    u"El presupuesto vale 14 días. Antes de comprometernos, hacemos una llamada de 20 minutos para confirmar que el alcance es lo que realmente necesitas &mdash; a veces no lo es, y te lo diré.")
add("q.days", u"days", u"dias", u"días")
add("q.day", u"day", u"dia", u"día")

# ---------------------------------------------------------------- process
add("proc.label", u"How it works", u"Como funciona", u"Cómo funciona")
add("proc.h2", u"Four steps, no surprises.", u"Quatro passos, sem surpresas.", u"Cuatro pasos, sin sorpresas.")
add("proc.1.h", u"You send the brief", u"Você envia o briefing", u"Envías el briefing")
add("proc.1.p", u"Use the quote tool above, or just write me. I need the problem, not a specification &mdash; writing the specification is part of what you&rsquo;re paying for.",
    u"Use a ferramenta de orçamento acima, ou simplesmente me escreva. Eu preciso do problema, não de uma especificação &mdash; escrever a especificação faz parte do que você está pagando.",
    u"Usa la herramienta de presupuesto de arriba, o simplemente escríbeme. Necesito el problema, no una especificación &mdash; escribir la especificación es parte de lo que estás pagando.")
add("proc.2.h", u"Twenty-minute call", u"Conversa de vinte minutos", u"Llamada de veinte minutos")
add("proc.2.p", u"I confirm the scope and either lock the price or tell you it&rsquo;s wrong. Roughly one in four projects turns out to be smaller than the client assumed, and I&rsquo;d rather say that up front than discover it in week two.",
    u"Confirmo o escopo e ou travo o preço ou digo que ele está errado. Cerca de um em cada quatro projetos acaba sendo menor do que o cliente imaginava, e prefiro dizer isso logo a descobrir na segunda semana.",
    u"Confirmo el alcance y o fijo el precio o te digo que está mal. Aproximadamente uno de cada cuatro proyectos resulta ser más pequeño de lo que el cliente suponía, y prefiero decirlo de entrada que descubrirlo en la segunda semana.")
add("proc.3.h", u"50% to start", u"50% para começar", u"50% para empezar")
add("proc.3.p", u"Work begins. You get repository access from day one and can watch the commits &mdash; no black box, no weekly status theatre.",
    u"O trabalho começa. Você recebe acesso ao repositório no primeiro dia e acompanha os commits &mdash; sem caixa-preta, sem teatro de status semanal.",
    u"El trabajo comienza. Tienes acceso al repositorio desde el primer día y puedes seguir los commits &mdash; sin caja negra, sin teatro de estado semanal.")
add("proc.4.h", u"Delivery, then the balance", u"Entrega, depois o restante", u"Entrega, luego el resto")
add("proc.4.p", u"Code, tests, and a short written handover explaining what I did and what to watch. Revisions included as quoted. You pay the rest when it&rsquo;s working.",
    u"Código, testes e um documento curto de passagem explicando o que fiz e o que observar. Revisões incluídas conforme o orçamento. Você paga o restante quando estiver funcionando.",
    u"Código, pruebas y un breve documento de traspaso explicando qué hice y qué vigilar. Revisiones incluidas según el presupuesto. Pagas el resto cuando funciona.")

# ---------------------------------------------------------------- footer
add("foot.h2", u"Let&rsquo;s scope it.", u"Vamos definir o escopo.", u"Definamos el alcance.")
add("foot.p", u"Tell me what&rsquo;s broken or what needs building. If it isn&rsquo;t something I should take on, I&rsquo;ll say so and point you somewhere better.",
    u"Me conte o que está quebrado ou o que precisa ser construído. Se não for algo que eu deva pegar, eu digo e te aponto um caminho melhor.",
    u"Cuéntame qué está roto o qué hay que construir. Si no es algo que deba tomar, te lo digo y te oriento hacia un lugar mejor.")
add("foot.reply", u"Replies within one business day", u"Respondo em até um dia útil", u"Respondo en un día hábil")
add("foot.contact", u"Contact", u"Contato", u"Contacto")
add("foot.where", u"Brazil &middot; UTC&minus;3 &middot; full overlap with US Eastern hours<br>Advanced English, daily work with international teams",
    u"Brasil &middot; UTC&minus;3 &middot; sobreposição total com o horário comercial dos EUA<br>Inglês avançado, trabalho diário com times internacionais",
    u"Brasil &middot; UTC&minus;3 &middot; solapamiento total con el horario comercial de EE. UU.<br>Inglés avanzado, trabajo diario con equipos internacionales")
add("foot.note", u"Paulo S&eacute;rgio Carvalho &middot; Java backend &amp; integration engineering &middot; Working in English and Portuguese",
    u"Paulo S&eacute;rgio Carvalho &middot; Engenharia de backend e integração em Java &middot; Atendimento em inglês e português",
    u"Paulo S&eacute;rgio Carvalho &middot; Ingeniería de backend e integración en Java &middot; Atención en inglés y portugués")

# ---------------------------------------------------------------- page meta
add("meta.home.title", u"Paulo Carvalho — Java Backend Engineer", u"Paulo Carvalho — Engenheiro Backend Java", u"Paulo Carvalho — Ingeniero Backend Java")
add("meta.home.desc", u"Java backend engineer, 18 years. Telecom for Ericsson, banking for Itaú, healthcare in Canada.",
    u"Engenheiro backend Java, 18 anos. Telecom para a Ericsson, bancos para o Itaú, saúde no Canadá.",
    u"Ingeniero backend Java, 18 años. Telecom para Ericsson, banca para Itaú, salud en Canadá.")
add("meta.svc.title", u"Services & Pricing — Paulo Carvalho", u"Serviços e Preços — Paulo Carvalho", u"Servicios y Precios — Paulo Carvalho")
add("meta.svc.desc", u"Fixed-scope backend engineering: API integrations, legacy Java upgrades, stuck bugs, AI features. Instant quote.",
    u"Engenharia de backend por escopo fechado: integrações de API, atualização de Java legado, bugs travados, recursos de IA. Orçamento na hora.",
    u"Ingeniería de backend con alcance cerrado: integraciones de API, actualización de Java heredado, bugs atascados, funciones de IA. Presupuesto al instante.")

# ---------------------------------------------------------------- lang picker
add("lang.aria", u"Language", u"Idioma", u"Idioma")
