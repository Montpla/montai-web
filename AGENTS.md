# MontAI — guía de trabajo para agentes de IA

> Documento de traspaso. Escrito para que **cualquier** asistente de IA (Claude, GPT, Gemini, Copilot…)
> pueda continuar el trabajo sin contexto previo. Si vas a tocar este proyecto, lee esto primero.
>
> ⚠️ **Este repositorio es PÚBLICO** (github.com/Montpla/montai-web). No escribas aquí tokens,
> claves de API ni identificadores de infraestructura. Esos datos están en `_INFRA-PRIVADO.md`,
> que está en `.gitignore` y nunca debe subirse.

---

## 1. Qué es esto

**MontAI** es una agencia española de automatización con IA para pequeños negocios. Su producto es
un **agente de IA que atiende WhatsApp**: responde clientes, resuelve dudas y agenda citas solo.

Este repositorio es **solo la web** (`montai.es`). El sistema completo tiene más piezas:

| Pieza | Dónde vive | Qué hace |
|---|---|---|
| **Web pública** | este repo → Vercel | Capta clientes y los lleva al agente |
| **Bot de WhatsApp** | n8n (workflow) | El producto: atiende, agenda, guarda leads |
| **Bot de Telegram** | n8n (workflow) | Canal secundario, sigue activo |
| **CRM** | Airtable | Tablas `Leads` y `Citas` |
| **Puente WhatsApp** | Evolution API | Conecta WhatsApp con n8n |
| **Blog automático** | tarea programada local | Publica 1 artículo/semana en este repo |

Detalles de acceso, IDs y nombres de credenciales: **`_INFRA-PRIVADO.md`** (local, no versionado).

---

## 2. La web

**Sitio estático puro.** Sin build, sin framework, sin dependencias. Se edita el HTML y ya.

```
index.html          Home. CSS propio embebido en <style>. NO usa Tailwind.
privacidad.html     Política de privacidad (RGPD)
sectores/*.html     Páginas por sector. GENERADAS, no se editan a mano (ver §2.1)
css/montai.css      Estilos compartidos, usados por sectores/. La home los lleva
                    en línea a propósito: es la página de entrada.
_generar-sectores.py  Generador de sectores/. Los textos viven aquí.
blog/index.html     Índice del blog
blog/*.html         Artículos (misma plantilla, ver §5)
blog/style.css      Estilos compartidos del blog
sitemap.xml         Hay que añadir cada artículo nuevo a mano
robots.txt
*.png, favicon.*    Iconos
slides-video.html   Presentación suelta, no enlazada desde el menú
```

### 2.1. Páginas de sector

`sectores/*.html` **están generadas**. Si editas el HTML a mano, el siguiente
`python _generar-sectores.py` se lo lleva por delante. **Edita los textos en el script.**

Existen por dos motivos, y conviene no perder ninguno de vista al tocarlas:

1. **SEO.** "IA para clínicas dentales" compite mucho menos que "automatizar whatsapp negocio",
   donde la web hoy no aparece. Es una apuesta a medio plazo.
2. **Venta.** Al visitar un negocio se le manda una página escrita *para su sector*, no la home
   genérica. Esto sirve desde el primer día, sin esperar a posicionar.

**Cada sector lleva un texto distinto en su enlace de WhatsApp** (`?text=Hola MontAI, tengo una
clínica dental…`). Así se sabe desde qué página ha escrito cada persona sin necesidad de
herramientas. No lo unifiques.

**Añadir un sector:** copia un bloque de `SECTORES` en el script, cambia los textos, ejecuta el
script y luego **tres cosas más a mano**: la URL en `sitemap.xml`, una tarjeta en la sección
`#sectores` de `index.html`, y las comprobaciones de §8.

### Despliegue

`git push origin master` → **Vercel despliega solo**. No hay más pasos.

**Verificación obligatoria** — que exista el commit en local NO significa que esté publicado:

```bash
git status -sb                 # debe decir rama sincronizada, no "ahead of origin"
git log origin/master -1       # debe aparecer TU commit
curl -sk -o /dev/null -w "%{http_code}" https://www.montai.es/<pagina>   # debe dar 200
```

