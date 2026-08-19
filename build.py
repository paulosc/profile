# -*- coding: utf-8 -*-
"""Builds public/index.html, public/services.html and public/i18n.js.

English is written straight into the HTML, so the page reads correctly even if
JavaScript never runs. i18n.js swaps the text for pt/es on top of that.

Run:  python build.py
"""
import io, os, re, json, hashlib
from content import S
from content_quote import Q

HERE = os.path.dirname(os.path.abspath(__file__))
PUB = os.path.join(HERE, "public")
LANGS = ["en", "pt", "es"]


def t(key, tag="span", cls=None, attrs=""):
    """Emit an element carrying the English text plus its translation key."""
    if key not in S:
        raise KeyError("missing content key: " + key)
    c = ' class="%s"' % cls if cls else ""
    return '<%s%s%s data-i18n="%s">%s</%s>' % (tag, c, (" " + attrs if attrs else ""), key, S[key]["en"], tag)


def raw(key):
    return S[key]["en"]


# --------------------------------------------------------------- chrome
FAVICON = ("data:image/svg+xml,<svg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 32 32%22>"
           "<rect width=%2232%22 height=%2232%22 rx=%226%22 fill=%22%231B4FD8%22/>"
           "<text x=%2216%22 y=%2223%22 font-family=%22monospace%22 font-size=%2219%22 font-weight=%22700%22 "
           "fill=%22white%22 text-anchor=%22middle%22>P</text></svg>")


def head(title_key, desc_key):
    return u"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title data-i18n="%s">%s</title>
<meta name="description" content="%s" data-i18n-meta="%s">
<link rel="stylesheet" href="/style.css">
<link rel="icon" href="%s">
</head>
<body>
""" % (title_key, raw(title_key), raw(desc_key), desc_key, FAVICON)


def nav(page):
    svc_key = "nav.services_short" if page == "services" else "nav.services"
    picker = ('<div class="langs" role="group" aria-label="%s">'
              '<button type="button" data-lang="en">EN</button>'
              '<button type="button" data-lang="pt">PT</button>'
              '<button type="button" data-lang="es">ES</button>'
              '</div>') % raw("lang.aria")
    return u"""<nav>
  <div class="wrap inner">
    <a class="brand" href="/">PAULO&nbsp;CARVALHO<span style="color:var(--accent)">.</span></a>
    <div class="links">
      <a href="/#work" data-i18n="nav.work">%s</a>
      <a href="/#history" data-i18n="nav.experience">%s</a>
      <a href="/#about" data-i18n="nav.about">%s</a>
      <a href="/services" data-i18n="%s">%s</a>
      %s
      <a class="cta" href="/services#quote" data-i18n="nav.quote">%s</a>
    </div>
  </div>
</nav>
""" % (raw("nav.work"), raw("nav.experience"), raw("nav.about"),
       svc_key, raw(svc_key), picker, raw("nav.quote"))


def status(key):
    return '<span class="status"><span class="dot"></span>%s</span>' % t(key).replace("<span ", "<span ", 1)


def cred(name, key):
    return '<div class="cred"><b>%s</b>%s</div>' % (name, t(key))


def cred_k(name_key, key):
    return '<div class="cred">%s%s</div>' % (t(name_key, "b"), t(key))


# ----------------------------------------------------------------- index
def build_index():
    creds = "\n      ".join([
        cred("Ericsson", "cred.ericsson"),
        cred("Ita&uacute;", "cred.itau"),
        cred("PolicyMedical", "cred.policy"),
        cred_k("cred.years_n", "cred.years"),
        cred_k("cred.postgrad_n", "cred.postgrad"),
    ])

    hero = u"""<header class="hero" id="top">
  <div class="wrap">
    <span class="status"><span class="dot"></span><span data-i18n="home.status">%s</span></span>
    <h1 data-i18n-html="home.h1">%s</h1>
    <p class="lede" data-i18n-html="home.lede1">%s</p>
    <p class="lede" style="margin-top:14px" data-i18n-html="home.lede2">%s</p>
    <div class="hero-actions">
      <a class="btn btn-solid" href="#work" data-i18n="home.cta1">%s</a>
      <a class="btn btn-ghost" href="/services" data-i18n="home.cta2">%s</a>
    </div>

    <div class="creds">
      %s
    </div>
  </div>
</header>
""" % (raw("home.status"), raw("home.h1"), raw("home.lede1"), raw("home.lede2"),
       raw("home.cta1"), raw("home.cta2"), creds)

    def workcard(slug, tags):
        paras = "".join(
            '\n          <p style="font-size:.94rem;color:var(--ink-2)" data-i18n-html="work.%s.p%d">%s</p>' % (slug, i, raw("work.%s.p%d" % (slug, i)))
            for i in (1, 2) if ("work.%s.p%d" % (slug, i)) in S)
        tagspan = "".join('<span class="tag">%s</span>' % x for x in tags)
        return u"""      <article class="work">
        <div class="work-h">
          %s
          %s
        </div>
        <div class="work-b">%s
          <div class="tags">%s</div>
        </div>
      </article>
