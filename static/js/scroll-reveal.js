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

  document.querySelectorAll('.reveal').forEach(function (el) {
    observer.observe(el);
  });
})();
