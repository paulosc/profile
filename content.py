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

add("work.sopede.h", u"SôPede", u"SôPede", u"SôPede")
add("work.sopede.meta", u"Own product &middot; in production", u"Produto próprio &middot; em produção", u"Producto propio &middot; en producción")
add("work.sopede.p1",
    u"An ordering platform for restaurants: a digital menu customers order from, and a kitchen-side order manager that runs on a screen in the kitchen and moves each order through preparation.",
    u"Uma plataforma de pedidos para restaurantes: um cardápio digital por onde o cliente pede, e um gestor de pedidos que roda numa tela na cozinha e move cada pedido pelo preparo.",
    u"Una plataforma de pedidos para restaurantes: una carta digital desde la que el cliente pide, y un gestor de pedidos que corre en una pantalla en la cocina y mueve cada pedido por la preparación.")
add("work.sopede.p2",
    u"The hard part was never the menu. It was keeping the kitchen screen, the customer&rsquo;s phone and the storefront agreeing about the same order at the same moment, on restaurant wifi that drops.",
    u"A parte difícil nunca foi o cardápio. Foi manter a tela da cozinha, o celular do cliente e a loja concordando sobre o mesmo pedido no mesmo instante, num wi-fi de restaurante que cai.",
    u"La parte difícil nunca fue la carta. Fue mantener la pantalla de la cocina, el móvil del cliente y la tienda de acuerdo sobre el mismo pedido en el mismo instante, en un wifi de restaurante que se cae.")

add("work.arena.h", u"Arena", u"Arena", u"Arena")
add("work.arena.meta", u"Own product &middot; live on Google Play", u"Produto próprio &middot; publicado na Google Play", u"Producto propio &middot; publicado en Google Play")
add("work.arena.p1",
    u"Management software for martial arts and sports academies, built around the two things that quietly drain a small academy: unpaid monthly fees and students who stop showing up without anyone noticing.",
    u"Software de gestão para academias de artes marciais e esportes, construído em torno das duas coisas que drenam uma academia pequena em silêncio: mensalidade atrasada e aluno que some sem ninguém perceber.",
    u"Software de gestión para academias de artes marciales y deportes, construido alrededor de las dos cosas que desangran en silencio a una academia pequeña: la mensualidad impagada y el alumno que deja de venir sin que nadie lo note.")
add("work.arena.p2",
    u"Recurring billing over PIX and card through a licensed payment institution, QR-code attendance, belt and grade progression with configurable rules, and a churn alert that fires before the student is gone for good. Revenue is a percentage of what actually gets collected, which makes the payment pipeline the part that must never quietly fail.",
    u"Cobrança recorrente por PIX e cartão através de uma instituição de pagamento autorizada, presença por QR code, progressão de faixas e graus com regras configuráveis, e um alerta de evasão que dispara antes do aluno sumir de vez. A receita é um percentual do que é efetivamente recebido, o que torna a esteira de pagamento a parte que não pode falhar em silêncio.",
    u"Cobro recurrente por PIX y tarjeta a través de una entidad de pago autorizada, asistencia por código QR, progresión de cinturones y grados con reglas configurables, y una alerta de abandono que salta antes de que el alumno se vaya del todo. Los ingresos son un porcentaje de lo efectivamente cobrado, lo que convierte la pasarela de pago en la parte que no puede fallar en silencio.")

add("work.cidade.h", u"Cidade Cidad\u00e3", u"Cidade Cidad\u00e3", u"Cidade Cidad\u00e3")
add("work.cidade.meta", u"Own product &middot; civic tech &middot; Google Play",
    u"Produto pr\u00f3prio &middot; govtech &middot; Google Play",
    u"Producto propio &middot; govtech &middot; Google Play")
