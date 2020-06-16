function initMap() {
  $('#route-opt-form').submit(function (e) {
    // Prevent reload page
    e.preventDefault();

    let origin = $('#route-opt-input').val().split('\n');
    origin = origin.filter((item) => item);

    if (origin.length > 10) {
      alert('Please enter up to 10 destinations.');
      return;
    }

    const destination = origin;
    const numDestinations = origin.length - 1; // for example, 3 destinations, excluding the origin
    TestRoute = RouteComb(numDestinations); // Construct an object RouteComb
    let travelTime = 0;
    let minTravelTime = 0;
    let minTravelTime_i = 0;

    const service = new google.maps.DistanceMatrixService();

    service.getDistanceMatrix(
      {
        origins: origin,
        destinations: destination,
        travelMode: 'DRIVING',
        // unitSystem: google.maps.UnitSystem.METRIC,
        avoidHighways: false,
        avoidTolls: false,
      },
      function (response, status) {
        if (status !== 'OK') {
          // alert('Error was: ' + status);
          $('#optimal-route').html('Error occurred.');
        } else {
          // Add travel time of the first pair
          for (i = 0; i < TestRoute.comb.length; ++i) {
            travelTime = 0;
            for (j = 0; j < TestRoute.comb[0].length - 1; ++j) {
              travelTime +=
                response.rows[TestRoute.comb[i][j]].elements[
                  TestRoute.comb[i][j + 1]
                ].duration.value;
            }
            if (i == 0) {
              minTravelTime = travelTime;
            } else if (travelTime < minTravelTime) {
              minTravelTime = travelTime;
              minTravelTime_i = i;
            }
          }
          optimalRoute = TestRoute.comb[minTravelTime_i].map(
            (index) => origin[index]
          );
          $('#optimal-route').html(optimalRoute.join(' &rarr; '));
        }
      }
    );

    function RouteComb(numDestn) {
      const RouteComb = {}; // Create an object
      RouteComb.numDestn = numDestn;
      RouteComb.dest = [];
      RouteComb.comb = [];

      for (let i = 1; i <= numDestn; ++i) {
        RouteComb.dest.push(i);
      }
      // Generate an array of destination indices from 1 to n, as 0 is reserved for
      // the origin.

      RouteComb.comb = permutator(RouteComb.dest);
      // Generate all permutations

      if (document.getElementById('returnToOrigin').checked) {
        RouteComb.comb.forEach((e) => {
          e.unshift(0);
          e.push(0);
          return e;
        });
        // Add origin 0 to the array. 0 represents the origin
      } else if (document.getElementById('notReturnToOrigin').checked) {
        RouteComb.comb.forEach((e) => e.unshift(0));
        // Add origin 0 to the array. 0 represents the origin
      }

      return RouteComb;
    }

    function permutator(inputArr) {
      // Generate all permutations
      const results = [];
      function permute(arr, memo) {
        let cur;
        var memo = memo || [];

        for (let i = 0; i < arr.length; ++i) {
          cur = arr.splice(i, 1);
          if (arr.length === 0) {
            results.push(memo.concat(cur));
          }
          permute(arr.slice(), memo.concat(cur));
          arr.splice(i, 0, cur[0]);
        }
        return results;
      }
      return permute(inputArr);
    }
  });
}
