# MontAI

La guía de trabajo de este proyecto está en **[`AGENTS.md`](./AGENTS.md)** — léela antes de tocar nada.
Está escrita para cualquier asistente de IA, no solo para Claude.

Resumen de lo imprescindible:

- **Este repo es PÚBLICO.** Nunca escribas aquí tokens, claves ni IDs de infraestructura.
  Eso va en `_INFRA-PRIVADO.md`, que está en `.gitignore` y no se sube.
- Sitio estático sin build. `git push origin master` → Vercel despliega solo.
- **Verifica siempre contra la URL pública**, no contra el repo local: `git fetch origin` primero,
  y `curl` a `https://www.montai.es/…` para confirmar que algo está publicado de verdad.
- No inventes testimonios, precios ni estadísticas. Ver `AGENTS.md` §4.
