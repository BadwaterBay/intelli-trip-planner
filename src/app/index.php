<!doctype html>
<html lang="en">

<head>
  <meta charset="utf-8" />
  <meta http-equiv="X-UA-Compatible" content="IE=edge" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <link rel="stylesheet" type="text/css" href="https://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/4.4.0/css/bootstrap.min.css">
  <link rel="stylesheet" type="text/css" href="./styles.min.css">
  <title>Route Optimization</title>
</head>

<body>
  <div class="container maincontent">
    <div class="row">
      <div class="col-12 mb-3">
        <div>
          <h1>Route Optimization</h1>
        </div>
        <div>
          <p>Enter up to 10 destinations, one per line.</p>
          <p>It is assumed that (1) the first location is the origin and (2) you don't return back to the origin.</p>
          <form action="javascript:void(0);" method="post" id="route-opt-form">
            <textarea type="text" id="route-opt-input" placeholder="Destinations" required autofocus rows="10" cols="35"></textarea><br>
            <button type="submit">Submit</button>
          </form>
        </div>
        <hr />
        <div>
          <p>The optimal route is:</p>
          <p id="optimal-route"></p>
        </div>
        <hr />
        <div>
          <p>We use Google Distance Matrix API and Google Map JavaScript API with a customized optimization algorithm to
            calculate the fastest route.</p>
        </div>
      </div>
      <!--column-->
    </div>
    <!--row-->
  </div>
  <!--maincontent-->
  <script type="text/javascript" src="https://code.jquery.com/jquery-3.5.1.min.js" integrity="sha256-9/aliU8dGd2tb6OSsuzixeV4y/faTqgFtohetphbbj0=" crossorigin="anonymous"></script>
  <script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/twitter-bootstrap/4.4.0/js/bootstrap.min.js"></script>
  <script type="text/javascript" src="./app.js"></script>
  <?php include_once('./API_KEY_GOOG_route-optimization_dev.php'); ?>
  <script defer src=<?php echo 'https://maps.googleapis.com/maps/api/js?key=', GOOGMAPS_APIKEY, '&callback=initMap'; ?>></script>
</body>

</html>
