
var origin = ['Houston, Texas',
  'Denver, Colorado',
  'Dallas, Texas'];


var destination = origin;

// Test case: Generate an array of all permutations
var numDestinations = origin.length-1; // for example, 3 destinations, excluding the origin
TestRoute = RouteComb(numDestinations); // Construct an object RouteComb
console.log(TestRoute.comb); // permutation array
console.log(TestRoute.comb.length); // number of permutations

// console.log(TestRoute.comb.length);


origins = origin.join('|');
destinations = destination.join('|');
// travelTimes = [];
travelTime = 0;
minTravelTime = 0;
minTravelTime_i = 0;


(async () => {
  const result = await getDistanceMatrix(origins,destinations);
  
  console.log(JSON.stringify(result, null, 2));
  console.log(result.rows[0].elements[1].duration.value);
  console.log(result.rows[1].elements[2].duration.value);
  console.log(result.rows[0].elements[2].duration.value);
  console.log(result.rows[2].elements[1].duration.value);
  
  // Add travel time of the first pair
  for (i=0; i<TestRoute.comb.length; ++i) {
    travelTime = 0;
    for (j=0; j<TestRoute.comb[0].length-1; ++j) {
      travelTime += result.rows[TestRoute.comb[i][j]].elements[TestRoute.comb[i][j+1]].duration.value;
    }
    if (i==0) {
      minTravelTime = travelTime;
    }
    else if (travelTime < minTravelTime) {
        minTravelTime = travelTime;
        minTravelTime_i = i;
    }
  }
  // console.log(minTravelTime);
  // console.log(minTravelTime_i);
  // console.log(TestRoute.comb[minTravelTime_i]);
  // console.log(origin[0]);
  // TestRoute.comb[minTravelTime_i].forEach((origin.[])=>console.log(`Travel route is ${origin.[]}`));
  optimalRoute = (TestRoute.comb[minTravelTime_i].map((index) => origin[index]));
  console.log(`The optimal travel route is: ${optimalRoute.join(' -> ')}.`);
  // travelTimes.forEach((travelTime)=>console.log(`Travel Time is ${travelTime}`));

})();






/*
const travelInfo = new Object({
  this.
  

});
*/

/*
for (i=0; i<TestRoute.comb.length-1; ++i) {
  for (j=0; ) {
    TestRoute.comb[i];
  }
}
*/


function getDistanceMatrix(origin, destination) {
  return new Promise((resolve, reject) => {
    // HTTP Request to Google Map API
    // For now we use a set of example GPS coordinates
    const api_key = 'AIzaSyDtZvRnTEtBj8SP7tClaNxJRx5lrwmVASE';
    // API KEY from Yining's old Python code
    const api_endpoint = "https://maps.googleapis.com/maps/api/distancematrix/json";

    var mode = 'driving'; // driving, walking, bicycling, transit
    var params = {
        'origins': origins,
        'destinations': destinations, 
        // 'units': 'imperial',
        'key': api_key,
        'mode': mode
    };
    
    const request = require('request');
    request({url: api_endpoint, qs: params}, (error, response, body) => {
      if (error) {
        return reject(error.message);
      }
      else {
        if (response.statusCode != 200) {
          reject(`status code: ${response.statusCode}`);
        } else {
          resolve(JSON.parse(body));
        }
      }
    })
  })
}


/*
var request = require('request');
request({url: api_endpoint, qs: params}, callback);

function callback(error, response, body) {
  if (error) {
    return console.error('Error:', error);
  }
  if (!error && response.statusCode == 200) {
    info = JSON.parse(body);
    console.log("Travel duration in seconds: " + info.rows[0].elements[0].duration.value);
  }
}
*/

function RouteComb(numDestn) {
  /*
  Generate route combinations, given a number of destinations, excluding the
  origin. For example, if you are at A and you have 2 destinations (B and C),
  numDestn is 2.
  Note: Currently, we assume you do not return to the origin (A), but in a 
  future update, we will include such a parameter that allows you to return to
  the origin or not.
  */

  const RouteComb = {}; // Create an object
  RouteComb.numDestn = numDestn;
  RouteComb.dest = [];
  RouteComb.comb = [];
  
  for (var i=1; i<=numDestn; RouteComb.dest.push(i), i++);
  // Generate an array of destination indices from 1 to n, as 0 is reserved for
  // the origin.

  RouteComb.comb = permutator(RouteComb.dest);
  // Generate all permutations

  var origin = 0;
  for (var i=0; i<RouteComb.comb.length; RouteComb.comb[i].unshift(0), i++);
  // Add origin 0 to the array

  return RouteComb;
}


function permutator(inputArr) {
// Generate all permutations
  var results = [];
  function permute(arr, memo) {
    var cur, memo = memo || [];
  
    for (var i=0; i<arr.length; i++) {
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
