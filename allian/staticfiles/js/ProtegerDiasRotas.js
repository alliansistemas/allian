var rotaId;
$('#confirmarDelecao').on('show.bs.modal', function (event) {
    var button = $(event.relatedTarget)
    rotaId = button.data('rota')})