add("work.cidade.p1",
    u"A channel between a citizen and their city hall. Residents report a pothole, a dead streetlight or an illegal dump with a photo and a GPS pin, get a protocol number, and follow it until somebody closes it with photographic evidence.",
    u"Um canal entre o cidad\u00e3o e a prefeitura. O morador reporta um buraco, uma l\u00e2mpada queimada ou um descarte irregular com foto e ponto no GPS, recebe um n\u00famero de protocolo e acompanha at\u00e9 algu\u00e9m encerrar com foto de evid\u00eancia.",
    u"Un canal entre el ciudadano y su ayuntamiento. El vecino reporta un bache, una farola apagada o un vertido con foto y punto GPS, recibe un n\u00famero de expediente y lo sigue hasta que alguien lo cierra con prueba fotogr\u00e1fica.")
add("work.cidade.p2",
    u"Two constraints shaped the build. Faces and licence plates are blurred automatically before a photo is ever stored, because a public complaint feed is not allowed to become surveillance. And near-duplicate reports are detected at the same location, or the same pothole arrives fifty times and the queue becomes useless to the people who have to work it.",
    u"Duas restri\u00e7\u00f5es moldaram a constru\u00e7\u00e3o. Rostos e placas s\u00e3o desfocados automaticamente antes de a foto ser armazenada, porque um mural p\u00fablico de reclama\u00e7\u00f5es n\u00e3o pode virar vigil\u00e2ncia. E reclama\u00e7\u00f5es quase id\u00eanticas s\u00e3o detectadas no mesmo local, ou o mesmo buraco chega cinquenta vezes e a fila deixa de servir para quem precisa trabalhar nela.",
    u"Dos restricciones marcaron la construcci\u00f3n. Las caras y las matr\u00edculas se difuminan autom\u00e1ticamente antes de guardar la foto, porque un muro p\u00fablico de quejas no puede convertirse en vigilancia. Y se detectan reportes casi id\u00e9nticos en la misma ubicaci\u00f3n, o el mismo bache llega cincuenta veces y la cola deja de servir a quien tiene que trabajarla.")

add("work.rafael.h", u"Rafael IA", u"Rafael IA", u"Rafael IA")
add("work.rafael.meta", u"Own product &middot; LLM assistant &middot; Google Play",
    u"Produto pr\u00f3prio &middot; assistente com IA &middot; Google Play",
    u"Producto propio &middot; asistente con IA &middot; Google Play")
add("work.rafael.p1",
    u"An assistant for the building site, aimed at bricklayers, foremen and site engineers rather than at office staff. It answers the questions that actually come up with a bag of cement in hand: how many blocks per square metre, what concrete mix, how much rebar, what a slab will cost.",
    u"Um assistente para o canteiro de obras, feito para pedreiro, mestre de obras e engenheiro de campo, n\u00e3o para quem est\u00e1 no escrit\u00f3rio. Responde as perguntas que aparecem de verdade com o saco de cimento na m\u00e3o: quantos blocos por metro quadrado, qual o tra\u00e7o do concreto, quanta ferragem, quanto sai a laje.",
    u"Un asistente para la obra, pensado para alba\u00f1iles, capataces e ingenieros de campo, no para la oficina. Responde las preguntas que surgen de verdad con el saco de cemento en la mano: cu\u00e1ntos bloques por metro cuadrado, qu\u00e9 dosificaci\u00f3n de hormig\u00f3n, cu\u00e1nta armadura, cu\u00e1nto cuesta una losa.")
add("work.rafael.p2",
    u"The engineering problem is not the chat window. It is keeping the numbers right: a language model that improvises a concrete mix is worse than no app at all, so the calculations are constrained rather than generated freely.",
    u"O problema de engenharia n\u00e3o \u00e9 a janela de conversa. \u00c9 manter os n\u00fameros corretos: um modelo de linguagem que improvisa tra\u00e7o de concreto \u00e9 pior do que n\u00e3o ter aplicativo nenhum, ent\u00e3o os c\u00e1lculos s\u00e3o restringidos, e n\u00e3o gerados livremente.",
    u"El problema de ingenier\u00eda no es la ventana de chat. Es mantener los n\u00fameros correctos: un modelo de lenguaje que improvisa una dosificaci\u00f3n de hormig\u00f3n es peor que no tener app, as\u00ed que los c\u00e1lculos est\u00e1n acotados, no generados libremente.")

