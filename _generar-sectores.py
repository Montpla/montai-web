# -*- coding: utf-8 -*-
"""
Genera las paginas de sector de montai.es (carpeta sectores/).

POR QUE EXISTEN ESTAS PAGINAS
  1) SEO: "IA para clinicas dentales" es mucho menos competido que "automatizar whatsapp negocio".
  2) VENTA: al visitar una clinica dental le mandas una pagina escrita para clinicas dentales,
     no la home generica. Sirve desde el primer dia, sin esperar a posicionar.

ANADIR UN SECTOR NUEVO
  Copia un bloque de SECTORES, cambia los textos y ejecuta:  python _generar-sectores.py
  Luego anade la URL a sitemap.xml y una tarjeta en la seccion "sectores" de index.html.

El CTA de cada sector lleva un mensaje distinto en el enlace de WhatsApp, asi sabes
desde que pagina te ha escrito cada persona.
"""
import io, os, sys, datetime

try: sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception: pass

AQUI = os.path.dirname(os.path.abspath(__file__))
HOY = datetime.date.today().isoformat()
WA = "https://wa.me/34676085750?text="

SECTORES = [
 {
  "slug": "ia-para-clinicas-dentales",
  "cat": "Clínicas dentales",
  "title": "IA para clínicas dentales: menos ausencias | MontAI",
  "desc": "Un asistente de IA atiende el WhatsApp de tu clínica dental: da cita, confirma y recuerda. Menos huecos vacíos y una recepción libre del teléfono.",
  "kw": "IA para clínicas dentales, automatizar citas clínica dental, recordatorios pacientes dentista, chatbot clínica dental, reducir ausencias dentista",
  "h1a": "Cada paciente que no aparece",
  "h1b": "es un sillón vacío que ya no recuperas",
  "sub": "Un asistente de IA atiende el WhatsApp de tu clínica, <strong>da cita, confirma y recuerda</strong> — mientras tu recepción atiende a quien tiene delante.",
  "ctatext": "Hola MontAI, tengo una clínica dental y quiero automatizar las citas",
  "chat": [
    ("me","Hola, ¿tenéis hueco esta semana para una limpieza?","18:42"),
    ("bot","¡Hola! Sí 😊 Para higiene dental tengo estos huecos:", "18:42",
     ["1️⃣ Jueves 3 · 10:00","2️⃣ Jueves 3 · 17:30","3️⃣ Viernes 4 · 09:30"]),
    ("me","El jueves a las 17:30","18:43"),
    ("bot","Perfecto. ¿Me dices tu nombre y un teléfono de contacto y te la confirmo?","18:43"),
  ],
  "pains": [
    ("🪑","Las ausencias te dejan el sillón parado",
     "El paciente que no avisa te deja un hueco que ya no rellenas con dos horas de margen. Es la pérdida más silenciosa de una clínica.",
     "El sistema confirma y recuerda la cita el día antes"),
    ("☎️","Tu recepción vive al teléfono",
     "Mientras coge llamadas para dar hora, hay un paciente esperando en el mostrador. Las dos cosas se hacen peor.",
     "Las citas por WhatsApp se dan solas, sin descolgar"),
    ("🌙","Preguntan por la tarde-noche y contestas al día siguiente",
     "Quien busca dentista pregunta en dos o tres sitios. El que contesta primero se queda al paciente.",
     "Respuesta en segundos, también a las 23:00"),
  ],
  "servicios": [
    ("📅","Da cita y la confirma","Ofrece los huecos que tengas libres, reserva y confirma al momento. Se sincroniza con vuestra agenda para no pisar ninguna cita."),
    ("🔔","Recuerda la cita el día antes","El recordatorio automático es lo que más reduce las ausencias. Sin que nadie tenga que llamar uno por uno."),
    ("💬","Resuelve las dudas de siempre","Horarios, si trabajáis con su seguro, qué incluye una primera visita, dónde aparcar. Con la información real de tu clínica."),
    ("🧑‍⚕️","Sabe cuándo pasar la conversación","Ante una urgencia o una consulta clínica, deriva a una persona del equipo con el contexto ya resumido. No improvisa diagnósticos."),
  ],
  "faq": [
    ("¿El paciente notará que habla con una IA?",
     "No lo escondemos, pero tampoco lo disfrazamos de persona. Se presenta como el asistente de la clínica y resuelve en segundos. En cuanto la conversación es clínica o delicada, se la pasa a tu equipo."),
    ("¿Puede dar consejos médicos por su cuenta?",
     "No, y está configurado explícitamente para no hacerlo. Gestiona agenda e información práctica. Cualquier cosa clínica la deriva a un profesional."),
    ("¿Se conecta con el software que ya usamos?",
     "Se conecta con Google Calendar y con la mayoría de sistemas que tengan API. En el diagnóstico gratuito miramos el vuestro en concreto y te decimos si encaja."),
    ("¿Qué pasa con los datos de los pacientes?",
     "Se tratan conforme al RGPD, con finalidad clara y borrado a petición. No se comparten ni se venden. Puedes leer el detalle en nuestra <a href=\"/privacidad.html\" style=\"color:var(--gold);text-decoration:underline\">política de privacidad</a>."),
  ],
  "cierre": "Menos huecos vacíos en tu agenda",
  "cierresub": "En 30 minutos miramos cómo lleváis hoy las citas y te decimos si automatizarlo compensa en vuestro caso. Si no lo vemos claro, te lo diremos.",
 },
 {
  "slug": "ia-para-peluquerias-y-estetica",
  "cat": "Peluquerías y estética",
  "title": "IA para peluquerías y estética: citas automáticas | MontAI",
  "desc": "Un asistente de IA contesta el WhatsApp de tu peluquería y da cita mientras trabajas. Sin parar lo que haces y sin perder clientas por no contestar.",
  "kw": "IA para peluquerías, automatizar citas peluquería, chatbot centro de estética, reservas peluquería whatsapp, agenda automática estética",
  "h1a": "No puedes coger el móvil",
  "h1b": "con las manos en un tinte",
  "sub": "Un asistente de IA contesta tu WhatsApp y <strong>da cita mientras tú trabajas</strong>. Tus clientas reservan solas, tú no sueltas lo que estás haciendo.",
  "ctatext": "Hola MontAI, tengo una peluquería y quiero automatizar las citas",
  "chat": [
    ("me","Hola! quiero corte y color para el sábado","11:20"),
    ("bot","¡Hola! 😊 Para corte y color reservo 2 horas. El sábado me quedan:", "11:20",
     ["1️⃣ Sábado · 10:00","2️⃣ Sábado · 12:30","3️⃣ Sábado · 16:00"]),
    ("me","La de las 12:30","11:21"),
    ("bot","Genial. Dime tu nombre y te la dejo apuntada 💇","11:21"),
  ],
  "pains": [
    ("✂️","Suena el móvil y tienes las manos ocupadas",
     "O paras lo que estás haciendo, o esa clienta se queda sin respuesta. Las dos opciones te cuestan dinero.",
     "El asistente contesta y da cita sin que pares"),
    ("📭","Los huecos que se quedan sin cubrir",
     "Una cancelación a media mañana es una hora muerta. Rellenarla exige llamar a gente una por una, y nunca hay tiempo.",
     "Se ofrecen los huecos libres automáticamente"),
    ("🌙","Escriben por la noche, cuando ya has cerrado",
     "Mucha gente pide cita cuando sale de trabajar. Si lo lees al día siguiente, ya han reservado en otro sitio.",
     "Contesta a cualquier hora, también domingos"),
  ],
  "servicios": [
    ("📅","Reserva según el servicio","No es lo mismo un flequillo que unas mechas. El asistente sabe cuánto dura cada servicio y reserva el tiempo correcto en tu agenda."),
    ("🔔","Recuerda la cita el día antes","Menos plantones y menos huecos de última hora, sin que tengas que mandar mensajes a mano."),
    ("💬","Contesta lo de siempre","Precios orientativos, horarios, si hace falta reservar, si trabajáis con o sin cita previa. Con tu información real."),
    ("📇","Guarda a cada clienta","Cada persona que escribe queda registrada con su nombre, su teléfono y lo que pidió. Tu lista de clientas se construye sola."),
  ],
  "faq": [
    ("¿Puede dar precios exactos?",
     "Le configuramos los precios y rangos que tú nos digas. Si algo depende de ver el pelo o el estado previo, lo explica así y ofrece cita de valoración en vez de inventarse una cifra."),
    ("Tengo dos profesionales con agendas distintas. ¿Vale igual?",
     "Sí. Se puede configurar por profesional, por servicio o por cabina, para que no se solapen reservas. Lo vemos en el diagnóstico."),
    ("¿Y si prefiero atender yo algunos mensajes?",
     "Puedes. El asistente lleva lo repetitivo y te pasa a ti lo que quieras filtrar. Tú sigues viendo todas las conversaciones."),
    ("¿Es caro para un salón pequeño?",
     "Cuanto más pequeño es el equipo, más se nota quitarse el trabajo repetitivo. En el diagnóstico gratuito te damos un presupuesto cerrado y, si no compensa, te lo decimos."),
  ],
  "cierre": "Que reservar contigo sea así de fácil",
  "cierresub": "30 minutos y te decimos si en tu salón compensa automatizar las citas. Sin compromiso y sin tecnicismos.",
 },
 {
  "slug": "ia-para-asesorias-y-despachos",
  "cat": "Asesorías y despachos",
  "title": "IA para asesorías: filtra consultas y gana horas | MontAI",
  "desc": "Un asistente de IA atiende el WhatsApp de tu asesoría, resuelve las preguntas de siempre y agenda el resto. Menos interrupciones, más horas facturables.",
  "kw": "IA para asesorías, automatización asesoría fiscal, chatbot despacho profesional, atención al cliente asesoría, automatizar consultas clientes",
  "h1a": "Tu tiempo facturable",
  "h1b": "se va en preguntas que se repiten",
  "sub": "Un asistente de IA atiende las consultas de siempre, <strong>filtra lo que necesita a un profesional</strong> y agenda esa cita. Tú te quedas con el trabajo que se cobra.",
  "ctatext": "Hola MontAI, tengo una asesoría y quiero filtrar y automatizar consultas",
  "chat": [
    ("me","Buenas, ¿qué documentación necesitáis para la renta?","09:15"),
    ("bot","Buenos días 😊 Lo habitual: DNI, certificado de retenciones, datos bancarios y, si hay vivienda, las escrituras o el recibo del IBI.","09:15"),
    ("me","Vale. ¿Y podría ir esta semana a llevarla?","09:16"),
    ("bot","Claro. Estos huecos tengo libres:","09:16",
     ["1️⃣ Miércoles · 11:00","2️⃣ Jueves · 09:30","3️⃣ Jueves · 17:00"]),
  ],
  "pains": [
    ("🔁","Las mismas diez preguntas, todo el año",
     "Qué papeles hacen falta, cuándo vence un plazo, si ya está presentado. Son consultas que no necesitan tu criterio profesional, solo tu tiempo.",
     "Se resuelven solas, con la información de tu despacho"),
    ("📞","En campaña no se puede trabajar",
     "El teléfono no para justo cuando más concentración necesitas. Cada interrupción cuesta mucho más que el minuto que dura.",
     "Filtra y solo te pasa lo que de verdad te necesita"),
    ("🗂️","Consultas que llegan a medias",
     "El cliente escribe sin los datos necesarios y empieza el ida y vuelta. Tres mensajes después sigues sin poder resolver.",
     "Recoge los datos completos antes de pasártelo"),
  ],
  "servicios": [
    ("🧾","Resuelve las consultas frecuentes","Documentación, plazos, horarios, cómo enviar un papel. Configurado con la información real de tu despacho, no con respuestas genéricas."),
    ("🎯","Filtra y prioriza","Distingue lo urgente de lo que puede esperar, y te pasa la conversación con el contexto ya resumido cuando necesita a un profesional."),
    ("📅","Agenda las visitas","Ofrece tus huecos libres y reserva, con recordatorio el día antes. Menos plantones en temporada alta."),
    ("📇","Registra cada consulta","Quién preguntó, qué necesitaba y cuándo. Deja de perderse contexto entre el teléfono, el correo y el WhatsApp."),
  ],
  "faq": [
    ("¿Va a dar asesoramiento fiscal por su cuenta?",
     "No. Está configurado para dar información práctica y de trámite, nunca criterio profesional. Cualquier cosa que implique interpretación se deriva a un profesional del despacho."),
    ("¿Es compatible con el secreto profesional y el RGPD?",
     "Los datos se tratan conforme al RGPD, con finalidad clara y borrado a petición, y no se comparten con terceros. En el diagnóstico revisamos qué información conviene que maneje y cuál no."),
    ("¿Se integra con nuestro gestor documental o CRM?",
     "Con la mayoría de herramientas que tengan API, además de Google Calendar, hojas de cálculo y correo. Si usáis algo poco común, lo miramos antes de comprometernos."),
    ("¿Cuánto tarda en estar funcionando?",
     "Entre 7 y 14 días hábiles en una implantación estándar. El diagnóstico son 30 minutos y puede ser esta misma semana."),
  ],
  "cierre": "Recupera tus horas facturables",
  "cierresub": "En 30 minutos vemos qué consultas se repiten en tu despacho y cuánto tiempo te podrían devolver. Diagnóstico gratuito.",
 },
]

