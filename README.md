# profile

Personal site — portfolio and instant project-quote configurator.

**Live:** https://profile-69599.web.app

## Structure

- `public/index.html` — the entire site. Single self-contained file, no build step, no dependencies.
- `firebase.json` — Firebase Hosting config.
- `.firebaserc` — points at the `profile-69599` project.

## Editing

Everything lives in `public/index.html`.

- **Contact email** — the `EMAIL` constant at the top of the `<script>` block. It feeds both the footer link and the quote "Send this brief" button.
- **Pricing** — the `SERVICES` object. Each service has a `base`, a `days` estimate, and option groups. Radio groups must keep their first option at `p: 0`, since that first option defines the advertised "from $X" price.
- **Portfolio** — the `<section id="work">` block.

## Deploy

```bash
firebase deploy --only hosting --account arena.gestao.app@gmail.com
```

The Firebase project lives under `arena.gestao.app@gmail.com`, not `pcarvalhosergio@gmail.com`.