# ---- compact strip -------------------------------------------------------
add("also.label", u"Also shipped", u"Tamb\u00e9m publicado", u"Tambi\u00e9n publicado")
add("also.h2", u"Smaller things, and one I helped build.",
    u"Coisas menores, e uma que ajudei a construir.",
    u"Cosas m\u00e1s peque\u00f1as, y una que ayud\u00e9 a construir.")
add("also.gato.h", u"Gato X Telhado", u"Gato X Telhado", u"Gato X Telhado")
add("also.gato.p", u"A reflex arcade game on Google Play, wired into Play Games global leaderboards. Built mostly to keep the mobile release pipeline sharp.",
    u"Um jogo arcade de reflexo na Google Play, ligado aos placares globais do Play Games. Feito sobretudo para manter a esteira de publica\u00e7\u00e3o mobile afiada.",
    u"Un juego arcade de reflejos en Google Play, conectado a las clasificaciones globales de Play Games. Hecho sobre todo para mantener afinado el proceso de publicaci\u00f3n m\u00f3vil.")
add("also.kuak.h", u"Kuak", u"Kuak", u"Kuak")
add("also.kuak.p", u"A platform where influencers and brands find each other, with social metrics pulled in and refreshed automatically. I contributed to this one rather than owning it.",
    u"Uma plataforma onde influenciadores e marcas se encontram, com m\u00e9tricas das redes sociais puxadas e atualizadas automaticamente. Nesta eu participei, n\u00e3o \u00e9 produto meu.",
    u"Una plataforma donde influencers y marcas se encuentran, con m\u00e9tricas sociales importadas y actualizadas autom\u00e1ticamente. En esta particip\u00e9, no es producto m\u00edo.")
add("also.flowlyx", u"My products are published under Flowlyx, my own software studio.",
    u"Meus produtos s\u00e3o publicados sob a Flowlyx, meu est\u00fadio de software.",
    u"Mis productos se publican bajo Flowlyx, mi propio estudio de software.")

add("work.visit", u"Visit the site &rarr;", u"Ver o site &rarr;", u"Ver el sitio &rarr;")

# ---------------------------------------------------------------- AI section
add("aisec.label", u"AI in production", u"IA em produ\u00e7\u00e3o", u"IA en producci\u00f3n")
add("aisec.h2", u"Anyone can call the API. The hard part comes after.",
    u"Chamar a API qualquer um chama. A parte dif\u00edcil vem depois.",
    u"Llamar a la API la llama cualquiera. La parte dif\u00edcil viene despu\u00e9s.")
add("aisec.intro",
    u"A demo takes an afternoon. Keeping a language model useful once real users are hitting it &mdash; with costs that do not spiral, answers you can trust, and a way to know when a change made things worse &mdash; is a different job, and it is the one I do.",
    u"Uma demo sai numa tarde. Manter um modelo de linguagem \u00fatil depois que usu\u00e1rio de verdade come\u00e7a a bater nele &mdash; com custo que n\u00e3o dispara, resposta em que d\u00e1 para confiar, e um jeito de saber quando uma mudan\u00e7a piorou tudo &mdash; \u00e9 outro trabalho, e \u00e9 esse que eu fa\u00e7o.",
    u"Una demo sale en una tarde. Mantener un modelo de lenguaje \u00fatil una vez que los usuarios reales lo golpean &mdash; con costes que no se disparan, respuestas fiables y una forma de saber cu\u00e1ndo un cambio empeor\u00f3 las cosas &mdash; es otro trabajo, y es el que hago yo.")