WA_ICON = ('<svg style="display:none"><symbol id="wa-icon" viewBox="0 0 24 24" fill="currentColor">'
 '<path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413z"/>'
 '</symbol></svg>')
LOGO = "https://res.cloudinary.com/djuqqnrjw/image/upload/f_auto,q_auto,h_120/v1782304072/WhatsApp_Image_2026-06-24_at_14.25.05_urryde.jpg"


def q(s):
    from urllib.parse import quote
    return quote(s, safe="")


def chat_html(msgs):
    out = []
    for m in msgs:
        who, txt, hora = m[0], m[1], m[2]
        opts = m[3] if len(m) > 3 else []
        o = "".join('<span class="opt">%s</span>' % x for x in opts)
        out.append('<div class="msg %s">%s%s<span class="t">%s</span></div>' % (who, txt, o, hora))
    return "\n        ".join(out)


def pagina(s):
    url = "https://www.montai.es/sectores/%s.html" % s["slug"]
    cta = WA + q(s["ctatext"])
    pains = "\n".join(
      '<div class="card pain rv"><div class="ic">%s</div><h3>%s</h3><p>%s</p><span class="fix">→ %s</span></div>'
      % p for p in s["pains"])
    servs = "\n".join(
      '<div class="card rv"><div class="ic">%s</div><h3>%s</h3><p>%s</p></div>' % x for x in s["servicios"])
    faqs = "\n".join(
      '<details><summary>%s</summary><div class="body">%s</div></details>' % f for f in s["faq"])
    return f"""<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<title>{s['title']}</title>
<meta name="description" content="{s['desc']}" />
<meta name="keywords" content="{s['kw']}" />
<meta name="author" content="MontAI" />
<meta name="robots" content="index, follow" />
<meta name="theme-color" content="#06070C" />
<link rel="canonical" href="{url}" />
<link rel="icon" href="/favicon.ico" sizes="any" />
<link rel="icon" type="image/png" sizes="32x32" href="/favicon-32.png" />
<link rel="apple-touch-icon" href="/apple-touch-icon.png" />
<link rel="manifest" href="/site.webmanifest" />
<meta property="og:type" content="website" />
<meta property="og:url" content="{url}" />
<meta property="og:title" content="{s['h1a']} {s['h1b']}" />
<meta property="og:description" content="{s['desc']}" />
<meta property="og:image" content="https://www.montai.es/og-image.png" />
<meta property="og:locale" content="es_ES" />
<meta property="og:site_name" content="MontAI" />
<meta name="twitter:card" content="summary_large_image" />
<script type="application/ld+json">
{{"@context":"https://schema.org","@type":"Service",
"name":"{s['cat']} — automatización con IA","serviceType":"{s['cat']}",
"description":"{s['desc']}",
"provider":{{"@type":"ProfessionalService","name":"MontAI","url":"https://www.montai.es"}},
"areaServed":{{"@type":"Country","name":"España"}},
"url":"{url}",
"offers":{{"@type":"Offer","description":"Diagnóstico gratuito","price":"0","priceCurrency":"EUR"}}}}
</script>
<script type="application/ld+json">
{{"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[
{{"@type":"ListItem","position":1,"name":"Inicio","item":"https://www.montai.es/"}},
{{"@type":"ListItem","position":2,"name":"Sectores","item":"https://www.montai.es/#sectores"}},
{{"@type":"ListItem","position":3,"name":"{s['cat']}"}}]}}
</script>
<script type="application/ld+json">
{{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[
{",".join('{"@type":"Question","name":"%s","acceptedAnswer":{"@type":"Answer","text":"%s"}}' % (f[0], f[1].replace('"', "'").replace("<a href='/privacidad.html' style='color:var(--gold);text-decoration:underline'>", "").replace("</a>", "")) for f in s["faq"])}]}}
</script>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/css/montai.css" />
<script defer src="/_vercel/insights/script.js"></script>
<script defer src="/_vercel/speed-insights/script.js"></script>
</head>
<body>

<div class="orbs" aria-hidden="true"><span class="orb a"></span><span class="orb b"></span><span class="orb c"></span></div>
<div class="veil" aria-hidden="true"></div>
{WA_ICON}

<a class="float" href="{cta}" target="_blank" rel="noopener" aria-label="Escribir por WhatsApp">
  <svg><use href="#wa-icon"/></svg></a>

<nav>
  <div class="nav-in">
    <a href="/" aria-label="MontAI, ir al inicio"><img class="logo" src="{LOGO}" alt="MontAI" width="150" height="52" /></a>
    <div class="nav-links">
      <a href="/#servicios">Qué hacemos</a>
      <a href="/#proceso">Cómo trabajamos</a>
      <a href="/#mentoria">Mentoría</a>
      <a href="/#precio">Precio</a>
      <a href="/blog/">Blog</a>
    </div>
    <a class="btn btn-wa btn-sm" href="{cta}" target="_blank" rel="noopener">
      <svg width="15" height="15" fill="#04240f"><use href="#wa-icon"/></svg> Probar gratis</a>
  </div>
</nav>

<header class="hero">
  <div class="wrap hero-grid">
    <div>
      <nav class="micro" style="margin-bottom:16px">
        <a href="/" style="color:var(--tx3)">Inicio</a> <span style="color:var(--tx3)">/</span>
        <span style="color:var(--gold)">{s['cat']}</span>
      </nav>
      <span class="badge"><span class="dot"></span> {s['cat']}</span>
      <h1>{s['h1a']}<br><span class="grad">{s['h1b']}</span></h1>
      <p class="sub">{s['sub']}</p>
      <div class="cta-row">
        <a class="btn btn-wa btn-full" href="{cta}" target="_blank" rel="noopener">
          <svg width="21" height="21" fill="#04240f"><use href="#wa-icon"/></svg> Probar el agente ahora</a>
        <a class="btn btn-gh btn-full" href="#como">Ver cómo funciona →</a>
      </div>
      <p class="micro">No es una demo grabada: es <b>nuestro agente real</b>. Pregúntale lo que quieras.</p>
    </div>
    <div class="phone" role="img" aria-label="Ejemplo de conversación con el agente de MontAI">
      <div class="ph-top"><div class="ph-av">M</div>
        <div><div class="ph-nm">MontAI · Asistente</div><div class="ph-st">en línea</div></div></div>
      <div class="chat">
        {chat_html(s['chat'])}
      </div>
      <p class="ph-foot">Respuesta media: <strong style="color:var(--wa)">3 segundos</strong> · 24 h · 365 días</p>
    </div>
  </div>
</header>

<section>
  <div class="wrap">
    <div class="center"><span class="eyebrow">¿Te suena?</span>
      <h2>Lo que te está costando dinero<br><span class="grad">sin que aparezca en ninguna factura</span></h2></div>
    <div class="g3">
{pains}
    </div>
  </div>
</section>

<hr class="hr">

<section id="como">
  <div class="wrap">
    <div class="center"><span class="eyebrow">Qué hace por ti</span>
      <h2>Un asistente que no duerme,<br><span class="grad">no olvida y no se pone malo</span></h2></div>
    <div class="g2">
{servs}
    </div>
  </div>
</section>

<hr class="hr">

<section>
  <div class="wrap">
    <div class="center"><span class="eyebrow">Cómo trabajamos</span>
      <h2>De la primera llamada<br><span class="grad">a funcionando en 2 semanas</span></h2></div>
    <div class="steps">
      <div class="step rv"><h3>Diagnóstico gratuito</h3>
        <p>30 minutos. Miramos cómo trabajáis hoy y qué se puede quitar de en medio. Si no compensa, te lo decimos.</p>
        <span class="when">Día 1 · Gratis</span></div>
      <div class="step rv"><h3>Lo montamos y lo entrenamos</h3>
        <p>Configuramos el asistente con vuestra información real: servicios, horarios, precios y tono. Lo conectamos a vuestras herramientas.</p>
        <span class="when">Días 2-14</span></div>
      <div class="step rv"><h3>Funciona y lo afinamos</h3>
        <p>Empieza a atender de verdad. Revisamos conversaciones reales y lo ajustamos, con soporte y revisiones mensuales.</p>
        <span class="when">Desde el día 15</span></div>
    </div>
  </div>
</section>

<hr class="hr">

<section>
  <div class="wrap">
    <div class="center"><span class="eyebrow">Hablemos de dinero</span><h2>¿Cuánto cuesta?</h2>
      <p class="lead">La pregunta que todo el mundo tiene y casi nadie responde en su web.</p></div>
    <div class="price-box rv">
      <p style="font-size:1.08rem;color:var(--tx2);line-height:1.7">
        <strong style="color:var(--tx)">Depende de qué se automatice</strong>, y quien te dé un precio cerrado sin
        conocer tu negocio se lo está inventando. Lo que sí garantizamos:</p>
      <ul class="pl">
        <li><span class="ck">✓</span> <span><strong style="color:var(--tx)">Presupuesto cerrado antes de empezar.</strong></span></li>
        <li><span class="ck">✓</span> <span><strong style="color:var(--tx)">Sin cuotas sorpresa</strong> ni letra pequeña.</span></li>
        <li><span class="ck">✓</span> <span><strong style="color:var(--tx)">El diagnóstico es gratis</strong> y no compromete a nada.</span></li>
        <li><span class="ck">✓</span> <span><strong style="color:var(--tx)">Si no lo vemos rentable, te lo decimos.</strong></span></li>
      </ul>
      <div style="margin-top:28px">
        <a class="btn btn-wa btn-full" href="{WA + q('Hola, quiero mi diagnóstico gratuito')}" target="_blank" rel="noopener">
          <svg width="21" height="21" fill="#04240f"><use href="#wa-icon"/></svg> Pedir mi diagnóstico gratuito</a>
      </div>
    </div>
  </div>
</section>

<hr class="hr">

<section>
  <div class="wrap" style="max-width:820px">
    <div class="center"><span class="eyebrow">Dudas frecuentes</span>
      <h2>Lo que nos preguntáis<br><span class="grad">antes de dar el paso</span></h2></div>
    <div style="margin-top:34px">
{faqs}
    </div>
  </div>
</section>

<section class="final">
  <div class="wrap">
    <span class="badge"><span class="dot"></span> Respuesta en menos de 2 horas</span>
    <h2>{s['cierre']}</h2>
    <p class="lead" style="margin:16px auto 30px">{s['cierresub']}</p>
    <a class="btn btn-wa btn-full" href="{cta}" target="_blank" rel="noopener">
      <svg width="21" height="21" fill="#04240f"><use href="#wa-icon"/></svg> Probar el agente ahora</a>
    <p class="micro" style="margin-top:14px">Gratis · Sin formularios · Sin compromiso</p>
  </div>
</section>

<footer>
  <div class="wrap f-in">
    <a href="/"><img src="{LOGO}" alt="MontAI" style="height:34px;opacity:.75" width="98" height="34"/></a>
    <p>© 2026 MontAI · Automatización con IA para negocios en España</p>
    <p><a href="/blog/">Blog</a> · <a href="/privacidad.html">Privacidad</a></p>
  </div>
</footer>

<script>
(function(){{var e=document.querySelectorAll('.rv');
if(!('IntersectionObserver' in window)){{e.forEach(function(x){{x.classList.add('on')}});return}}
var o=new IntersectionObserver(function(en){{en.forEach(function(x,i){{if(x.isIntersecting){{
setTimeout(function(){{x.target.classList.add('on')}},(i%3)*90);o.unobserve(x.target)}}}})}},
{{threshold:.12,rootMargin:'0px 0px -50px 0px'}});e.forEach(function(x){{o.observe(x)}})}})();
</script>
</body>
</html>
"""


def main():
    dest = os.path.join(AQUI, "sectores")
    os.makedirs(dest, exist_ok=True)
    for s in SECTORES:
        p = os.path.join(dest, s["slug"] + ".html")
        io.open(p, "w", encoding="utf-8").write(pagina(s))
        print("  OK  sectores/%-42s %6.1f KB" % (s["slug"] + ".html", os.path.getsize(p) / 1024))
    print("\n%d paginas de sector generadas." % len(SECTORES))
    print("Recuerda: anadirlas a sitemap.xml y enlazarlas desde index.html")


if __name__ == "__main__":
    main()
