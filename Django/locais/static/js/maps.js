function initMap() {
        var uluru = {lat: -6.805643, lng: -35.074629};
        var map = new google.maps.Map(document.getElementById('map'), {
          zoom: 14,
          center: uluru
        });
        var marker = new google.maps.Marker({
          position: uluru,
          map: map
        });
      }

function upMap(latitude,longitude) {
        var uluru = {lat:parseFloat(latitude), lng:parseFloat(longitude)};
        var map = new google.maps.Map(document.getElementById('map'), {
          zoom: 14,
          center: uluru
        });
        var marker = new google.maps.Marker({
          position: uluru,
          map: map
        });
      }