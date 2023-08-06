/* global google */

/**
 * --------------------------------------------------------------------------
 * CoreUI Pro Boostrap Admin Template (2.0.1): google-maps.js
 * Licensed under MIT (https://coreui.io/license)
 * --------------------------------------------------------------------------
 */

/* eslint-disable no-magic-numbers, no-unused-vars */

function InitMap() {
   window.map = new google.maps.Map(document.getElementById('mapa-lojas'), {
        mapTypeId: google.maps.MapTypeId.ROADMAP
    });

    let infowindow = new google.maps.InfoWindow();
    let bounds = new google.maps.LatLngBounds();
    for (let i = 0; i < locations.length; i++) {
        // Adiciona os pontos no mapa
        marker = new google.maps.Marker({
            position: new google.maps.LatLng(locations[i][1], locations[i][2]),
            map: map,
            title: locations[i][0],
            icon: locations[i][4],
        });
        if (locations.length == 1){
            var listener = google.maps.event.addListener(map, "idle", function () {
            map.setZoom(15);
            google.maps.event.removeListener(listener);
        });
        }
        bounds.extend(marker.position);

        google.maps.event.addListener(marker, 'click', (function (marker, i) {
            return function () {
                infowindow.setContent(locations[i][0]);
                infowindow.open(map, marker);
            }
        })(marker, i));
    }

    map.fitBounds(bounds);


}

if (window.google && window.google.maps) {
  InitMap();
}

//# sourceMappingURL=google-maps.js.map