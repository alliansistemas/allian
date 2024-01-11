var searchOrigem = tomtom
.search()
.setKey('2inWVROkYfeGcxFvh3ueKhAjYeL7XPmG')
.init();

var searchDestino = tomtom
.search()
.setKey('2inWVROkYfeGcxFvh3ueKhAjYeL7XPmG')
.init();

// Configurar o autocompletar para os campos de origem e destino
var origemInput = document.getElementById('origem');
var destinoInput = document.getElementById('destino');

searchOrigem.setLocationInput(origemInput);
searchDestino.setLocationInput(destinoInput);