add("aisec.ship.h", u"LLM products, shipped", u"Produtos com LLM, publicados", u"Productos con LLM, publicados")
add("aisec.ship.p",
    u"Rafael IA is on Google Play: an assistant that answers construction-site questions and runs the material calculations behind them. I also built a nutrition assistant on Gemini that reads a photo of a meal and returns its nutritional breakdown, and transcribes a spoken description when the user would rather talk than type.",
    u"O Rafael IA est\u00e1 na Google Play: um assistente que responde d\u00favidas de obra e roda os c\u00e1lculos de material por tr\u00e1s delas. Tamb\u00e9m constru\u00ed um assistente de nutri\u00e7\u00e3o sobre o Gemini que l\u00ea a foto de uma refei\u00e7\u00e3o e devolve a composi\u00e7\u00e3o nutricional, e transcreve a descri\u00e7\u00e3o falada quando o usu\u00e1rio prefere falar a digitar.",
    u"Rafael IA est\u00e1 en Google Play: un asistente que responde dudas de obra y ejecuta los c\u00e1lculos de material detr\u00e1s de ellas. Tambi\u00e9n constru\u00ed un asistente de nutrici\u00f3n sobre Gemini que lee la foto de una comida y devuelve su composici\u00f3n nutricional, y transcribe la descripci\u00f3n hablada cuando el usuario prefiere hablar a escribir.")

add("aisec.trust.h", u"Guardrails where the answer must be right",
    u"Trava onde a resposta precisa estar certa",
    u"L\u00edmites donde la respuesta debe ser correcta")
add("aisec.trust.p",
    u"A model that improvises a concrete mix is worse than no app at all. So in Rafael IA the arithmetic is constrained rather than generated: the model handles the conversation, deterministic code handles the numbers. Knowing which half is which is most of the design work.",
    u"Um modelo que improvisa tra\u00e7o de concreto \u00e9 pior do que n\u00e3o ter aplicativo. Ent\u00e3o no Rafael IA a conta \u00e9 restringida, e n\u00e3o gerada: o modelo cuida da conversa, c\u00f3digo determin\u00edstico cuida dos n\u00fameros. Saber qual metade \u00e9 qual \u00e9 a maior parte do projeto.",
    u"Un modelo que improvisa una dosificaci\u00f3n de hormig\u00f3n es peor que no tener app. Por eso en Rafael IA la aritm\u00e9tica est\u00e1 acotada, no generada: el modelo lleva la conversaci\u00f3n, el c\u00f3digo determinista lleva los n\u00fameros. Saber qu\u00e9 mitad es cu\u00e1l es la mayor parte del dise\u00f1o.")

add("aisec.measure.h", u"Measured, not vibed", u"Medido, n\u00e3o no feeling", u"Medido, no a ojo")
add("aisec.measure.p",
    u"Prompts under version control, structured output the application can actually rely on, cost tracked per request, and an eval set that tells me when a prompt change made accuracy worse instead of better. Without that last one you are not improving a system, you are redecorating it.",
    u"Prompts sob controle de vers\u00e3o, sa\u00edda estruturada em que a aplica\u00e7\u00e3o realmente pode confiar, custo medido por requisi\u00e7\u00e3o, e um conjunto de eval que me diz quando uma mudan\u00e7a de prompt piorou a acur\u00e1cia em vez de melhorar. Sem esse \u00faltimo voc\u00ea n\u00e3o est\u00e1 melhorando um sistema, est\u00e1 redecorando.",
    u"Prompts bajo control de versiones, salida estructurada en la que la aplicaci\u00f3n puede confiar de verdad, coste medido por solicitud, y un conjunto de evaluaci\u00f3n que me dice cu\u00e1ndo un cambio de prompt empeor\u00f3 la precisi\u00f3n en vez de mejorarla. Sin esto \u00faltimo no est\u00e1s mejorando un sistema, lo est\u00e1s redecorando.")

add("aisec.vision.h", u"Vision, and knowing when not to store something",
    u"Vis\u00e3o computacional, e saber quando n\u00e3o guardar algo",
    u"Visi\u00f3n, y saber cu\u00e1ndo no guardar algo")