Ya ha pasado que un artículo quedara commiteado pero sin subir y nadie se enterase durante días.
**Verifica siempre contra la URL pública, no contra el repo local.**

---

## 3. Reglas de diseño (no negociables)

La home usa **glassmorphism**: paneles translúcidos con `backdrop-filter`, sobre tres luces
ambientales que derivan lentamente. Fondo `#06070C` (negro con matiz azul, para que el oro lea
cálido). Marca: **oro `#C9A84C`** sobre negro, tipografía **Inter**.

Tres decisiones deliberadas. **No las "simplifiques":**

1. **El botón de WhatsApp es SÓLIDO, nunca de cristal.** Es el único elemento opaco de la página,
   a propósito. La translucidez baja el contraste y ese botón es el que convierte.
2. **El desenfoque baja de 20px a 12px por debajo de 700px de ancho.** `backdrop-filter` es caro
   para la GPU; sin esto el scroll se entrecorta en móviles modestos.
3. **Hay un bloque `@supports not (backdrop-filter)`** que opaca todos los paneles. Sin él, en un
   navegador sin soporte el texto queda flotando sobre las luces, ilegible.

### ⚠️ Contraste: la trampa del cristal

El cristal **aclara el fondo efectivo** y rompe la accesibilidad sin que se note. Ya se publicó
un fallo así: el gris `--tx3` daba **3,97** sobre las tarjetas (el mínimo WCAG AA es **4,5**).

Ahora `--tx3: #8a8a95` → **5,43**. Si cambias colores:

- Mide contra el fondo **compuesto** (≈ `rgb(18,19,24)` detrás de una tarjeta de cristal),
  **nunca contra `#000`**.
- Verifica antes de publicar. Objetivo: ≥4,5 en texto normal, ≥3,0 en texto grande.

### Rendimiento

La home pesa **~38 KB**. Antes pesaba 2,3 MB (una imagen de héroe de 1,4 MB + Tailwind por CDN
compilando CSS en el navegador). **No vuelvas a meter Tailwind por CDN ni imágenes pesadas.**

- El "mockup" de conversación de WhatsApp del héroe es **CSS puro**, no una imagen. Mantenlo así.
- Las imágenes de Cloudinary aceptan transformaciones: `f_auto,q_auto,h_120` bajó el logo de
  145 KB a 6 KB. Úsalo siempre en URLs de Cloudinary.

---

## 4. Reglas de contenido (no negociables)

**Canal de contacto: WhatsApp.** Todo CTA lleva exactamente este enlace:

```
https://wa.me/34676085750?text=Hola%20MontAI%2C%20vengo%20de%20la%20web%20y%20quiero%20automatizar%20mi%20negocio
```

- El icono es el símbolo SVG `#wa-icon`; el botón flotante usa la clase `wa-float`.
- **Nunca** introduzcas enlaces `t.me` ni clases `tg-icon` / `tg-float`. La web usó Telegram hasta
  julio de 2026 y quedan referencias en documentación antigua: ignóralas.
- Matiz: en el **texto** de un artículo sí se puede mencionar Telegram como tema (el bot también lo
  atiende). Lo prohibido es que Telegram aparezca en los **CTA o enlaces de contacto**.

**Nunca inventes:**

- **Testimonios.** Los antiguos ("Juan M.", "María G.", con inicial en vez de foto y sin empresa)
  se retiraron porque se leían como falsos y restaban credibilidad. No los repongas ni crees otros.
  Solo se añadirá prueba social cuando haya un cliente real que permita nombre + empresa + cifra.
- **Precios.** El dueño nunca ha dado cifras. La sección de precio responde la objeción con honestidad
  ("presupuesto cerrado antes de empezar, sin cuotas sorpresa") sin dar números. Mantenlo así.
- **Estadísticas con fuente.** Se retiró un "+30% en ventas · Garantizado" por poco creíble. Si usas
  cifras en un artículo, mantenlas genéricas y sin atribuir a estudios inventados.

**Argumento central de la web:** MontAI vende agentes de IA **y tiene uno funcionando**. Por eso la
página no describe el producto: invita a **probarlo** ("Probar el agente ahora"). El CTA es la demo.
Es el mayor diferenciador frente a la competencia — consérvalo en cualquier rediseño.

