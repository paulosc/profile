// Hero backdrop: a small distributed system with events moving through it.
//
// Deliberately not particles or a starfield — the subject of this site is
// event-driven backends, so the drawing is a service graph with messages
// travelling the edges. Colours are read from the CSS custom properties, so
// the canvas follows the light/dark theme without knowing which one is on.

(function () {
  var canvas = document.getElementById("heroCanvas");
  if (!canvas) return;

  var reduce = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  var ctx = canvas.getContext("2d");
  var dpr = Math.min(window.devicePixelRatio || 1, 2);
  var W = 0, H = 0, running = true, raf = null;

  function css(name, fallback) {
    var v = getComputedStyle(document.documentElement).getPropertyValue(name).trim();
    return v || fallback;
  }

  var accent, ink, line;
  function readTheme() {
    accent = css("--accent", "#1B4FD8");
    ink = css("--ink-2", "#36414B");
    line = css("--line", "#D4DAE1");
  }

  // A deliberately small topology: edge → gateway → two services → queue →
  // workers → store. Positions are fractions of the canvas so it reflows.
  var NODES = [
    { x: 0.06, y: 0.50, r: 3.5 },
    { x: 0.22, y: 0.28, r: 5 },
    { x: 0.22, y: 0.72, r: 5 },
    { x: 0.40, y: 0.50, r: 7 },
    { x: 0.58, y: 0.24, r: 5 },
    { x: 0.58, y: 0.50, r: 5 },
    { x: 0.58, y: 0.76, r: 5 },
    { x: 0.76, y: 0.36, r: 6 },
    { x: 0.76, y: 0.64, r: 6 },
    { x: 0.93, y: 0.50, r: 4 }
  ];
  var EDGES = [
    [0, 1], [0, 2], [1, 3], [2, 3],
    [3, 4], [3, 5], [3, 6],
    [4, 7], [5, 7], [5, 8], [6, 8],
    [7, 9], [8, 9]
  ];

  // Messages ride an edge from one node to the next, then pick a continuation.
  var msgs = [];
  function outgoing(n) {
    var outs = [];
    for (var i = 0; i < EDGES.length; i++) if (EDGES[i][0] === n) outs.push(i);
    return outs;
  }
  function spawn(seed) {
    var outs = outgoing(0);
    if (!outs.length) return;
    msgs.push({
      e: outs[(seed | 0) % outs.length],
      t: -(seed % 7) * 0.14,
      speed: 0.0035 + ((seed * 37) % 10) * 0.00028
    });
  }
  for (var i = 0; i < 7; i++) spawn(i);

  function resize() {
    var rect = canvas.getBoundingClientRect();
    W = rect.width; H = rect.height;
    canvas.width = Math.round(W * dpr);
    canvas.height = Math.round(H * dpr);
    ctx.setTransform(dpr, 0, 0, dpr, 0, 0);
  }

  function pt(n) { return { x: NODES[n].x * W, y: NODES[n].y * H }; }

  function draw() {
    ctx.clearRect(0, 0, W, H);

    // edges
    ctx.lineWidth = 1;
    ctx.strokeStyle = line;
    ctx.globalAlpha = 0.55;
    for (var i = 0; i < EDGES.length; i++) {
      var a = pt(EDGES[i][0]), b = pt(EDGES[i][1]);
      ctx.beginPath();
      ctx.moveTo(a.x, a.y);
      ctx.lineTo(b.x, b.y);
      ctx.stroke();
    }

    // nodes
    ctx.globalAlpha = 0.5;
    for (var n = 0; n < NODES.length; n++) {
      var p = pt(n);
      ctx.beginPath();
      ctx.arc(p.x, p.y, NODES[n].r, 0, Math.PI * 2);
      ctx.strokeStyle = ink;
      ctx.lineWidth = 1.2;
      ctx.stroke();
    }

    // messages in flight
    ctx.globalAlpha = 1;
    for (var m = 0; m < msgs.length; m++) {
      var msg = msgs[m];
      if (msg.t < 0) continue;
      var e = EDGES[msg.e];
      var s = pt(e[0]), d = pt(e[1]);
      var x = s.x + (d.x - s.x) * msg.t;
      var y = s.y + (d.y - s.y) * msg.t;

      var g = ctx.createRadialGradient(x, y, 0, x, y, 9);
      g.addColorStop(0, accent);
      g.addColorStop(1, "transparent");
      ctx.globalAlpha = 0.28;
      ctx.fillStyle = g;
      ctx.beginPath();
      ctx.arc(x, y, 9, 0, Math.PI * 2);
      ctx.fill();

      ctx.globalAlpha = 0.95;
      ctx.fillStyle = accent;
      ctx.beginPath();
      ctx.arc(x, y, 2.1, 0, Math.PI * 2);
      ctx.fill();
    }
    ctx.globalAlpha = 1;
  }

  function step() {
    for (var m = 0; m < msgs.length; m++) {
      var msg = msgs[m];
      msg.t += msg.speed;
      if (msg.t >= 1) {
        var next = outgoing(EDGES[msg.e][1]);
        if (next.length) {
          msg.e = next[(Math.floor(msg.t * 1000) + m) % next.length];
          msg.t = 0;
        } else {
          // reached the store; re-enter at the edge
          var outs = outgoing(0);
          msg.e = outs[m % outs.length];
          msg.t = -0.5;
        }
      }
    }
    draw();
    raf = running ? requestAnimationFrame(step) : null;
  }

  function start() {
    if (raf || !running) return;
    raf = requestAnimationFrame(step);
  }
  function stop() {
    running = false;
    if (raf) { cancelAnimationFrame(raf); raf = null; }
  }

  readTheme();
  resize();

  if (reduce) {
    draw();          // one static frame, no animation
  } else {
    // Stop paying for frames when the hero is off screen or the tab is hidden.
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) {
        if (en.isIntersecting) { running = true; start(); }
        else { running = false; if (raf) { cancelAnimationFrame(raf); raf = null; } }
      });
    }, { threshold: 0 });
    io.observe(canvas);
    document.addEventListener("visibilitychange", function () {
      if (document.hidden) { running = false; if (raf) { cancelAnimationFrame(raf); raf = null; } }
      else { running = true; start(); }
    });
    start();
  }

  window.addEventListener("resize", function () { resize(); if (reduce) draw(); });
  document.addEventListener("langchange", function () { readTheme(); });
  var mq = window.matchMedia("(prefers-color-scheme: dark)");
  (mq.addEventListener ? mq.addEventListener.bind(mq, "change") : mq.addListener.bind(mq))(function () {
    readTheme();
    if (reduce) draw();
  });
})();