""" % (t("work.%s.h" % slug, "h3"), t("work.%s.meta" % slug, "span", "lbl"), paras, tagspan)

    work = u"""<section id="work">
  <div class="wrap">
    <div class="sec-lbl">%s</div>
    %s
    <div class="grid g2" style="margin-top:32px">

%s
%s
%s
%s
    </div>
""" % (t("work.label", "span", "lbl"), t("work.h2", "h2"),
       workcard("itau", ["Java", "Spring Boot", "Kafka", "AWS SQS", "Lambda", "Docker", "CI/CD"]),
       workcard("policy", ["Java 11", "Spring Boot", "Kotlin", "Elasticsearch", "MongoDB", "Kafka", "Vue", "Angular", "Jenkins"]),
       workcard("icc", ["Java", "JSF", "PrimeFaces", "C", "FreeRTOS", "Embedded Linux", "Angular", "NodeJS"]),
       workcard("pedifood", ["Java", "Spring Boot", "Angular", "AWS"]))

    def hist(year, slug):
        return u"""        <div class="pstep"><span class="n" style="width:auto">%s</span><div class="c">%s%s</div></div>
""" % (year, t("hist.%s.h" % slug, "h3"), t("hist.%s.p" % slug, "p", None, 'style="color:var(--ink-2)"'))

    timeline = u"""
    <div style="margin-top:44px">
      <div class="sec-lbl" id="history">%s</div>
      <div class="steps" style="max-width:80ch">
%s%s%s%s%s%s      </div>
    </div>
""" % (t("hist.label", "span", "lbl"), hist("2023", "zup"), hist("2018", "policy"),
       hist("2011", "icc"), hist("2010", "imagem"), hist("2008", "kiq"), hist("2014", "pronatec"))

    education = u"""
    <div style="margin-top:44px">
      <div class="sec-lbl">%s</div>
      <div class="grid g2">
        <div class="card">
          <span class="lbl">2014 &mdash; 2016</span>
          %s
          <p style="font-size:.92rem;color:var(--ink-2)">INATEL</p>
        </div>
        <div class="card">
          <span class="lbl">2007 &mdash; 2010</span>
          %s
          <p style="font-size:.92rem;color:var(--ink-2)">UNIVAS</p>
        </div>
      </div>
    </div>
  </div>
</section>
""" % (t("edu.label", "span", "lbl"), t("edu.post.h", "h3"), t("edu.bach.h", "h3"))

    core = ["Java", "Spring Boot", "Kafka", "AWS SQS", "Microservices", "REST", "Docker", "AWS",
            "PostgreSQL", "MongoDB", "Elasticsearch", "Python", "Kotlin", "Angular", "Vue",
            "TDD / BDD", "CI/CD", "Jenkins"]
    also = ["C", "C++", "FreeRTOS", "Embedded Linux", "JSF", "PrimeFaces", "Grails", "Groovy",
            "Flutter", "Firebase", "Gemini"]

    about = u"""<section id="about">
  <div class="wrap">
    <div class="sec-lbl">%s</div>
    <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(300px,1fr));gap:36px;align-items:start">
      <div style="display:flex;flex-direction:column;gap:16px">
        %s
        <p style="color:var(--ink-2)" data-i18n-html="about.p1">%s</p>
        <p style="color:var(--ink-2)" data-i18n-html="about.p2">%s</p>
        <p style="color:var(--ink-2)" data-i18n-html="about.p3">%s</p>
      </div>
      <div style="display:flex;flex-direction:column;gap:14px">
        <div class="card">
          %s
          <div class="tags">%s</div>
        </div>
        <div class="card">
          %s
          <div class="tags">%s</div>
        </div>
        <div class="card">
          %s
          <p style="font-size:.93rem;color:var(--ink-2)" data-i18n-html="about.langs.p">%s</p>
        </div>
      </div>
    </div>
  </div>
