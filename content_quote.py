# -*- coding: utf-8 -*-
"""Translations for the quote configurator.

Paths mirror the SERVICES object in quote.js: "<service>.name",
"<service>.<group>.label", "<service>.<group>.<option>.t" and ".d".
English lives in quote.js itself and is the fallback, so a missing key here
degrades to English instead of blanking out.
"""

Q = {"pt": {}, "es": {}}


def q(path, pt, es):
    Q["pt"][path] = pt
    Q["es"][path] = es


# ------------------------------------------------------------------- api
q("api.name", u"Integração de API de terceiros", u"Integración de API de terceros")
q("api.endpoints.label", u"Quantos endpoints?", u"¿Cuántos endpoints?")
q("api.endpoints.1-3.t", u"1 a 3 endpoints", u"1 a 3 endpoints")
q("api.endpoints.1-3.d", u"Uma integração pontual", u"Una integración puntual")
q("api.endpoints.4-8.t", u"4 a 8 endpoints", u"4 a 8 endpoints")
q("api.endpoints.4-8.d", u"Uma funcionalidade inteira", u"Una funcionalidad completa")
q("api.endpoints.9+.t", u"9 ou mais", u"9 o más")
q("api.endpoints.9+.d", u"API inteira coberta", u"API completa cubierta")
q("api.auth.label", u"Autenticação", u"Autenticación")
q("api.auth.key.t", u"Chave de API ou token", u"Clave de API o token")
q("api.auth.key.d", u"Direto ao ponto", u"Directo")
q("api.auth.oauth.t", u"OAuth2 / OIDC", u"OAuth2 / OIDC")
q("api.auth.oauth.d", u"Refresh, expiração, escopos", u"Refresh, expiración, scopes")
q("api.auth.custom.t", u"Customizada ou sem documentação", u"Personalizada o sin documentación")
q("api.auth.custom.d", u"Eu descubro pelas respostas reais da API", u"La deduzco de las respuestas reales de la API")
q("api.extras.label", u"Adicionais", u"Adicionales")
q("api.extras.hooks.t", u"Webhooks de entrada", u"Webhooks entrantes")
q("api.extras.hooks.d", u"Verificação de assinatura e idempotência", u"Verificación de firma e idempotencia")
q("api.extras.docs.t", u"Documentação escrita", u"Documentación escrita")
q("api.extras.docs.d", u"Como rodar e o que quebra", u"Cómo ejecutarlo y qué lo rompe")
q("api.extras.monitor.t", u"Alerta de falha", u"Alerta de fallo")
q("api.extras.monitor.d", u"Você fica sabendo antes dos seus usuários", u"Te enteras antes que tus usuarios")

# --------------------------------------------------------------- upgrade
q("upgrade.name", u"Atualização de Java e Spring legado", u"Actualización de Java y Spring heredado")
q("upgrade.jump.label", u"Qual o tamanho do salto?", u"¿De qué tamaño es el salto?")
q("upgrade.jump.minor.t", u"Subir versão menor", u"Subir versión menor")
q("upgrade.jump.minor.d", u"Mesma linha principal", u"Misma línea principal")
q("upgrade.jump.java.t", u"Java 8 ou 11 → 17 / 21", u"Java 8 u 11 → 17 / 21")
q("upgrade.jump.java.d", u"Migração de linguagem e JVM", u"Migración de lenguaje y JVM")
q("upgrade.jump.boot.t", u"Spring Boot 2 → 3", u"Spring Boot 2 → 3")
q("upgrade.jump.boot.d", u"Inclui a migração javax → jakarta", u"Incluye la migración javax → jakarta")
q("upgrade.size.label", u"Tamanho do projeto", u"Tamaño del proyecto")
q("upgrade.size.s.t", u"Menos de 50 arquivos", u"Menos de 50 archivos")
q("upgrade.size.m.t", u"50 a 200 arquivos", u"50 a 200 archivos")
q("upgrade.size.l.t", u"Mais de 200 arquivos", u"Más de 200 archivos")
q("upgrade.tests.label", u"Tem testes hoje?", u"¿Tiene pruebas hoy?")
q("upgrade.tests.yes.t", u"Sim, e passam", u"Sí, y pasan")
q("upgrade.tests.yes.d", u"São eles que provam que nada mudou", u"Son los que prueban que nada cambió")
q("upgrade.tests.some.t", u"Alguns, parcialmente quebrados", u"Algunas, parcialmente rotas")
q("upgrade.tests.some.d", u"Conserto o necessário para verificar", u"Arreglo lo necesario para verificar")
q("upgrade.tests.no.t", u"Nenhum", u"Ninguna")
q("upgrade.tests.no.d", u"Crio uma rede de segurança nos caminhos críticos antes", u"Creo una red de seguridad en las rutas críticas antes")
q("upgrade.extras.label", u"Adicionais", u"Adicionales")
q("upgrade.extras.ci.t", u"Pipeline de CI configurado", u"Pipeline de CI configurado")
q("upgrade.extras.ci.d", u"Build, teste e deploy a cada push", u"Build, prueba y despliegue en cada push")
q("upgrade.extras.cve.t", u"Dependências vulneráveis substituídas", u"Dependencias vulnerables sustituidas")
q("upgrade.extras.cve.d", u"Auditoria e correção", u"Auditoría y corrección")

