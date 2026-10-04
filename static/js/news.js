/*
 * Carrossel de novidades da home.
 *
 * Base: um scroller horizontal com scroll-snap (rola e dá swipe sem JS).
 * Com JS: avança sozinho a cada INTERVAL ms, animando o scrollLeft com LERP
 * (interpolação linear: a cada quadro anda uma fração da distância restante,
 * o que dá uma chegada suave que desacelera).
 *
 * Acessibilidade: botão de pausar/retomar, pausa em hover/foco/aba oculta/
 * fora da tela, e nenhuma rotação automática com prefers-reduced-motion.
 */
(function () {
  var root = document.querySelector('[data-news]');
  if (!root) return;

  var INTERVAL = 5500;   // ms entre slides
  var LERP = 0.1;        // fração da distância percorrida por quadro (a 60 fps)

  var viewport = root.querySelector('[data-news-viewport]');
  var slides = Array.prototype.slice.call(root.querySelectorAll('[data-news-slide]'));
  var section = root.closest('section');
  var controls = section.querySelector('[data-news-controls]');
  var dotsWrap = root.querySelector('[data-news-dots]');
  var prevBtn = section.querySelector('[data-news-prev]');
  var nextBtn = section.querySelector('[data-news-next]');
  var toggleBtn = section.querySelector('[data-news-toggle]');
  if (!viewport || slides.length < 2) return;

  var reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)');

  var index = 0;
  var target = 0;
  var lerpRaf = 0;
  var tickRaf = 0;
  var lastTime = 0;
  var elapsed = 0;
  var userPaused = false;
  var hovering = false;
  var focusing = false;
  var onScreen = true;
  var dragging = false;
  var settleTimer = 0;

  // --- UI -----------------------------------------------------------------

  var dots = slides.map(function (_, i) {
    var b = document.createElement('button');
    b.type = 'button';
    b.className = 'news__dot';
    b.setAttribute('aria-label', 'Ir para a novidade ' + (i + 1) + ' de ' + slides.length);
    b.innerHTML = '<span></span>';
    b.addEventListener('click', function () { goTo(i); });
    dotsWrap.appendChild(b);
    return b;
  });

  controls.hidden = false;
  dotsWrap.hidden = false;
  if (reduceMotion.matches) toggleBtn.hidden = true;

  function markActive() {
    dots.forEach(function (d, i) {
      var on = i === index;
      d.classList.toggle('is-active', on);
      if (on) d.setAttribute('aria-current', 'true'); else d.removeAttribute('aria-current');
      d.style.setProperty('--p', on && !reduceMotion.matches && !userPaused ? 0 : 1);
    });
  }

  // --- Posição / LERP -------------------------------------------------------

  function leftOf(i) {
    var max = viewport.scrollWidth - viewport.clientWidth;
    return Math.max(0, Math.min(slides[i].offsetLeft, max));
  }

  function stopLerp() {
    if (lerpRaf) cancelAnimationFrame(lerpRaf);
    lerpRaf = 0;
    viewport.style.scrollSnapType = '';
  }

  function lerpStep(now) {
    var dt = Math.min(now - (lerpStep.last || now), 64) || 16;
    lerpStep.last = now;
    var current = viewport.scrollLeft;
    var diff = target - current;

    if (Math.abs(diff) < 0.75) {
      viewport.scrollLeft = target;
      lerpRaf = 0;
      lerpStep.last = 0;
      viewport.style.scrollSnapType = '';
      return;
    }
    // Mesmo comportamento em 60/120/144 Hz: a fração é ajustada pelo tempo do quadro.
    var k = 1 - Math.pow(1 - LERP, dt / 16.67);
    var step = diff * k;
    // scrollLeft pode arredondar para inteiro; garante pelo menos 1px de avanço.
    if (Math.abs(step) < 1) step = diff > 0 ? 1 : -1;
    viewport.scrollLeft = current + step;
    lerpRaf = requestAnimationFrame(lerpStep);
  }

  function goTo(i) {
    index = (i + slides.length) % slides.length;
    target = leftOf(index);
    elapsed = 0;
    markActive();

    if (reduceMotion.matches) {
      viewport.scrollLeft = target;
      return;
    }
    viewport.style.scrollSnapType = 'none'; // o snap brigaria com a interpolação
    if (!lerpRaf) {
      lerpStep.last = 0;
      lerpRaf = requestAnimationFrame(lerpStep);
    }
    resume();
  }

  // --- Rotação automática ---------------------------------------------------

  function canPlay() {
    return !reduceMotion.matches && !userPaused && !hovering && !focusing &&
      !dragging && onScreen && !document.hidden;
  }

  function tick(now) {
    tickRaf = 0;
    if (!canPlay()) { lastTime = 0; return; }
    var dt = lastTime ? Math.min(now - lastTime, 100) : 0;
    lastTime = now;
    elapsed += dt;
    dots[index].style.setProperty('--p', Math.min(elapsed / INTERVAL, 1));
    if (elapsed >= INTERVAL) { goTo(index + 1); return; }
    tickRaf = requestAnimationFrame(tick);
  }

  function resume() {
    if (!tickRaf && canPlay()) { lastTime = 0; tickRaf = requestAnimationFrame(tick); }
  }

  // --- Eventos ----------------------------------------------------------------

  prevBtn.addEventListener('click', function () { goTo(index - 1); });
  nextBtn.addEventListener('click', function () { goTo(index + 1); });

  toggleBtn.addEventListener('click', function () {
    userPaused = !userPaused;
    toggleBtn.setAttribute('aria-pressed', String(userPaused));
    toggleBtn.setAttribute('aria-label', userPaused ? 'Retomar rotação automática' : 'Pausar rotação automática');
    toggleBtn.firstElementChild.className = userPaused ? 'fas fa-play' : 'fas fa-pause';
    root.classList.toggle('is-paused', userPaused);
    markActive();
    resume();
  });

  root.addEventListener('mouseenter', function () { hovering = true; });
  root.addEventListener('mouseleave', function () { hovering = false; resume(); });
  section.addEventListener('focusin', function () { focusing = true; });
  section.addEventListener('focusout', function () { focusing = false; resume(); });

  // Gesto do usuário (toque, arrasto, roda) cancela a animação automática.
  var releaseTimer = 0;
  function release() { dragging = false; resume(); }
  function userTookOver() {
    stopLerp();
    dragging = true;
    elapsed = 0;
    clearTimeout(releaseTimer);
    releaseTimer = setTimeout(release, 1500); // rede de segurança (clique sem rolagem)
  }
  viewport.addEventListener('pointerdown', userTookOver);
  viewport.addEventListener('wheel', userTookOver, { passive: true });
  viewport.addEventListener('keydown', userTookOver);

  viewport.addEventListener('scroll', function () {
    if (lerpRaf) return; // rolagem causada pela nossa animação
    clearTimeout(settleTimer);
    settleTimer = setTimeout(function () {
      // Rolagem do usuário terminou: descobre o slide mais próximo.
      var pos = viewport.scrollLeft;
      var best = 0;
      slides.forEach(function (s, i) {
        if (Math.abs(leftOf(i) - pos) < Math.abs(leftOf(best) - pos)) best = i;
      });
      dragging = false;
      if (best !== index) { index = best; elapsed = 0; markActive(); }
      resume();
    }, 140);
  }, { passive: true });

  document.addEventListener('visibilitychange', resume);

  if ('IntersectionObserver' in window) {
    new IntersectionObserver(function (entries) {
      onScreen = entries[0].isIntersecting;
      resume();
    }, { threshold: 0.25 }).observe(root);
  }

  window.addEventListener('resize', function () {
    stopLerp();
    viewport.scrollLeft = target = leftOf(index);
  });

  reduceMotion.addEventListener('change', function () {
    toggleBtn.hidden = reduceMotion.matches;
    if (reduceMotion.matches) stopLerp(); else resume();
  });

  markActive();
  resume();
})();
