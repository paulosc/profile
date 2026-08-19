// Configurator strings are translated by path, e.g. "api.auth.oauth.t".
// English stays in this file as both the source and the fallback, so a missing
// translation degrades to English instead of blanking the option out.
function L(){ return window.__lang || "en"; }
function tr(path, fallback){
  var m = (window.SVC_I18N || {})[L()];
  return (m && m[path] != null) ? m[path] : fallback;
}
function ui(key, fallback){
  var d = (window.I18N || {})[L()];
  return (d && d[key] != null) ? d[key] : fallback;
}
function P(g, o){ return state.svc + "." + g.id + "." + o.v; }

/* ---- EDIT THIS ---- */
var EMAIL = "pcarvalhosergio@gmail.com";
/* ------------------- */

var SERVICES = {
  api: { name:"Third-party API integration", base:450, days:4, revs:2, groups:[
    { id:"endpoints", label:"How many endpoints?", type:"radio", opts:[
      {v:"1-3", t:"1 to 3 endpoints", d:"A focused integration", p:0, days:0},
      {v:"4-8", t:"4 to 8 endpoints", d:"A full feature surface", p:250, days:2},
      {v:"9+",  t:"9 or more", d:"Whole API covered", p:600, days:5}]},
    { id:"auth", label:"Authentication", type:"radio", opts:[
      {v:"key", t:"API key or token", d:"Straightforward", p:0, days:0},
      {v:"oauth", t:"OAuth2 / OIDC", d:"Refresh flows, expiry, scopes", p:150, days:1},
      {v:"custom", t:"Custom or undocumented", d:"I reverse-engineer it from real responses", p:300, days:2}]},
    { id:"extras", label:"Add-ons", type:"check", opts:[
      {v:"hooks", t:"Inbound webhooks", d:"Signature verification and idempotency", p:200, days:2},
      {v:"docs", t:"Written documentation", d:"How to run it and what breaks it", p:150, days:1},
      {v:"monitor", t:"Failure alerting", d:"You hear about it before your users do", p:250, days:1}]}
  ]},
  upgrade: { name:"Legacy Java & Spring upgrade", base:600, days:8, revs:2, groups:[
    { id:"jump", label:"How far are you jumping?", type:"radio", opts:[
      {v:"minor", t:"Minor version bump", d:"Same major line", p:0, days:0},
      {v:"java", t:"Java 8 or 11 → 17 / 21", d:"Language and JVM migration", p:400, days:4},
      {v:"boot", t:"Spring Boot 2 → 3", d:"Includes the javax → jakarta migration", p:750, days:7}]},
    { id:"size", label:"Project size", type:"radio", opts:[
      {v:"s", t:"Under 50 source files", d:"", p:0, days:0},
      {v:"m", t:"50 to 200 files", d:"", p:300, days:3},
      {v:"l", t:"Over 200 files", d:"", p:800, days:7}]},
    { id:"tests", label:"Does it have tests today?", type:"radio", opts:[
      {v:"yes", t:"Yes, and they pass", d:"They prove nothing changed", p:0, days:0},
      {v:"some", t:"Some, partly broken", d:"I repair what's needed to verify", p:200, days:2},
      {v:"no", t:"None", d:"I add a thin safety net over critical paths first", p:400, days:4}]},
    { id:"extras", label:"Add-ons", type:"check", opts:[
      {v:"ci", t:"CI pipeline set up", d:"Build, test and deploy on every push", p:400, days:2},
      {v:"cve", t:"Vulnerable dependencies replaced", d:"Audit and remediation", p:300, days:2}]}
  ]},
  bug: { name:"Find and fix a stuck bug", base:300, days:3, revs:2, groups:[
    { id:"kind", label:"How does it behave?", type:"radio", opts:[
      {v:"repro", t:"Reproducible on demand", d:"Fails the same way every time", p:0, days:0},
      {v:"inter", t:"Intermittent", d:"Once every N requests, no clear trigger", p:400, days:3},
      {v:"prod", t:"Only in production", d:"Works fine on staging — the expensive kind", p:650, days:4}]},
    { id:"extras", label:"Add-ons", type:"check", opts:[
      {v:"post", t:"Written post-mortem", d:"Root cause and how to prevent the class of bug", p:250, days:1},
      {v:"audit", t:"Sweep for the same pattern elsewhere", d:"Usually there is more than one", p:350, days:2}]}
  ]},
  ai: { name:"AI feature in an existing product", base:800, days:9, revs:2, groups:[
    { id:"kind", label:"What should it do?", type:"radio", opts:[
      {v:"extract", t:"Extract or classify", d:"Structured data out of documents or text", p:0, days:0},
      {v:"rag", t:"Answer questions over your data", d:"Retrieval with real relevance work", p:500, days:4},
      {v:"agent", t:"Take actions in your systems", d:"Tool use, with guardrails", p:900, days:7}]},
    { id:"extras", label:"Add-ons", type:"check", opts:[
      {v:"eval", t:"Eval harness", d:"Measured accuracy, so regressions are visible", p:350, days:2},
      {v:"deploy", t:"Deploy and monitor", d:"Tracing plus cost-per-request reporting", p:400, days:2},
      {v:"multi", t:"Provider-agnostic", d:"Swap models without a rewrite", p:300, days:2}]}
  ]},
  data: { name:"Scraper & scheduled pipeline", base:350, days:4, revs:2, groups:[
    { id:"sources", label:"How many sources?", type:"radio", opts:[
      {v:"1", t:"One site or API", d:"", p:0, days:0},
      {v:"2-5", t:"Two to five", d:"", p:300, days:3},
      {v:"6+", t:"Six or more", d:"", p:700, days:6}]},
    { id:"extras", label:"Add-ons", type:"check", opts:[
      {v:"sched", t:"Scheduling and drift alerts", d:"You hear when the source layout changes", p:200, days:1},
      {v:"dash", t:"Dashboard", d:"Browse and export the data", p:350, days:3}]}
  ]},
  cicd: { name:"CI/CD pipeline from zero", base:400, days:3, revs:2, groups:[
    { id:"envs", label:"Environments", type:"radio", opts:[
      {v:"1", t:"One", d:"Production only", p:0, days:0},
      {v:"2-3", t:"Two or three", d:"Staging plus production", p:250, days:2},
      {v:"4+", t:"Four or more", d:"", p:500, days:4}]},
    { id:"extras", label:"Add-ons", type:"check", opts:[
      {v:"iac", t:"Infrastructure as code", d:"Terraform — environments become reproducible", p:450, days:3},
      {v:"rb", t:"Automated rollback", d:"One command back to the last good build", p:250, days:1}]}
  ]},
  review: { name:"Architecture review", base:500, days:5, revs:1, groups:[
    { id:"depth", label:"How deep?", type:"radio", opts:[
      {v:"survey", t:"Survey", d:"Structure, risks and quick wins", p:0, days:0},
      {v:"deep", t:"Deep review", d:"Data model, boundaries, scaling limits, cost", p:500, days:4}]},
    { id:"extras", label:"Add-ons", type:"check", opts:[
      {v:"exec", t:"Executive summary", d:"One page your board will actually read", p:200, days:1},
      {v:"road", t:"Prioritized remediation plan", d:"Sequenced, with effort estimates", p:400, days:3}]}
  ]}
};