</section>
""" % (t("about.label", "span", "lbl"), t("about.h2", "h2"),
       raw("about.p1"), raw("about.p2"), raw("about.p3"),
       t("about.stack", "span", "lbl"), "".join('<span class="tag">%s</span>' % x for x in core),
       t("about.also", "span", "lbl"), "".join('<span class="tag">%s</span>' % x for x in also),
       t("about.langs", "span", "lbl"), raw("about.langs.p"))

    band = u"""<section id="hire" style="background:var(--surface)">
  <div class="wrap" style="display:flex;flex-wrap:wrap;gap:28px;align-items:center;justify-content:space-between">
    <div style="max-width:52ch;display:flex;flex-direction:column;gap:12px">
      %s
      %s
      <p style="color:var(--ink-2)" data-i18n-html="hire.p">%s</p>
    </div>
    <a class="btn btn-solid" href="/services" style="font-size:1rem;padding:14px 26px" data-i18n="hire.cta">%s</a>
  </div>
</section>
""" % (t("hire.label", "span", "lbl"), t("hire.h2", "h2"), raw("hire.p"), raw("hire.cta"))

    return (head("meta.home.title", "meta.home.desc") + nav("index") + hero + work
            + timeline + education + about + band + footer() + script_tail(False))


# -------------------------------------------------------------- services
def build_services():
    hero = u"""<header class="hero" id="top">
  <div class="wrap">
    <span class="status"><span class="dot"></span><span data-i18n="svc.status">%s</span></span>
    <h1 data-i18n-html="svc.h1">%s</h1>
    <p class="lede" data-i18n-html="svc.lede">%s</p>
    <div class="hero-actions">
      <a class="btn btn-solid" href="#quote" data-i18n="svc.cta1">%s</a>
      <a class="btn btn-ghost" href="/" data-i18n="svc.cta2">%s</a>
    </div>
  </div>
</header>
""" % (raw("svc.status"), raw("svc.h1"), raw("svc.lede"), raw("svc.cta1"), raw("svc.cta2"))

    prices = {"api": 450, "upgrade": 600, "bug": 300, "ai": 800, "data": 350, "cicd": 400, "review": 500}
    order = ["api", "upgrade", "bug", "ai", "data", "cicd", "review"]
    cards = []
    for cid in order:
        bullets = ""
        i = 0
        while ("card.%s.b%d" % (cid, i)) in S:
            bullets += "\n          " + t("card.%s.b%d" % (cid, i), "li")
            i += 1
        cards.append(u"""      <div class="card">
        %s
        %s
        <span class="price"><span data-i18n="svc.from">%s</span> $%d</span>
        <ul>%s
        </ul>
      </div>
""" % (t("card.%s.tag" % cid, "span", "lbl"), t("card.%s.h" % cid, "h3"),
       raw("svc.from"), prices[cid], bullets))

    services = u"""<section id="services">
  <div class="wrap">
    <div class="sec-lbl">%s</div>
    %s
    <p class="lede" style="margin-top:14px;margin-bottom:32px" data-i18n-html="svc.intro">%s</p>

    <div class="grid g3">
%s    </div>
  </div>
</section>
""" % (t("svc.label", "span", "lbl"), t("svc.h2", "h2"), raw("svc.intro"), "".join(cards))

    quote = u"""<section id="quote">
  <div class="wrap">
    <div class="sec-lbl">%s</div>
    %s
    <p class="lede" style="margin-top:14px;margin-bottom:32px" data-i18n-html="q.intro">%s</p>

    <div class="cfg">
      <div class="cfg-main">
        <div class="step">
          <div class="step-h"><span class="step-n">01</span>%s</div>
          <div class="opts cols" id="svc"></div>
        </div>
        <div class="step" id="optStep">
          <div class="step-h"><span class="step-n">02</span>%s</div>
          <div id="opts"></div>
        </div>
        <div class="step">
          <div class="step-h"><span class="step-n">03</span>%s</div>
          <div class="opts">
            <label class="opt" id="rushOpt">
              <input type="checkbox" id="rush">
              <span class="t">%s%s</span>
              <span class="p">+35%%</span>
            </label>
          </div>
        </div>
      </div>

      <aside class="quote">
        <div class="quote-h">%s</div>
        <div class="quote-b">
          <div>
            <div class="total" id="total">$450</div>
            %s
          </div>
          <div class="meta-grid">
            <div>%s<b id="days">4 days</b></div>
            <div>%s<b id="revs">2</b></div>
          </div>
          <div class="lines" id="lines"></div>
          <button class="btn btn-solid" id="send" data-i18n="q.send">%s</button>
          <button class="btn btn-ghost" id="copy" data-i18n="q.copy">%s</button>
          <p class="fineprint" data-i18n-html="q.fine">%s</p>
        </div>
      </aside>
    </div>
  </div>
