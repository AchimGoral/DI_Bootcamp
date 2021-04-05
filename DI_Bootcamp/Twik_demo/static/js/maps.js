let map;
let marker;
const coordinates = {lat: 32.062, lng: 34.779};

function initMap() {
    map = new google.maps.Map (document.getElementById("main"), {
        center: coordinates,
        zoom: 12,
    });

    function addMarker(coordinates){
        marker = new google.maps.Marker ({
            position: coordinates,
            map: map,
        });
    }

    addMarker(coordinates)
}