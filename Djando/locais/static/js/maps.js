var map;
function initMap() {
  map = new google.maps.Map(document.getElementById('map'), {
    center: {lat: -6.805643, lng: -35.074629},
    zoom: 14,
    draggable: false,
    zoomControl: false,
    scrollwheel: false
  });
  //map.getMaximumResolution=function() {
//    return 14;
//  };
//  map.getMinimumResolution=function() {
//      return 19;
//  };
}