var state = { svc:"api", picks:{}, rush:false };
var $ = function(id){ return document.getElementById(id); };

function initPicks(){
  state.picks = {};
  SERVICES[state.svc].groups.forEach(function(g){
    state.picks[g.id] = g.type === "radio" ? g.opts[0].v : [];
  });
}

function renderServices(){
  $("svc").innerHTML = Object.keys(SERVICES).map(function(k){
    var s = SERVICES[k];
    var sel = k === state.svc;
    return '<label class="opt' + (sel?' sel':'') + '" data-svc="' + k + '">' +
      '<input type="radio" name="svc"' + (sel?' checked':'') + '>' +
      '<span class="t"><b>' + tr(k + '.name', s.name) + '</b></span>' +
      '<span class="p">$' + s.base + '+</span></label>';
  }).join("");
}

function renderOptions(){
  var s = SERVICES[state.svc];
  $("opts").innerHTML = s.groups.map(function(g){
    var rows = g.opts.map(function(o){
      var sel = g.type === "radio" ? state.picks[g.id] === o.v : state.picks[g.id].indexOf(o.v) > -1;
      return '<label class="opt' + (sel?' sel':'') + '" data-g="' + g.id + '" data-v="' + o.v + '" data-t="' + g.type + '">' +
        '<input type="' + (g.type==="radio"?"radio":"checkbox") + '"' + (g.type==="radio"?' name="'+g.id+'"':'') + (sel?' checked':'') + '>' +
        '<span class="t"><b>' + tr(P(g,o) + '.t', o.t) + '</b>' + (o.d ? '<small>' + tr(P(g,o) + '.d', o.d) + '</small>' : '') + '</span>' +
        '<span class="p">' + (o.p ? '+$' + o.p : ui('q.included','included')) + '</span></label>';
    }).join("");
    return '<div style="margin-bottom:18px"><span class="lbl" style="display:block;margin-bottom:8px">' + tr(state.svc + '.' + g.id + '.label', g.label) + '</span><div class="opts">' + rows + '</div></div>';
  }).join("");

}

