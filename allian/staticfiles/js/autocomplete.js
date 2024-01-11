$(document).ready(function() {
    // Inicializa o autocomplete para o campo de texto de origem
    $("#origem").autocomplete({
      apiKey: "2inWVROkYfeGcxFvh3ueKhAjYeL7XPmG",
      source: function(request, response) {
        // Chama a API TOMTOM Places para obter as sugestões de endereços
        var url = "https://api.tomtom.com/places/v1/search/autocomplete?q=" + request.term;
        $.get(url, function(data) {
          response(data.results);
        });
      }
    });
  
    // Inicializa o autocomplete para o campo de texto de destino
    $("#destino").autocomplete({
      apiKey: "2inWVROkYfeGcxFvh3ueKhAjYeL7XPmG",
      source: function(request, response) {
        // Chama a API TOMTOM Places para obter as sugestões de endereços
        var url = "https://api.tomtom.com/places/v1/search/autocomplete?q=" + request.term;
        $.get(url, function(data) {
          response(data.results);
        });
      }
    });
  });
  