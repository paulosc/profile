# profile

Personal site — portfolio and instant project-quote configurator.

**Live:** https://profile-69599.web.app

## Structure

Two pages, deliberately separated: the home page presents who I am, `/services` sells.

- `public/index.html` — portfolio and background. No pricing, no sales tooling.
- `public/services.html` — served at `/services`. Offer, quote configurator, process.
- `public/style.css` — shared stylesheet.
- `public/quote.js` — the quote configurator. Only loaded by `/services`.
- `firebase.json` — Hosting config. `cleanUrls` is what maps `/services` to `services.html`.
- `.firebaserc` — points at the `profile-69599` project.

## Editing

- **Contact email** — the `EMAIL` constant at the top of `quote.js` feeds the "Send this brief" button; the footer link is plain HTML in both pages.
- **Pricing** — the `SERVICES` object in `quote.js`. Each service has a `base`, a `days` estimate and option groups. Radio groups must keep their first option at `p: 0`, because that option defines the advertised "from $X" on the service card.
- **Portfolio** — the `<section id="work">` block in `index.html`.

After editing `style.css` or `quote.js`, bump the `?v=` on the `<link>` and `<script>` tags in both HTML files. Without it, returning visitors keep the old asset.

## A trap worth knowing

Option rows are a `<label>` wrapping an `<input>`. The browser ticks the input as part of the label's *activation*, which happens after the click event is dispatched. Rebuilding the option list inside that click handler destroys the input before it is ticked, and the click is silently lost — the total simply never moves.

So `onOption` never re-renders. It reads the inputs back out of the DOM on a deferred tick and only repaints the selected state. Keep it that way.

## Deploy

```bash
firebase deploy --only hosting --account arena.gestao.app@gmail.com
```

The Firebase project lives under `arena.gestao.app@gmail.com`, not `pcarvalhosergio@gmail.com`.
