/*
 * Carrossel genérico com bolinhas de navegação (usado nos Certificados da
 * home e na Ficha Técnica do blog). Qualquer elemento marcado com
 * [data-carousel] vira um carrossel se tiver dentro dele:
 *   [data-carousel-track]  — o "trilho" que desliza (os filhos diretos são
 *                             os slides, cada um ocupando 100% da largura)
 *   [data-carousel-dots]   — onde as bolinhas de navegação são geradas
 *   [data-carousel-prev]   — botão "anterior" (opcional)
 *   [data-carousel-next]   — botão "próximo" (opcional)
 *
 * Slides escondidos via [hidden] (ex.: filtro de categoria) são ignorados
 * automaticamente — o carrossel só navega entre os visíveis.
 */
(function () {
  function initCarousel(root) {
    var track = root.querySelector('[data-carousel-track]');
    var dotsWrap = root.querySelector('[data-carousel-dots]');
    var prevBtn = root.querySelector('[data-carousel-prev]');
    var nextBtn = root.querySelector('[data-carousel-next]');
    if (!track || !dotsWrap) return;

    var index = 0;

    function visibleSlides() {
      return Array.prototype.filter.call(track.children, function (el) {
        return !el.hidden;
      });
    }

    function goTo(i) {
      index = i;
      render();
    }

    function render() {
      var slides = visibleSlides();

      if (!slides.length) {
        dotsWrap.innerHTML = '';
        if (prevBtn) prevBtn.disabled = true;
        if (nextBtn) nextBtn.disabled = true;
        return;
      }

      if (index >= slides.length) index = 0;
      if (index < 0) index = slides.length - 1;

      slides.forEach(function (slide, i) {
        slide.classList.toggle('is-active', i === index);
        // Slides fora de vista não recebem foco por teclado nem leitor de tela.
        slide.inert = i !== index;
      });

      dotsWrap.innerHTML = '';
      slides.forEach(function (_, i) {
        var dot = document.createElement('button');
        dot.type = 'button';
        dot.className = 'carousel-dot';
        dot.setAttribute('aria-label', 'Ir para o item ' + (i + 1) + ' de ' + slides.length);
        if (i === index) {
          dot.classList.add('is-active');
          dot.setAttribute('aria-current', 'true');
        }
        dot.addEventListener('click', function () { goTo(i); });
        dotsWrap.appendChild(dot);
      });

      track.style.transform = 'translateX(' + (index * -100) + '%)';

      var single = slides.length <= 1;
      if (prevBtn) prevBtn.disabled = single;
      if (nextBtn) nextBtn.disabled = single;
    }

    if (prevBtn) prevBtn.addEventListener('click', function () { goTo(index - 1); });
    if (nextBtn) nextBtn.addEventListener('click', function () { goTo(index + 1); });

    // Swipe horizontal (touch/caneta). Mouse continua usando as setas/bolinhas.
    var viewport = track.parentElement;
    var startX = null;
    viewport.addEventListener('pointerdown', function (e) {
      if (e.pointerType !== 'mouse') startX = e.clientX;
    });
    viewport.addEventListener('pointerup', function (e) {
      if (startX === null) return;
      var dx = e.clientX - startX;
      startX = null;
      if (Math.abs(dx) > 50) goTo(index + (dx < 0 ? 1 : -1));
    });
    viewport.addEventListener('pointercancel', function () { startX = null; });

    // Recalcula quando slides são escondidos/mostrados (ex.: filtro de categoria).
    new MutationObserver(function () { goTo(0); })
      .observe(track, { attributes: true, attributeFilter: ['hidden'], subtree: true });

    render();
  }

  document.querySelectorAll('[data-carousel]').forEach(initCarousel);
})();
