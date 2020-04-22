<?php
  if ($_SERVER["SERVER_NAME"] == "localhost") {
    require_once '../../../login/API_KEY_GOOG_route-optimization_dev.php';
  }
  else {
    require_once '../../../login/API_KEY_GOOG_route-optimization_public.php';
  }
  define("SITE_TITLE",'App: Route Optimization');
  define("SITE_SUBTITLE",'Find the fastest route with multiple stops using JavaScript and Google Map API.');
  define("FADE_IN",'no');
  define("FOOTER_COLOR",'dark');
  define("OG_IMAGE",'https://skylerdong.com/images/other/SD-IMG_4854-Edit-Web.jpg');
?>
<!doctype html>
<html lang="en">
<?php include_once '../../common/config.php'; ?>
<head>
<?php include_once '../../common/head.php';?>
<title>Route Optimization</title>
<link rel="canonical" href="https://route-optimization.app.skylerdong.com" />
</head>
<body>
<?php
  include_once '../../common/navbar.php';
  include_once './app.php';
  include_once '../../common/footer.php';
?>
<script defer src="<?php echo PATH; ?>/app/route-optimization/app.js"></script>
<script type="text/javascript" defer src="https://maps.googleapis.com/maps/api/js?key=<?php echo API_KEY_GOOGLE; ?>&callback=initMap"></script>
</script>
</body>
</html>
