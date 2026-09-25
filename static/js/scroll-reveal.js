/*
 * Scroll reveal progressivo: elementos com a classe "reveal" ficam visíveis
 * por padrão (CSS). Só entram no estado "oculto até aparecer" se este script
 * rodar, o navegador suportar IntersectionObserver e o usuário não tiver
 * pedido menos animação — assim nada depende de JS para ser visível.
 */
(function () {
  var prefersReducedMotion = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  if (prefersReducedMotion || !('IntersectionObserver' in window)) {
    return;
  }

  document.documentElement.classList.add('js-reveal-ready');

  var elements = document.querySelectorAll('.reveal');

  var observer = new IntersectionObserver(
    function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add('is-visible');
          observer.unobserve(entry.target);
        }
      });
    },
    { threshold: 0.15, rootMargin: '0px 0px -40px 0px' }
  );

  elements.forEach(function (el) {
    observer.observe(el);
  });

  // Rede de segurança: se por qualquer motivo o observer não disparar para
  // algum elemento (ex.: geometria incomum, bugs de navegador), garante que
  // nada fique invisível para sempre.
  window.setTimeout(function () {
    elements.forEach(function (el) {
      el.classList.add('is-visible');
    });
    observer.disconnect();
  }, 2500);
})();
