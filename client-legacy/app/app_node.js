const { getDistanceMatrix } = require('./getDistanceMatrix');
const { getPermutations } = require('./getPermutations');

async function main() {
  const locations = [
    '12307 Danny Dr, Austin TX 78759',
    "Julie's noodle, Austin TX",
    '11501 Alterra Pkwy, Austin TX 78758',
    'Kung Fu Tea, Austin TX',
    // 'Main Event, Austin TX',
    // 'ifly, Austin TX'
  ];

  const routes = getPermutations(locations.length).map((routes) => [
    0,
    ...routes,
  ]);
  const dMatrix = await getDistanceMatrix(locations, locations);
  const routeStats = routes.map((route) => {
    const segments = [];
    route.reduce((prev, curr) => {
      segments.push([prev, curr]);
      return curr;
    });
    const stats = segments.reduce(
      (acc, [origin, destination]) => {
        const { distance, duration } = dMatrix.rows[origin].elements[
          destination
        ];
        acc.distance += distance.value;
        acc.duration += duration.value;
        return acc;
      },
      { distance: 0, duration: 0 }
    );
    return {
      ...stats,
      route: route.map((i) => locations[i]),
      segments,
    };
  });
  const compare = (measurement) => (a, b) => a[measurement] - b[measurement];
  const shortestDurationRoute = routeStats.sort(compare('duration'))[0];
  console.log(
    `Shortest Time Routing: ${shortestDurationRoute.duration} seconds`
  );
  console.log(
    shortestDurationRoute.route.map((v, i) => `${i + 1}. ${v}`).join('\n')
  );
}

main();