// A label wrapping an input fires the click twice — once on the label, once
// forwarded from the input as it bubbles back up — and "change" is not reliable
// for synthetic clicks. So nothing here mutates state per event. Instead we read
// the checkboxes back out of the DOM, which makes a repeated event a no-op.
function syncFromDom(){
  SERVICES[state.svc].groups.forEach(function(g){
    var chosen = g.type === "radio" ? null : [];
    g.opts.forEach(function(o){
      var el = $("opts").querySelector('[data-g="' + g.id + '"][data-v="' + o.v + '"]');
      if (el && el.querySelector("input").checked) {
        if (g.type === "radio") { chosen = o.v; } else { chosen.push(o.v); }
      }
    });
    if (g.type === "radio") { if (chosen) { state.picks[g.id] = chosen; } }
    else { state.picks[g.id] = chosen; }
  });
}

function onService(e){
  var lab = e.target.closest && e.target.closest("[data-svc]");
  if (!lab) return;
  var k = lab.getAttribute("data-svc");
  if (k === state.svc) return;
  state.svc = k;
  initPicks(); renderServices(); renderOptions(); calc();
}

// Never rebuild the options while the user is interacting with them. The browser
// ticks a checkbox as part of the label's activation, which lands *after* the
// click event; rebuilding in between throws away the node before it is ticked and
// the click is silently lost. So the inputs stay put and stay authoritative — we
// only repaint the selected state and recompute the total.
function refreshSel(){
  Array.prototype.forEach.call($("opts").querySelectorAll("[data-g]"), function(el){
    el.classList.toggle("sel", el.querySelector("input").checked);
  });
}

// Deliberately undebounced: every handler run only reads the DOM, so running
// several times is harmless, and the last run — after activation settles — wins.
function onOption(e){
  if (!(e.target.closest && e.target.closest("[data-g]"))) return;
  setTimeout(function(){ syncFromDom(); refreshSel(); calc(); }, 0);
}

function onRush(){
  setTimeout(function(){
    state.rush = $("rush").checked;
    $("rushOpt").classList.toggle("sel", state.rush);
    calc();
  }, 0);
}

function build(){
  var s = SERVICES[state.svc];
  var total = s.base, days = s.days, lines = [{ t: tr(state.svc + '.name', s.name), p: s.base }];
  s.groups.forEach(function(g){
    g.opts.forEach(function(o){
      var on = g.type === "radio" ? state.picks[g.id] === o.v : state.picks[g.id].indexOf(o.v) > -1;
      if (on && o.p > 0) { total += o.p; days += o.days; lines.push({ t: tr(P(g,o) + '.t', o.t), p:o.p }); }
      else if (on && o.p === 0 && g.type === "radio" && g.opts.length > 1) { /* baseline choice */ }
    });
  });
  if (state.rush) { total = Math.round(total * 1.35 / 5) * 5; days = Math.max(2, Math.ceil(days * 0.55)); lines.push({ t: ui("q.rush.t","Rush delivery"), p:"+35%" }); }
  return { total: total, days: days, revs: s.revs, lines: lines, name: tr(state.svc + '.name', s.name) };
}

