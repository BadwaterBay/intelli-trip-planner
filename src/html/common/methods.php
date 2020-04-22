<?php

function loadImage_blog($image) {
  list($width, $height) = getimagesize('../images/blog/' . $image);
  $aspect = round($height / $width * 10000) / 100;
  echo '<div class="responsive-container" style="padding-bottom:', $aspect, '%;">', '<img class="lozad" data-src="../images/blog/', $image, '" alt="Blog - SkylerDong.com"></div>', "\r\n";
}

function loadImage_photography($image) {
  list($width, $height) = getimagesize('../images/photography/' . $image);
  $aspect = round($height / $width * 10000) / 100;
  echo '<div class="responsive-container" style="padding-bottom:', $aspect, '%;">', '<img class="lozad" data-src="../images/photography/', $image, '" alt="Photography - SkylerDong.com"></div>', "\r\n";
}

// Photography gallery

function modifyQueryStr_cat($str) {
  $str = str_replace("_", " ", $str);
  $str = htmlspecialchars($str);
  if (!strcmp($str, 'bnw'))
    $str = 'B&amp;W';
  $str = ucfirst($str);
  return $str;
}

function modifyQueryStr_title($str) {
  $str = ucfirst($str);
  $str = htmlspecialchars($str);
  $str = str_replace(' - ', ' &ndash; ', $str);
  $str = str_replace("\w'\w", '&apos;', $str);
  $str = str_replace("\w’\w", '&apos;', $str);
  return $str;
}

function modifyQueryStr_location($str) {
  $str = ucfirst($str);
  $str = htmlspecialchars($str);
  $str = str_replace(' - ', ' &ndash; ', $str);
  $str = str_replace("\w'\w", '&apos;', $str);
  return $str;
}
?>
