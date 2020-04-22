$(function () {
  // START: Do things when URL parameters present during page loading

  // Lozad
  const observer_1 = lozad('.lozad', {
    rootMargin: '0px', // syntax similar to that of CSS Margin
    threshold: 0 // ratio of element convergence
  });

  const observer_2 = lozad('.lozad', {
    rootMargin: '200px 0px', // syntax similar to that of CSS Margin
    threshold: 0 // ratio of element convergence
  });

  const observer_3 = lozad('.lozad', {
    rootMargin: '600px 0px', // syntax similar to that of CSS Margin
    threshold: 0 // ratio of element convergence
  });

  observer_1.observe();

  setTimeout(function () {
    observer_2.observe();
  }, 5000);

  setTimeout(function () {
    observer_3.observe();
  }, 10000);
  // END: Lozad

  if (typeof $meta_og_image_0 == 'undefined') {
    $meta_og_image_0 = $('#meta_og_image').attr('content');
  }

  const filterCat = document.querySelectorAll('.maincontent .filter-button');
  const filterE = document.querySelectorAll('.maincontent .filterE');

  function urlParams() {
    let params = new URLSearchParams(window.location.search);
    return {
      path: window.location.href.split('?')[0],
      category: params.get('category') === null ? [] : params.get('category').split(','),
      photo: params.get('photo')
    };
  }

  let params_onLoading = urlParams();
  var activeCatList = params_onLoading.category;
  // console.log(activeCatList);

  // Activate filter on loading if URL parameters are present
  if (activeCatList.length > 0) {
    toggleFilterCat(activeCatList);
    toggleFilterE(activeCatList);
  }

  // Activate modal on loading if URL parameters are present
  if (params_onLoading.photo != null) {
    let $photoid = $("#" + params_onLoading.photo);

    // Use large modal if photo is landscape
    if ($photoid.children('div').attr('class').indexOf('photo-landscape') > -1) {
      $('#imagemodal>div').attr('class', $('#imagemodal>div').attr('class') + ' modal-lg');
    }

    let $image_src = $photoid.find('img').attr('data-src');
    $('.modal-img').attr('src', $image_src);
    $('p.modal-photo-title').text($photoid.find('p.photo-title').text());
    $('p.modal-photo-location').text($photoid.find('p.photo-location').text());
    $('p.modal-photo-category').text();
    $('#imagemodal').modal('show');
    // $('#meta_og_image').attr('content', $image_src);
  }

  // Filter when clicked
  filterCat.forEach(cat => {
    cat.addEventListener('click', () => {
      if (cat.dataset.class === 'all') {
        activeCatList = [];
      }
      else {
        if (activeCatList.includes(cat.dataset.class)) {
          activeCatList = activeCatList.filter(e => e !== cat.dataset.class);
        }
        else {
          activeCatList.push(cat.dataset.class);
        }
      }

      toggleFilterCat(activeCatList);
      toggleFilterE(activeCatList);

      let param = window.location.href.split('?')[0];
      // This might cause problems in corner cases
      if (activeCatList.length === 1) {
        param = param.concat('?category=', activeCatList[0]);
      }
      if (activeCatList.length > 1) {
        param = param.concat('?category=', activeCatList.join(','));
      }

      window.history.replaceState(null, null, param);
    });
  })

  function toggleFilterCat(activeCatList) {
    testList = activeCatList.join('|');
    filterCat.forEach(cat => {
      if (activeCatList.length === 0) {
        if (cat.dataset.class === 'all') {
          cat.classList.add('active');
        }
        else {
          cat.classList.remove('active');
        }
      }
      else {
        if (testList.includes(cat.dataset.class)) {
          cat.classList.add('active');
        }
        else {
          cat.classList.remove('active');
        }
      }
    })
  }

  function toggleFilterE(activeCatList) {
    if (activeCatList.length === 0) {
      filterE.forEach(e => {
        e.style.display = 'block';
      })
    }
    else {
      filterE.forEach(e => {
        if (activeCatList.every(a => e.dataset.class.includes(a))) {
          e.style.display = 'block';
        }
        else {
          e.style.display = 'none';
        }
      })
    }
  }

  // Open modal
  $('.gallery .pop').click(function () {

    // Use large modal if photo is landscape
    if ($(this).children('div').children('div').attr('class').indexOf('photo-landscape') > -1) {
      $('#imagemodal>div').attr('class', $('#imagemodal>div').attr('class') + ' modal-lg');
    }

    let $image_src = $(this).find('img').attr('data-src');
    $('.modal-img').attr('src', $image_src);
    $('p.modal-photo-title').text($(this).find('p.photo-title').text());
    $('p.modal-photo-location').text($(this).find('p.photo-location').text());

    let categoryInfoArr = $(this)
      .find('div')
      .attr('data-class')
      .split(' ');

    categoryInfoArr.forEach(function (e, i) {
      if (e === 'bnw') {
        this[i] = 'B&W';
      }
      else if (e === '') {
        this[i] = 'None';
      }
      else {
        e = e.replace('_', ' ');
        this[i] = e.replace('_', ' ').charAt(0).toUpperCase() + e.slice(1);
      }
    }, categoryInfoArr);

    if (categoryInfoArr.length === 1) {
      categoryInfoStr = 'Category: '.concat(categoryInfoArr[0]);
    }
    else {
      categoryInfoStr = 'Categories: '.concat(categoryInfoArr.join(', '));
    }

    $('p.modal-photo-category').text(categoryInfoStr);
    $('#imagemodal').modal('show');

    let url = window.location.href;
    url = (url.indexOf('?') > -1) ? url.concat('&') : url.concat('?');
    url = url.concat('photo=', $(this).attr('id'));
    window.history.replaceState(null, null, url);

    $('#meta_og_image').attr('content', $image_src);
    $('#meta_og_url').attr('content', window.location.href);
  });

  // Click anywhere to close modal
  $(document).click(e => {
    if (e.button == 0) {
      $('#imagemodal').modal('hide');
    }
  });

  // Update URL when modal is closed
  $('#imagemodal').on('hidden.bs.modal', () => {

    // Return to normal-size modal
    if ($('#imagemodal>div').attr('class').indexOf('modal-lg') > -1) {
      $('#imagemodal>div').attr('class', 'modal-dialog modal-dialog-centered');
    }

    let url_modalClosed = urlParams();
    let url = '';
    if (url_modalClosed.category.length === 0) {
      url = url_modalClosed.path;
    }
    else {
      url = url.concat(url_modalClosed.path, '?category=', url_modalClosed.category);
    }
    window.history.replaceState(null, null, url);

    $('#meta_og_image').attr('content', $meta_og_image_0);
    $('#meta_og_url').attr('content', url);
  })

  // Back to top button
  var backToTopButton = document.getElementById("back-to-top-button");

  window.onscroll = () => {
    if (document.body.scrollTop > 2000 || document.documentElement.scrollTop > 2000) {
      backToTopButton.style.display = "block";
    } else {
      backToTopButton.style.display = "none";
    }
  };

  $('#back-to-top-button').click(function () {
    $('html,body').animate({ scrollTop: 0 }, 'slow');
    return false;
  })

  $('#nav-icon, #nav-icon-demo').click(function () {
    $(this).toggleClass('open');
  });

});
