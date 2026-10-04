/*
 * Lista completa de certificações: filtro por área, busca por texto e
 * "Mostrar mais" progressivo (a lista começa curta para não virar um paredão).
 * Sem JS a lista inteira continua visível e navegável.
 *
 * A área pode vir pela URL: /certificados?tema=Python
 */
(function () {
  var tools = document.querySelector('[data-cert-tools]');
  var list = document.querySelector('[data-cert-list]');
  if (!tools || !list) return;

  var PAGE = 12;
  var items = Array.prototype.slice.call(list.children);
  var pills = tools.querySelectorAll('[data-tema]');
  var search = tools.querySelector('[data-cert-search]');
  var status = document.querySelector('[data-cert-status]');
  var empty = document.querySelector('[data-cert-empty]');
  var more = document.querySelector('[data-cert-more]');

  var tema = '';
  var termo = '';
  var limite = PAGE;

  function normalizar(s) {
    return s.toLowerCase().normalize('NFD').replace(/[̀-ͯ]/g, '');
  }
  items.forEach(function (li) { li.dataset.busca = normalizar(li.dataset.busca || ''); });

  function render() {
    var casam = items.filter(function (li) {
      return (!tema || li.dataset.tema === tema) && (!termo || li.dataset.busca.indexOf(termo) !== -1);
    });
    var filtrando = tema || termo;
    var visiveis = filtrando ? casam.length : Math.min(limite, casam.length);

    items.forEach(function (li) { li.hidden = true; });
    casam.slice(0, visiveis).forEach(function (li) { li.hidden = false; });

    status.textContent = casam.length === items.length
      ? 'Mostrando ' + visiveis + ' de ' + items.length + ' certificações'
      : casam.length + (casam.length === 1 ? ' certificação encontrada' : ' certificações encontradas');
    empty.hidden = casam.length !== 0;
    more.hidden = filtrando || visiveis >= casam.length;
    more.textContent = 'Mostrar mais (' + (casam.length - visiveis) + ')';
  }

  function selecionar(valor, atualizarUrl) {
    tema = valor;
    pills.forEach(function (b) {
      var on = b.dataset.tema === valor;
      b.classList.toggle('is-active', on);
      b.setAttribute('aria-pressed', String(on));
    });
    if (atualizarUrl && window.history && history.replaceState) {
      var url = new URL(location.href);
      if (valor) url.searchParams.set('tema', valor); else url.searchParams.delete('tema');
      history.replaceState(null, '', url);
    }
    render();
  }

  pills.forEach(function (b) {
    b.addEventListener('click', function () { selecionar(b.dataset.tema, true); });
  });
  search.addEventListener('input', function () {
    termo = normalizar(search.value.trim());
    render();
  });
  more.addEventListener('click', function () {
    limite += PAGE;
    render();
    var primeiroNovo = items.filter(function (li) { return !li.hidden; })[limite - PAGE];
    var link = primeiroNovo && primeiroNovo.querySelector('a');
    if (link) link.focus({ preventScroll: true }); // teclado continua de onde parou
  });

  var inicial = new URL(location.href).searchParams.get('tema') || '';
  var existe = Array.prototype.some.call(pills, function (b) { return b.dataset.tema === inicial; });
  selecionar(existe ? inicial : '', false);
})();
