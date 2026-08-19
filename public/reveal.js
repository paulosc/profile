// Reveals sections as they enter the viewport. Purely additive: if the
// observer is unavailable the class is applied immediately, so nothing can
// end up permanently invisible.
(function () {
  var els = document.querySelectorAll(".reveal");
  if (!els.length) return;
  if (!("IntersectionObserver" in window) ||
      window.matchMedia("(prefers-reduced-motion: reduce)").matches) {
    return;                       // leave everything visible, animate nothing
  }
  // Only now does hiding become safe: this class is what arms the CSS.
  document.documentElement.classList.add("js-reveal");
  var io = new IntersectionObserver(function (entries) {
    entries.forEach(function (en) {
      if (en.isIntersecting) { en.target.classList.add("in"); io.unobserve(en.target); }
    });
  }, { rootMargin: "0px 0px -8% 0px", threshold: 0.05 });
  els.forEach(function (e) { io.observe(e); });

  // Failsafe. Content that only becomes visible when JavaScript says so is one
  // bug away from an invisible page — which is exactly how this broke once.
  // After three seconds everything is shown regardless of what the observer did.
  setTimeout(function () {
    els.forEach(function (e) { e.classList.add("in"); });
  }, 3000);
})();
