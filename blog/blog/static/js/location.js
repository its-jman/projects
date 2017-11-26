<!--GEOLOCATION BORROWED FROM W3 SCHOOLS-->
var x = document.getElementById("demo");

function getLocation() {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(showPosition, showError);
    } else {
        x.innerHTML = "Geolocation is not supported by this browser.";
    }
}

function showPosition(position) {
    var latlon = position.coords.latitude + "," + position.coords.longitude;

    var img_url = "http://maps.googleapis.com/maps/api/staticmap?center="
        + latlon + "&zoom=14&size=400x300&sensor=false";

    $('#map').attr('src', img_url);
    $('.popup').fadeToggle(350);
}

function showError(error) {
    switch (error.code) {
        case error.PERMISSION_DENIED:
            x.innerHTML = "User denied the request for Geolocation.";
            break;
        case error.POSITION_UNAVAILABLE:
            x.innerHTML = "Location information is unavailable.";
            break;
        case error.TIMEOUT:
            x.innerHTML = "The request to get user location timed out.";
            break;
        case error.UNKNOWN_ERROR:
            x.innerHTML = "An unknown error occurred.";
            break;
    }
}

// http://stackoverflow.com/questions/1403615/use-jquery-to-hide-a-div-when-the-user-clicks-outside-of-it
$(document).mouseup(function (e) {
    var container = $('.popup-inner');
    var outerContainer = $('.popup');

    if (outerContainer.css('display') === 'block' && // If the map is currently displayed
        !container.is(e.target) && // if the target of the click isn't the container...
        container.has(e.target).length === 0 && // ... nor a descendant of the container
        e.target.className === 'popup') { // And you are clicking on the grey area

        outerContainer.fadeToggle(350);
    }
});