# ------------------------------------------------------------------- bug
q("bug.name", u"Achar e corrigir um bug travado", u"Encontrar y corregir un bug atascado")
q("bug.kind.label", u"Como ele se comporta?", u"¿Cómo se comporta?")
q("bug.kind.repro.t", u"Reproduzível sempre", u"Reproducible siempre")
q("bug.kind.repro.d", u"Falha do mesmo jeito toda vez", u"Falla igual cada vez")
q("bug.kind.inter.t", u"Intermitente", u"Intermitente")
q("bug.kind.inter.d", u"Uma vez a cada N requisições, sem gatilho claro", u"Una vez cada N solicitudes, sin disparador claro")
q("bug.kind.prod.t", u"Só em produção", u"Solo en producción")
q("bug.kind.prod.d", u"Funciona em staging — o tipo caro", u"Funciona en staging — el tipo caro")
q("bug.extras.label", u"Adicionais", u"Adicionales")
q("bug.extras.post.t", u"Post-mortem escrito", u"Post-mortem escrito")
q("bug.extras.post.d", u"Causa raiz e como evitar essa classe de bug", u"Causa raíz y cómo evitar esa clase de bug")
q("bug.extras.audit.t", u"Varredura do mesmo padrão no resto do código", u"Barrido del mismo patrón en el resto del código")
q("bug.extras.audit.d", u"Quase sempre existe mais de um", u"Casi siempre hay más de uno")

# -------------------------------------------------------------------- ai
q("ai.name", u"Recurso de IA em um produto existente", u"Función de IA en un producto existente")
q("ai.kind.label", u"O que ele deve fazer?", u"¿Qué debe hacer?")
q("ai.kind.extract.t", u"Extrair ou classificar", u"Extraer o clasificar")
q("ai.kind.extract.d", u"Dados estruturados a partir de documentos ou texto", u"Datos estructurados a partir de documentos o texto")
q("ai.kind.rag.t", u"Responder perguntas sobre seus dados", u"Responder preguntas sobre tus datos")
q("ai.kind.rag.d", u"Retrieval com trabalho real de relevância", u"Retrieval con trabajo real de relevancia")
q("ai.kind.agent.t", u"Executar ações nos seus sistemas", u"Ejecutar acciones en tus sistemas")
q("ai.kind.agent.d", u"Uso de ferramentas, com travas de segurança", u"Uso de herramientas, con salvaguardas")
q("ai.extras.label", u"Adicionais", u"Adicionales")
q("ai.extras.eval.t", u"Suíte de avaliação", u"Suíte de evaluación")
q("ai.extras.eval.d", u"Acurácia medida, para regressão ficar visível", u"Precisión medida, para que la regresión sea visible")
q("ai.extras.deploy.t", u"Deploy e monitoramento", u"Despliegue y monitorización")
q("ai.extras.deploy.d", u"Tracing e relatório de custo por requisição", u"Tracing e informe de coste por solicitud")
q("ai.extras.multi.t", u"Independente de fornecedor", u"Independiente del proveedor")
q("ai.extras.multi.d", u"Trocar de modelo sem reescrever", u"Cambiar de modelo sin reescribir")

