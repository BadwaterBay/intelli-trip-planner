<!-- Config -->
<?php
if ($_SERVER['HTTP_HOST'] === 'localhost') {
  if (strpos(dirname(__FILE__), 'build/release')) {
    define('PATH', 'http://localhost/ProjectMyWeb/build/release/public_html');
  } elseif (strpos(dirname(__FILE__), 'ProjectMyWeb/src')) {
    define('PATH', 'http://localhost/ProjectMyWeb/src/public_html');
  } elseif (strpos(dirname(__FILE__), 'ProjectNextGen/src')) {
    define('PATH', 'http://localhost/App/ProjectNextGen/src');
  }
} else
    define("PATH", 'https://skylerdong.com');
    // define("PATH", $_SERVER['HTTP_HOST']);
?>
