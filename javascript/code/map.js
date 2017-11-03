
function initialize(id) {

    // Set map options
    var parisLocation = new google.maps.LatLng(48.8, 2.33);

    var mapOptions = {
        zoom      : 2,
        center    : parisLocation,
        mapTypeId : google.maps.MapTypeId.ROADMAP
    };

    /**
     * private property containing the data from AJAX
     */
    var data;

    // Object model of our webapp
    var GM = {
        // public properties
        map       : new google.maps.Map(document.getElementById(id), mapOptions),
        markers   : [],
        lines     : [],

        getData   : function () {
            // Accessing the private variable data though closure
            return data;
        },

        getLatLng : function (key){
            return new google.maps.LatLng(data.points[key].lat, data.points[key].lng);
        },

        addMarker : function (latlng, title){

            var marker = new google.maps.Marker({
                position : latlng,
                map      : this.map,
                title    : title
            });

            this.markers.push(marker);

            // Example of this binding
            var that = this;

            google.maps.event.addListener(marker, 'click', function (e) {
                // If you want to access the GM, you have to use the 'that'
                //that.resetMap();
                this.setAnimation(google.maps.Animation.BOUNCE);
            });
        },

        addLine : function (o){
            var line = new google.maps.Polyline({
                map           : this.map,
                geodesic      : true,
                path          : o.path,
                strokeOpacity : o.opacity,
                strokeWeight  : 4,
                strokeColor   : 'blue'
            });
            this.lines.push(line);
        },

        computeMaxPrice : function() {
            var n = data.flights.length;
            var max_price = 0;

            for (var i=0; i<n; i++){
                var price = parseFloat(data.flights[i].price);
                if (price > max_price) {
                    max_price = price;
                }
            }
            return max_price;
        },

        handleData : function (p_data){
            // Storing in private member data
            data = p_data;

            if (typeof data.flights === "undefined"){
                return;
            }

            var max_price = this.computeMaxPrice();
            var n = data.flights.length;

            for (var i=0; i<n; i++){

                var flight = data.flights[i];
                var latlng_ori = this.getLatLng(flight.origin);
                var latlng_des = this.getLatLng(flight.destination);

                this.addMarker(latlng_ori, flight.origin);
                this.addMarker(latlng_des, flight.destination);

                this.addLine({
                    path    : [latlng_ori, latlng_des],
                    opacity : parseFloat(flight.price) / max_price
                });
            }

        },

        resetMap : function () {
            // Clean the map
            var i, c;
            for (i=0, c=this.markers.length; i<c; i++){
                this.markers[i].setMap(null);
            }
            for (i=0, c=this.lines.length; i<c; i++){
                this.lines[i].setMap(null);
            }
            // This crushes the arrays
            this.markers.length = 0;
            this.lines.length = 0;
        }
    };

    return GM;

}

// Done when the document is loaded
$(document).ready(function() {

    var GM = initialize('canvas');

    $('#canvas').css({
        'heigth' : 0.95 * $(window).height(),
        'width'  : 0.95 * $(window).width()
    });

    // At every key stroke inside the text field!
    $('#text').keyup(function () {

        var origin = $('#text').val();

        if (origin === '') {
            return;
        }

        // Sending the request for data
        // Here we target another domain, so this webservice has to allow
        // cross-origin-ressource-sharing (CORS)
        $.ajax({
            url      : 'http://localhost:5000/data/flights?origin=' + origin,
            dataType : 'json',
            success  : function (data) {
                GM.resetMap();
                GM.handleData(data);

                // Setting the label
                $('#go').html(' Query for ' + origin + ' (' + data.flights.length + ' results)');
            },
            error : function () {
                console.log('Ooooooh');
            }
        });

    });

});

