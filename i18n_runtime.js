// Language detection and switching.
//
// No IP geolocation on purpose: it needs a third-party request, leaks every
// visitor's address to that provider, adds latency to first paint and gets it
// wrong behind a VPN. The browser already states the languages the person reads,
// which is both a better signal and nobody else's business. Time zone is only
// consulted as a location hint when the language list says nothing useful.

(function () {
  var SUPPORTED = ["en", "pt", "es"];
  var KEY = "lang";

  var TZ_PT = /^(America\/(Sao_Paulo|Bahia|Fortaleza|Recife|Belem|Manaus|Cuiaba|Campo_Grande|Porto_Velho|Boa_Vista|Rio_Branco|Maceio|Araguaina|Santarem|Eirunepe|Noronha)|Atlantic\/(Azores|Madeira)|Europe\/Lisbon|Africa\/(Luanda|Maputo|Bissau|Praia|Sao_Tome))$/;
  var TZ_ES = /^(America\/(Mexico_City|Cancun|Merida|Monterrey|Chihuahua|Mazatlan|Tijuana|Hermosillo|Bogota|Lima|Santiago|Caracas|Guayaquil|La_Paz|Asuncion|Montevideo|Panama|Costa_Rica|Guatemala|El_Salvador|Tegucigalpa|Managua|Havana|Santo_Domingo|Puerto_Rico|Argentina\/.*)|Atlantic\/Canary|Europe\/Madrid)$/;

  function fromNavigator() {
    var list = navigator.languages && navigator.languages.length
      ? navigator.languages
      : [navigator.language || ""];
    for (var i = 0; i < list.length; i++) {
      var base = String(list[i] || "").toLowerCase().split("-")[0];
      if (SUPPORTED.indexOf(base) > -1) return base;
    }
    return null;
  }

  function fromTimezone() {
    try {
      var tz = Intl.DateTimeFormat().resolvedOptions().timeZone || "";
      if (TZ_PT.test(tz)) return "pt";
      if (TZ_ES.test(tz)) return "es";
    } catch (e) { /* Intl unavailable — fall through to English */ }
    return null;
  }

  function stored() {
    try {
      var v = localStorage.getItem(KEY);
      return SUPPORTED.indexOf(v) > -1 ? v : null;
    } catch (e) { return null; }
  }

  function detect() {
    // An explicit choice always wins; ?lang= lets a link force one.
    var q = (location.search.match(/[?&]lang=([a-z]{2})/i) || [])[1];
    if (q && SUPPORTED.indexOf(q.toLowerCase()) > -1) return q.toLowerCase();
    return stored() || fromNavigator() || fromTimezone() || "en";
  }

  function apply(lang) {
    var dict = (window.I18N || {})[lang];
    if (!dict) return;

    document.documentElement.lang = lang;
    window.__lang = lang;

    document.querySelectorAll("[data-i18n]").forEach(function (el) {
      var v = dict[el.getAttribute("data-i18n")];
      if (v != null) el.innerHTML = v;
    });
    document.querySelectorAll("[data-i18n-html]").forEach(function (el) {
      var v = dict[el.getAttribute("data-i18n-html")];
      if (v != null) el.innerHTML = v;
    });
    document.querySelectorAll("[data-i18n-meta]").forEach(function (el) {
      var v = dict[el.getAttribute("data-i18n-meta")];
      if (v != null) el.setAttribute("content", v);
    });

    document.querySelectorAll(".langs button").forEach(function (b) {
      var on = b.getAttribute("data-lang") === lang;
      b.classList.toggle("on", on);
      b.setAttribute("aria-pressed", on ? "true" : "false");
    });

    // Let the quote configurator redraw itself in the new language.
    document.dispatchEvent(new CustomEvent("langchange", { detail: lang }));
  }

  function choose(lang) {
    try { localStorage.setItem(KEY, lang); } catch (e) { /* private mode */ }
    apply(lang);
  }

  function init() {
    document.querySelectorAll(".langs button").forEach(function (b) {
      b.addEventListener("click", function () { choose(b.getAttribute("data-lang")); });
    });
    apply(detect());
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }

  window.__setLang = choose;
})();
