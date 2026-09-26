/*
 * Cada seção "surge" ao entrar na tela e "sai" ao deixá-la, continuamente,
 * conforme o visitante rola a página para cima ou para baixo.
 *
 * Caminho principal: scroll-driven CSS animation (animation-timeline: view())
 * definida em shell.css — roda nos dois sentidos automaticamente, sem JS.
 *
 * Este script só entra em ação quando o navegador NÃO suporta isso (ex.:
 * Firefox): aí ele assume via IntersectionObserver, alternando a classe
 * .is-visible para frente e para trás. Se o suporte nativo existir, o script
 * não faz nada — os elementos já ficam visíveis por padrão (sem a classe
 * .js-reveal-fallback, a regra de ocultar em shell.css nunca é ativada).
 */
(function () {
  var prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  if (prefersReducedMotion) {
    return;
  }

  var nativeSupport =
    'CSS' in window &&
    typeof CSS.supports === 'function' &&
    CSS.supports('(animation-timeline: view()) and (animation-range: entry)');

  if (nativeSupport) {
    return;
  }

  if (!('IntersectionObserver' in window)) {
    return;
  }

  document.documentElement.classList.add('js-reveal-fallback');

  var elements = document.querySelectorAll('.reveal');

  var observer = new IntersectionObserver(
    function (entries) {
      entries.forEach(function (entry) {
        entry.target.classList.toggle('is-visible', entry.isIntersecting);
      });
    },
    { threshold: 0.1, rootMargin: '0px 0px -8% 0px' }
  );

  elements.forEach(function (el) {
    observer.observe(el);
  });

  // Rede de segurança: se por algum motivo o observer nunca disparar para um
  // elemento, garante que nada fique invisível para sempre.
  window.setTimeout(function () {
    elements.forEach(function (el) {
      if (!el.classList.contains('is-visible')) {
        el.classList.add('is-visible');
      }
    });
  }, 4000);
})();