function calc(){
  var q = build();
  $("total").textContent = "$" + q.total.toLocaleString("en-US");
  $("days").textContent = q.days + " " + (q.days === 1 ? ui("q.day","day") : ui("q.days","days"));
  $("revs").textContent = q.revs;
  $("lines").innerHTML = q.lines.map(function(l){
    return '<div class="line"><span>' + l.t + '</span><span>' + (typeof l.p === "number" ? "$" + l.p.toLocaleString("en-US") : l.p) + '</span></div>';
  }).join("");
}

function briefText(){
  var q = build(), s = SERVICES[state.svc];
  var out = tr("brief.title","PROJECT BRIEF") + "\n\n" + tr("brief.service","Service") + ": " + q.name + "\n\n" + tr("brief.scope","Scope selected") + ":\n";
  s.groups.forEach(function(g){
    g.opts.forEach(function(o){
      var on = g.type === "radio" ? state.picks[g.id] === o.v : state.picks[g.id].indexOf(o.v) > -1;
      if (on) { out += "  - " + tr(state.svc + "." + g.id + ".label", g.label) + ": " + tr(P(g,o) + ".t", o.t) + "\n"; }
    });
  });
  if (state.rush) { out += "  - " + tr("brief.rush","Rush delivery requested") + "\n"; }
  out += "\n" + tr("brief.price","Quoted price") + ": $" + q.total.toLocaleString("en-US") + " " + tr("brief.fixed","USD (fixed)") + "\n";
  out += tr("brief.eta","Estimated delivery") + ": " + q.days + " " + tr("brief.days_from","days from start") + "\n";
  out += tr("brief.revs","Revisions included") + ": " + q.revs + "\n";
  out += "\n" + tr("brief.please","--- Please add ---") + "\n";
  out += tr("brief.fields","Your name / company:\nRepository or system:\nLanguage & framework:\nWhat outcome would make this a success:\nAnything already tried:") + "\n";
  return out;
}

// Delegated and bound once, so re-rendering never duplicates a listener.
// Both events are wired because neither alone fires in every path.
$("svc").addEventListener("click", onService);
$("svc").addEventListener("change", onService);
$("opts").addEventListener("click", onOption);
$("opts").addEventListener("change", onOption);
$("rushOpt").addEventListener("click", onRush);
$("rushOpt").addEventListener("change", onRush);

function toast(msg){
  var t = $("toast"); t.textContent = msg; t.classList.add("on");
  setTimeout(function(){ t.classList.remove("on"); }, 2200);
}

$("copy").addEventListener("click", function(){
  var txt = briefText();
  if (navigator.clipboard && navigator.clipboard.writeText) {
    navigator.clipboard.writeText(txt).then(function(){ toast(ui("q.copied","Brief copied")); },
      function(){ toast("Select and copy manually"); });
  } else { toast("Copy not available here"); }
});

// A bare mailto: link silently does nothing for anyone without a desktop mail
// client configured, which is most people. Copy the brief first, then offer
// Gmail, the mail app and WhatsApp so at least one route always works.
$("send").addEventListener("click", function(){
  var b = build();
  var subj = tr("brief.subject","Project") + ": " + b.name + " - $" + b.total.toLocaleString("en-US");
  var body = briefText();

  if (navigator.clipboard && navigator.clipboard.writeText) {
    navigator.clipboard.writeText(body).catch(function(){});
  }

  $("toGmail").href = "https://mail.google.com/mail/?view=cm&fs=1&to=" + encodeURIComponent(EMAIL) +
                      "&su=" + encodeURIComponent(subj) + "&body=" + encodeURIComponent(body);
  $("toMail").href  = "mailto:" + EMAIL + "?subject=" + encodeURIComponent(subj) +
                      "&body=" + encodeURIComponent(body);
  $("toWhats").href = "https://wa.me/5535991040850?text=" + encodeURIComponent(subj + "\n\n" + body);

  $("sendPanel").hidden = false;
  $("sendPanel").scrollIntoView({block: "nearest", behavior: "smooth"});
});

$("closePanel").addEventListener("click", function(){ $("sendPanel").hidden = true; });

// wire the footer email from the constant
(function(){
  var a = $("mailLink");
  if (a) { a.href = "mailto:" + EMAIL; a.textContent = EMAIL; }
})();

initPicks(); renderServices(); renderOptions(); calc();

// Redraw in the new language, keeping whatever the visitor already selected.
document.addEventListener("langchange", function(){
  renderServices(); renderOptions(); calc();
});
