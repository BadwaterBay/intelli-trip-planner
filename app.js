
// Test case: Generate an array of all permutations
var numDestinations = 3; // for example, 3 destinations, excluding the origin
TestRoute = RouteComb(numDestinations); // Construct an object RouteComb
console.log(TestRoute.comb); // permutation array
console.log(TestRoute.comb.length); // number of permutations


// HTTP Request to Google Map API
// For now we use a set of example GPS coordinates
var request = require('request');
var api_key = 'AIzaSyDtZvRnTEtBj8SP7tClaNxJRx5lrwmVASE';
// API KEY from Yining's old Python code
var api_endpoint = "https://maps.googleapis.com/maps/api/distancematrix/json";
var origin = '30.289029,-97.735392'; // this GPS coordinate is an example
var destination = '30.399866,-97.686537'; // this GPS coordinate is an example

params = {
    'origins': origin, 
    'destinations': destination, 
    'units': 'imperial',
    'key': api_key
};

request({url: api_endpoint, qs: params},
    function(error, response, body) {
    console.log(body);
});


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