# ------------------------------------------------------------------ data
q("data.name", u"Scraper e pipeline agendado", u"Scraper y pipeline programado")
q("data.sources.label", u"Quantas fontes?", u"¿Cuántas fuentes?")
q("data.sources.1.t", u"Um site ou API", u"Un sitio o API")
q("data.sources.2-5.t", u"De duas a cinco", u"De dos a cinco")
q("data.sources.6+.t", u"Seis ou mais", u"Seis o más")
q("data.extras.label", u"Adicionais", u"Adicionales")
q("data.extras.sched.t", u"Agendamento e alerta de mudança", u"Programación y alerta de cambios")
q("data.extras.sched.d", u"Você é avisado quando a fonte muda de layout", u"Te avisa cuando la fuente cambia de estructura")
q("data.extras.dash.t", u"Painel", u"Panel")
q("data.extras.dash.d", u"Navegar e exportar os dados", u"Navegar y exportar los datos")

# ------------------------------------------------------------------ cicd
q("cicd.name", u"Pipeline de CI/CD do zero", u"Pipeline de CI/CD desde cero")
q("cicd.envs.label", u"Ambientes", u"Entornos")
q("cicd.envs.1.t", u"Um", u"Uno")
q("cicd.envs.1.d", u"Só produção", u"Solo producción")
q("cicd.envs.2-3.t", u"Dois ou três", u"Dos o tres")
q("cicd.envs.2-3.d", u"Staging e produção", u"Staging y producción")
q("cicd.envs.4+.t", u"Quatro ou mais", u"Cuatro o más")
q("cicd.extras.label", u"Adicionais", u"Adicionales")
q("cicd.extras.iac.t", u"Infraestrutura como código", u"Infraestructura como código")
q("cicd.extras.iac.d", u"Terraform — ambientes viram reproduzíveis", u"Terraform — los entornos se vuelven reproducibles")
q("cicd.extras.rb.t", u"Rollback automatizado", u"Rollback automatizado")
q("cicd.extras.rb.d", u"Um comando de volta para o último build bom", u"Un comando para volver al último build correcto")

# ---------------------------------------------------------------- review
q("review.name", u"Revisão de arquitetura", u"Revisión de arquitectura")
q("review.depth.label", u"Qual profundidade?", u"¿Qué profundidad?")
q("review.depth.survey.t", u"Panorâmica", u"Panorámica")
q("review.depth.survey.d", u"Estrutura, riscos e ganhos rápidos", u"Estructura, riesgos y mejoras rápidas")
q("review.depth.deep.t", u"Revisão profunda", u"Revisión profunda")
q("review.depth.deep.d", u"Modelo de dados, fronteiras, limites de escala, custo", u"Modelo de datos, fronteras, límites de escala, coste")
q("review.extras.label", u"Adicionais", u"Adicionales")
q("review.extras.exec.t", u"Resumo executivo", u"Resumen ejecutivo")
q("review.extras.exec.d", u"Uma página que sua diretoria vai realmente ler", u"Una página que tu directiva sí va a leer")
q("review.extras.road.t", u"Plano de correção priorizado", u"Plan de corrección priorizado")
q("review.extras.road.d", u"Sequenciado, com estimativa de esforço", u"Secuenciado, con estimación de esfuerzo")

# ------------------------------------------------------------ brief text
q("brief.title", u"BRIEFING DO PROJETO", u"BRIEFING DEL PROYECTO")
q("brief.service", u"Serviço", u"Servicio")
q("brief.scope", u"Escopo selecionado", u"Alcance seleccionado")
q("brief.rush", u"Entrega acelerada solicitada", u"Entrega acelerada solicitada")
q("brief.price", u"Preço orçado", u"Precio presupuestado")
q("brief.fixed", u"USD (fechado)", u"USD (cerrado)")
q("brief.eta", u"Prazo estimado", u"Plazo estimado")
q("brief.days_from", u"dias a partir do início", u"días desde el inicio")
q("brief.revs", u"Revisões incluídas", u"Revisiones incluidas")
q("brief.please", u"--- Por favor preencha ---", u"--- Por favor completa ---")
q("brief.fields", u"Seu nome / empresa:\nRepositório ou sistema:\nLinguagem e framework:\nQue resultado tornaria isso um sucesso:\nO que já foi tentado:",
  u"Tu nombre / empresa:\nRepositorio o sistema:\nLenguaje y framework:\nQué resultado haría de esto un éxito:\nQué se ha intentado ya:")
q("brief.subject", u"Projeto", u"Proyecto")
