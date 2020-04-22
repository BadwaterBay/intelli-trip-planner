

var origin1 = new google.maps.LatLng(55.930385, -3.118425);
var origin2 = 'Greenwich, England';
var destinationA = 'Stockholm, Sweden';
var destinationB = new google.maps.LatLng(50.087692, 14.421150);

function calculateDistances(origins,destinations) {
    var service = new google.maps.DistanceMatrixService();
    var d = $.Deferred();
    service.getDistanceMatrix(
        {
            origins: [origin1, origin2],
            destinations: [destinationA, destinationB],
            travelMode: 'DRIVING',
            transitOptions: TransitOptions,
            drivingOptions: DrivingOptions,
            unitSystem: UnitSystem,
            avoidHighways: Boolean,
            avoidTolls: Boolean,
        },
        function(response, status){
            if (status != google.maps.DistanceMatrixStatus.OK) {
                d.reject(status);
            } else {
                d.resolve(response);
            }
        });
    return d.promise();
}

calculateDistances([origin1],[destinationA])
    .done(function(response){

        var origins = response.originAddresses;

        for (var i = 0; i < origins.length; i++) {
            var results = response.rows[i].elements;
            for (var j = 0; j < results.length; j++) {
                //console.log(results[j].distance.text);
                document.getElementById('result').innerHTML += results[j].distance.text;
            }
        }

    })
    .fail(function(status){
        document.getElementById('result').innerHTML = 'An error occured. Status: ' + status;
    });

    
