/*
 * Filtro por categoria. Cada .filter-bar tem botões [data-filter] e filtra os
 * elementos [data-category] da mesma <section>/<main>. "all" mostra tudo.
 * Mantém aria-pressed em sincronia e avisa o resultado em [data-filter-status].
 */
(function () {
  document.querySelectorAll('.filter-bar').forEach(function (bar) {
    var scope = bar.closest('section') || document;
    var status = scope.querySelector('[data-filter-status]');
    var buttons = bar.querySelectorAll('[data-filter]');

    buttons.forEach(function (button) {
      button.addEventListener('click', function () {
        buttons.forEach(function (b) {
          b.classList.remove('is-active');
          b.setAttribute('aria-pressed', 'false');
        });
        button.classList.add('is-active');
        button.setAttribute('aria-pressed', 'true');

        var category = button.getAttribute('data-filter');
        var shown = 0;
        scope.querySelectorAll('[data-category]').forEach(function (card) {
          var match = category === 'all' || card.getAttribute('data-category') === category;
          card.hidden = !match;
          if (match) shown += 1;
        });
        if (status) status.textContent = shown + (shown === 1 ? ' item exibido' : ' itens exibidos');
      });
    });
  });
})();