add("aisec.vision.p",
    u"In Cidade Cidad\u00e3, every photo of a street problem passes through automatic blurring of faces and licence plates before it is ever written to storage. A public complaint feed that quietly becomes a surveillance archive is a failure of engineering, not of policy.",
    u"No Cidade Cidad\u00e3, toda foto de problema urbano passa por desfoque autom\u00e1tico de rostos e placas antes de ser gravada. Um mural p\u00fablico de reclama\u00e7\u00f5es que silenciosamente vira arquivo de vigil\u00e2ncia \u00e9 falha de engenharia, n\u00e3o de pol\u00edtica.",
    u"En Cidade Cidad\u00e3, cada foto de un problema urbano pasa por un difuminado autom\u00e1tico de caras y matr\u00edculas antes de guardarse. Un muro p\u00fablico de quejas que en silencio se convierte en un archivo de vigilancia es un fallo de ingenier\u00eda, no de pol\u00edtica.")

add("aisec.claude.h", u"Claude in the daily loop", u"Claude no dia a dia", u"Claude en el d\u00eda a d\u00eda")
add("aisec.claude.p",
    u"I work with Claude Code every day, and it is the reason I can quote a fixed price and mean it. This site &mdash; three languages, a quote configurator, a build pipeline &mdash; was built that way. It does not replace knowing what the code should do; it removes the hours between deciding and having it.",
    u"Trabalho com o Claude Code todos os dias, e \u00e9 por isso que consigo fechar pre\u00e7o fixo e cumprir. Este site &mdash; tr\u00eas idiomas, um configurador de or\u00e7amento, uma esteira de build &mdash; foi feito assim. N\u00e3o substitui saber o que o c\u00f3digo deve fazer; elimina as horas entre decidir e ter pronto.",
    u"Trabajo con Claude Code a diario, y por eso puedo cerrar un precio fijo y cumplirlo. Este sitio &mdash; tres idiomas, un configurador de presupuesto, un pipeline de build &mdash; se hizo as\u00ed. No sustituye saber qu\u00e9 debe hacer el c\u00f3digo; elimina las horas entre decidirlo y tenerlo.")

add("aisec.providers.h", u"Providers", u"Fornecedores", u"Proveedores")
add("aisec.providers.p",
    u"Claude, Gemini and OpenAI. I build the provider behind an interface so swapping one out is a configuration change, not a rewrite &mdash; the pricing and the leaderboard both move too fast to marry any of them.",
    u"Claude, Gemini e OpenAI. Deixo o fornecedor atr\u00e1s de uma interface para que trocar seja mudan\u00e7a de configura\u00e7\u00e3o, e n\u00e3o reescrita &mdash; o pre\u00e7o e o ranking mudam r\u00e1pido demais para casar com algum deles.",
    u"Claude, Gemini y OpenAI. Dejo al proveedor detr\u00e1s de una interfaz para que cambiarlo sea una modificaci\u00f3n de configuraci\u00f3n, no una reescritura &mdash; el precio y el ranking cambian demasiado r\u00e1pido como para casarse con ninguno.")

add("nav.ai", u"AI", u"IA", u"IA")

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
add("q.sent.h", u"Brief copied to your clipboard.", u"Briefing copiado para a sua \u00e1rea de transfer\u00eancia.", u"Briefing copiado a tu portapapeles.")
add("q.sent.p", u"Pick how you would rather send it &mdash; the text is already copied either way.",
    u"Escolha por onde prefere enviar &mdash; o texto j\u00e1 est\u00e1 copiado de qualquer forma.",
    u"Elige por d\u00f3nde prefieres enviarlo &mdash; el texto ya est\u00e1 copiado igualmente.")
add("q.sent.gmail", u"Open in Gmail", u"Abrir no Gmail", u"Abrir en Gmail")
add("q.sent.mail", u"Open mail app", u"Abrir app de e-mail", u"Abrir app de correo")
add("q.sent.whats", u"Send on WhatsApp", u"Enviar no WhatsApp", u"Enviar por WhatsApp")
add("q.sent.manual", u"Or paste it into an email to", u"Ou cole em um e-mail para", u"O p\u00e9galo en un correo a")
add("q.sent.close", u"Close", u"Fechar", u"Cerrar")

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
