# profile

Personal site — portfolio and instant project-quote configurator.

**Live:** https://paulosergiocarvalho.com.br (Firebase origin: https://profile-69599.web.app)

## Languages

English, Portuguese and Spanish. English is written into the HTML, so the page
still reads correctly if JavaScript never runs; `i18n.js` swaps it afterwards.

Detection order: `?lang=xx` in the URL, then a saved choice in `localStorage`,
then `navigator.languages`, then the time zone as a location hint, then English.

There is deliberately **no IP geolocation**. It needs a third-party request,
hands every visitor's address to that provider, delays first paint and gets it
wrong behind a VPN. The browser already states which languages the person reads.

## Domain

`paulosergiocarvalho.com.br`, registered at Registro.br and using its free DNS
(`a.auto.dns.br` / `b.auto.dns.br`). Connected to Firebase Hosting through the
console — there is no CLI command for custom domains.

`DOMAIN` in `build.py` is the single place the address is written; it feeds the
canonical tag, the Open Graph tags, `robots.txt` and `sitemap.xml`.

`make_og.py` renders `public/og.png`, the card shown when the link is pasted into
LinkedIn or WhatsApp. Rerun it only if the name, role or credential row changes.

## Build

The two HTML pages and `i18n.js` are generated. Do not edit them by hand.

```bash
python build.py
```

- `content.py` — every string on the pages, in the three languages.
- `content_quote.py` — the configurator's strings. English lives in `quote.js`
  and is the fallback, so a missing key degrades to English rather than blanking out.
- `i18n_runtime.js` — detection and switching; appended to the generated `i18n.js`.

`build.py` also stamps `?v=<content hash>` onto the CSS and JS references, so a
deploy can never leave a returning visitor on a stale asset.

## Structure

Two pages, deliberately separated: the home page presents who I am, `/services` sells.

- `public/index.html` — generated. Portfolio and background; no pricing, no sales tooling.
- `public/services.html` — generated, served at `/services`. Offer, quote configurator, process.
- `public/i18n.js` — generated. Translation tables plus the language runtime.
- `public/style.css` — shared stylesheet. Edited by hand.
- `public/quote.js` — the quote configurator. Edited by hand; only loaded by `/services`.
- `firebase.json` — Hosting config. `cleanUrls` is what maps `/services` to `services.html`.
- `.firebaserc` — points at the `profile-69599` project.

## Editing

- **Copy** — `content.py`, then `python build.py`.
- **Contact email** — the `EMAIL` constant at the top of `quote.js` feeds the "Send this brief" button; the footer link is emitted by `build.py`.
- **Pricing** — the `SERVICES` object in `quote.js`. Each service has a `base`, a `days` estimate and option groups. Radio groups must keep their first option at `p: 0`, because that option defines the advertised "from $X" on the service card. Adding an option means adding its translation to `content_quote.py`.
- **Portfolio** — the `work.*` keys in `content.py` and the `workcard(...)` calls in `build.py`.

## Two traps worth knowing

**Never let CSS hide what only JavaScript can reveal.** The scroll animation
started as a plain `.reveal{opacity:0}` plus a script that added `.in`. The
script tag failed to make it into the generated HTML and every section below the
fold went invisible on the live site. The rule is now scoped under `.js-reveal`,
a class `reveal.js` sets on `<html>` before it observes anything, and the script
also force-reveals everything after three seconds. Two independent ways for the
content to survive a broken script.

## A trap worth knowing

Option rows are a `<label>` wrapping an `<input>`. The browser ticks the input as part of the label's *activation*, which happens after the click event is dispatched. Rebuilding the option list inside that click handler destroys the input before it is ticked, and the click is silently lost — the total simply never moves.

So `onOption` never re-renders. It reads the inputs back out of the DOM on a deferred tick and only repaints the selected state. Keep it that way.

## Deploy

```bash
firebase deploy --only hosting --account arena.gestao.app@gmail.com
```

The Firebase project lives under `arena.gestao.app@gmail.com`, not `pcarvalhosergio@gmail.com`.
