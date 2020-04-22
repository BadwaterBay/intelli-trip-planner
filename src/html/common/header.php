<!-- Header -->
<header id="masthead-image" class="masthead
<?php
if (defined('MASTHEAD_SIZE')) {
  if (MASTHEAD_SIZE == 'SM') {
    echo ' masthead-sm';
  }
}
?> lozad
<?php
if (!(defined('FADE_IN')) || FADE_IN == 'no')
  echo ' fade-in-fast';
elseif (FADE_IN == 'yes')
  echo ' fade-in-slow';
?>
">
  <div class="overlay"></div>
  <div class="container">
    <div class="row">
      <div class="col-12 mx-auto col-xl-10">
        <?php
        if (!defined('HEADER_TYPE') || HEADER_TYPE == 'site') {
          echo '<div class="page-heading';
          if (!(defined('FADE_IN')) || FADE_IN == 'no')
            echo ' slide-in-bottom-fast';
          elseif (FADE_IN == 'yes')
            echo ' slide-in-bottom';
          echo '">', "\r\n",
            '<h1>',
            SITE_TITLE,
            '</h1>',
            "\r\n",
            '<div class="subheading">',
            SITE_SUBTITLE,
            '</div>',
            "\r\n";
        } elseif (HEADER_TYPE == 'blogpost') {
          echo '<div class="post-heading">', "\r\n",
            '<h1>',
            SITE_TITLE,
            '</h1>',
            "\r\n",
            '<h2 class="subheading">',
            SITE_SUBTITLE,
            '</h2>',
            "\r\n",
            '<div class="meta">',
            SITE_SUBSUBTITLE,
            '</div>',
            "\r\n";
        }
        ?>
      </div>
    </div>
  </div>
  </div>
</header>