</section>
""" % (t("q.label", "span", "lbl"), t("q.h2", "h2"), raw("q.intro"),
       t("q.step1", "h3"), t("q.step2", "h3"), t("q.step3", "h3"),
       t("q.rush.t", "b"), t("q.rush.d", "small"),
       t("q.yours", "span", "lbl", 'style="color:var(--accent)"'),
       t("q.terms", "span", "fineprint"),
       t("q.delivery", "span", "lbl"), t("q.revisions", "span", "lbl"),
       raw("q.send"), raw("q.copy"), raw("q.fine"))

    steps = ""
    for i in (1, 2, 3, 4):
        steps += u"""      <div class="pstep"><span class="n">0%d</span><div class="c">%s%s</div></div>
""" % (i, t("proc.%d.h" % i, "h3"), t("proc.%d.p" % i, "p", None, 'style="color:var(--ink-2)"'))

    process = u"""<section id="process">
  <div class="wrap">
    <div class="sec-lbl">%s</div>
    %s
    <div class="steps" style="margin-top:28px;max-width:78ch">
%s    </div>
  </div>
</section>
""" % (t("proc.label", "span", "lbl"), t("proc.h2", "h2"), steps)

    return (head("meta.svc.title", "meta.svc.desc") + nav("services") + hero + services
            + quote + process + footer()
            + '\n<div class="toast" id="toast">%s</div>\n' % raw("q.copied")
            + script_tail(True))


def footer():
    return u"""<footer>
  <div class="wrap">
    <div class="foot-grid">
      <div style="max-width:46ch;display:flex;flex-direction:column;gap:14px">
        %s
        <p style="color:var(--ink-2)" data-i18n-html="foot.p">%s</p>
        <span class="status" style="align-self:flex-start"><span class="dot"></span><span data-i18n="foot.reply">%s</span></span>
      </div>
      <div class="contact-list">
        %s
        <a href="mailto:pcarvalhosergio@gmail.com" id="mailLink">pcarvalhosergio@gmail.com</a>
        <a href="https://wa.me/5535991040850">WhatsApp +55 35 99104-0850</a>
        <a href="https://github.com/paulosc">GitHub</a>
        <span class="muted" style="font-size:.9rem;margin-top:6px" data-i18n-html="foot.where">%s</span>
      </div>
    </div>
    <p class="foot-note" data-i18n-html="foot.note">%s</p>
  </div>
</footer>
""" % (t("foot.h2", "h2"), raw("foot.p"), raw("foot.reply"),
       t("foot.contact", "span", "lbl", 'style="margin-bottom:4px"'),
       raw("foot.where"), raw("foot.note"))


def script_tail(with_quote):
    s = '\n<script src="/i18n.js"></script>\n'
    if with_quote:
        s += '<script src="/quote.js"></script>\n'
    return s + "</body>\n</html>\n"


# ---------------------------------------------------------------- i18n.js
def build_i18n():
    table = {}
    for lang in LANGS:
        table[lang] = {k: v[lang] for k, v in S.items()}
    return (u"// Generated by build.py — edit content.py / content_quote.py instead.\n"
            u"window.I18N = %s;\n"
            u"window.SVC_I18N = %s;\n\n" % (
                json.dumps(table, ensure_ascii=False, sort_keys=True),
                json.dumps(Q, ensure_ascii=False, sort_keys=True))
            ) + io.open(os.path.join(HERE, "i18n_runtime.js"), encoding="utf-8").read()


# ------------------------------------------------------------------ main
def main():
    io.open(os.path.join(PUB, "index.html"), "w", encoding="utf-8").write(build_index())
    io.open(os.path.join(PUB, "services.html"), "w", encoding="utf-8").write(build_services())
    io.open(os.path.join(PUB, "i18n.js"), "w", encoding="utf-8").write(build_i18n())

    # cache-bust every asset by content hash
    def h(f):
        return hashlib.sha1(io.open(os.path.join(PUB, f), "rb").read()).hexdigest()[:8]
    hashes = {f: h(f) for f in ["style.css", "quote.js", "i18n.js"]}
    for page in ["index.html", "services.html"]:
        p = os.path.join(PUB, page)
        s = io.open(p, encoding="utf-8").read()
        for f, v in hashes.items():
            s = re.sub(r'(href|src)="/%s(\?v=[a-f0-9]+)?"' % re.escape(f),
                       lambda m, f=f, v=v: '%s="/%s?v=%s"' % (m.group(1), f, v), s)
        io.open(p, "w", encoding="utf-8").write(s)

    missing = [k for k, v in S.items() for l in LANGS if not v.get(l)]
    print("strings: %d x %d languages" % (len(S), len(LANGS)))
    print("quote translations: pt=%d es=%d" % (len(Q["pt"]), len(Q["es"])))
    print("empty translations:", missing or "none")
    for f in ["index.html", "services.html", "i18n.js"]:
        print("  %-14s %6d bytes" % (f, os.path.getsize(os.path.join(PUB, f))))


if __name__ == "__main__":
    main()
