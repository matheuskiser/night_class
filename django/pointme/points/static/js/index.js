// Index.html

$.ajax({
    method: 'GET',
    url: '/points/api/get_places/',
    data: {},
    success: function (data) {
        // Parse through response
        var json = $.parseJSON(data);
        $(json).each(function (i, val) {
            addDiv(val.name, val.address, val.rating, val.user_name);
        });
    },
    error: function (data) {
        alert("There was an error. Please, try again later.");
    }
});

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