---

## 5. Blog automático

Se publica **1 artículo por semana** sin intervención humana.

- **Banco de temas:** `_blog-topics.md` (en `.gitignore`, NO se sube). Formato:
  `[ ] slug | Título | palabra clave`. La rutina coge el primer `[ ]`, escribe y lo marca `[x]`.
- **Plantilla:** copia `blog/seguimiento-leads-automatico-ia.html` y adapta solo meta, JSON-LD,
  breadcrumb, `<h1>` y el cuerpo de `<div class="prose">`.
- **Al publicar hay que tocar 3 ficheros:** el artículo nuevo, `blog/index.html` (añadir tarjeta al
  grid) y `sitemap.xml` (añadir `<url>`).
- **Cada artículo debe llevar los dos scripts de analítica** en el `<head>` (ver §6). Si faltan,
  ese artículo no se mide.

⚠️ `_blog-topics.md` está en `.gitignore`, así que **no viaja con `git clone`**. Si falta, hay que
reconstruirlo mirando qué `.html` existen ya en `blog/`.

---

## 6. Analítica

Dos productos de Vercel, ambos **sin cookies, sin IP y sin perfilado** (por eso no hace falta banner
de consentimiento, y la política de privacidad §8 los declara):

```html
<script defer src="/_vercel/insights/script.js"></script>        <!-- visitas -->
<script defer src="/_vercel/speed-insights/script.js"></script>  <!-- velocidad -->
```

Están en las 12 páginas. **Cualquier página nueva debe llevarlos.**

⚠️ **Trampa conocida:** activar Web Analytics en el panel de Vercel **no publica la ruta**
`/_vercel/insights/script.js` — solo aparece **tras el siguiente despliegue**. Hasta entonces da 404,
que parece exactamente "no lo han activado". Si da 404, **lanza un despliegue antes de sacar
conclusiones**.

Comprobar que mide de verdad (que el fichero exista no basta): carga la web en un navegador y busca
en las peticiones de red un **`POST /_vercel/insights/view` → 200**. Eso es la visita registrándose.

**Ojo:** "Speed Insights" y "Web Analytics" son productos distintos en pestañas distintas del panel,
y se confunden. `speed-insights` = cómo de rápido. `insights` = cuánta gente.

---

## 7. Trampas conocidas (aprendidas a base de fallos)

| Síntoma | Causa real |
|---|---|
| "El blog lleva semanas sin publicar" | La tarea programada solo corre con la app abierta. Antes era solo los miércoles y se perdieron 3 semanas seguidas. Ahora comprueba a diario y publica solo si han pasado ≥7 días. |
| "Esto no se ha publicado" (y sí estaba) | `git status` compara contra una referencia **obsoleta**. **Haz siempre `git fetch origin` antes** de diagnosticar nada. |
| Rutas rotas de un día para otro | La carpeta del proyecto se ha movido ya dos veces (estuvo en `OneDrive\Desktop\WEB MONTAi`). Si una ruta falla, **búscala** antes de dar nada por perdido. |
| La analítica no mide | Ver §6: hace falta un despliegue posterior a la activación. |
| Texto gris ilegible | Ver §3: medir contraste sobre el fondo compuesto, no sobre negro. |

---

## 8. Antes de dar algo por terminado

```bash
# 1. Sincronizar de verdad
git fetch origin && git status -sb

# 2. Nada sensible en el commit (repo PÚBLICO)
git status --porcelain | grep -iE "env|topics|token|secret|privado"   # debe salir vacío

# 3. Sin rastros de Telegram en los CTA
grep -rn "t.me/\|tg-icon\|tg-float" *.html blog/*.html               # debe salir vacío

# 4. Analítica en toda página nueva
grep -c "_vercel/insights" <pagina>.html                             # debe dar 1

# 5. Publicado DE VERDAD
curl -sk -o /dev/null -w "%{http_code}" https://www.montai.es/<pagina>   # 200
```

Y una regla general: **verifica contra la web pública, no contra tu copia local.** La mayoría de los
fallos de este proyecto han sido cosas que parecían hechas y no lo estaban.
