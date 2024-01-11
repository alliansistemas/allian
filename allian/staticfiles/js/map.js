var mapElement = document.getElementById('map');
var lat_origem = mapElement.getAttribute('data-lat-origem');
var lng_origem = mapElement.getAttribute('data-lng-origem');
var lat_destino = mapElement.getAttribute('data-lat-destino');
var lng_destino = mapElement.getAttribute('data-lng-destino');
var lat_media = (parseFloat(lat_origem) + parseFloat(lat_destino)) / 2;
var lng_media = (parseFloat(lng_origem) + parseFloat(lng_destino)) / 2;
var map = L.map('map').setView([lat_media, lng_media], 13);
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
  attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>',
  maxZoom: 18,
}).addTo(map);
var origemMarker = L.marker([lat_origem, lng_origem]).addTo(map);
var destinoMarker = L.marker([lat_destino, lng_destino]).addTo(map);
function tracarRota(origem, destino) {
  var apiKey = '2inWVROkYfeGcxFvh3ueKhAjYeL7XPmG';
  var url = 'https://api.tomtom.com/routing/1/calculateRoute/' + origem + ':' + destino + '/json?key=' + apiKey;
  fetch(url)
    .then(response => response.json())
    .then(data => {
      var routeCoordinates = data.routes[0].legs[0].points.map(point => [point.latitude, point.longitude]);
      var rota = L.polyline(routeCoordinates, { color: 'red' }).addTo(map);
      map.fitBounds(rota.getBounds().pad(0.1), {
        maxZoom: 15,
      });
    })
    .catch(error => { console.error('Erro ao obter a rota:', error); });
}
tracarRota(lat_origem + ',' + lng_origem, lat_destino + ',' + lng_destino);