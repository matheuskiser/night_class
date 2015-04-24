var infowindow = new google.maps.InfoWindow();
var geocoder = new google.maps.Geocoder();

var map = new google.maps.Map(document.getElementById('map-canvas'), {
    zoom: 10,
    mapTypeId: google.maps.MapTypeId.ROADMAP
});

// Sets map to center at current location
if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(function (position) {
        var pos = new google.maps.LatLng(position.coords.latitude, position.coords.longitude);
        map.setCenter(pos);
    });
}

// Gets ViewPort lat and long once map is loaded
google.maps.event.addListener(map, 'idle', function () {
    var upper_left_lat = map.getBounds().getNorthEast().lat();
    var upper_left_lng = map.getBounds().getNorthEast().lng();
    var lower_left_lat = map.getBounds().getSouthWest().lat();
    var lower_left_lng = map.getBounds().getSouthWest().lng();

    $.ajax({
        method: 'GET',
        url: '',
        data: {
            'upper_left_lat': upper_left_lat,
            'upper_left_lng': upper_left_lng,
            'lower_left_lat': lower_left_lat,
            'lower_left_lng': lower_left_lng
        },
        success: function (data) {
            // Remove all elements from main div
            var parentDiv = document.getElementById('places-content');
            parentDiv.innerHTML = "";

            // Parse through response
            var json = $.parseJSON(data);
            $(json).each(function (i, val) {
                geocodeAddress(val.address);

                //Creates all list items for what is shown in map
                addDiv(val.name, val.address, val.rating, val.user_name);
            });

        },
        error: function (data) {
            alert("There was an error. Please, try again later.");
        }
    });
});

function geocodeAddress(address) {
    geocoder.geocode({'address': address}, function (results, status) {
        if (status == google.maps.GeocoderStatus.OK) {
            createMarker(results[0].geometry.location, address);
        }
    });
}

function createMarker(latlng, html) {
    var marker = new google.maps.Marker({
        position: latlng,
        map: map
    });

    google.maps.event.addListener(marker, 'mouseover', function () {
        infowindow.setContent(html);
        infowindow.open(map, marker);
    });

    google.maps.event.addListener(marker, 'mouseout', function () {
        infowindow.close();
    });
}

function addDiv(name, address, rating, user_name) {
    var parentDiv = document.getElementById('places-content');
    var newDiv = document.createElement("div");
    newDiv.className = "item";

    var newUserName = document.createElement("span");
    newUserName.className = "item-user-name";
    newUserName.innerHTML = user_name;
    newDiv.appendChild(newUserName);

    var newName = document.createElement("span");
    newName.className = "item-name";
    newName.innerHTML = name;
    newDiv.appendChild(newName);

    var newAddress = document.createElement("span");
    newAddress.className = "item-address";
    newAddress.innerHTML = address;
    newDiv.appendChild(newAddress);

    var newRating = document.createElement("span");
    newRating.className = "item-rating";
    newRating.innerHTML = rating;
    newDiv.appendChild(newRating);

    parentDiv.appendChild(newDiv);
}