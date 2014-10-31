(function() {
  var animate_css;

  animate_css = function(jquery_elem, motion) {
    jquery_elem.addClass('animated ' + motion);
    return jquery_elem.one('webkitAnimationEnd mozAnimationEnd MSAnimationEnd oanimationend animationend', function() {
      return jquery_elem.removeClass('animated ' + motion);
    });
  };

  $('#contact').click(function() {
    $('#home').removeClass('active');
    $('#contact').addClass('active');
    $('#explain').html('Contact us -> Issue to <a href="https://github.com/lazy-night/iplatform/issues">GitHub</a>');
    return animate_css($('#explain'), 'fadeIn');
  });

  $('#home').click(function() {
    $('#contact').removeClass('active');
    $('#home').addClass('active');
    $('#explain').html('PaaS engine using Docker.');
    return animate_css($('#explain'), 'fadeIn');
  });

  $('#login').click(function() {
    $('#home').removeClass('active');
    $('#contact').removeClass('active');
    return $('#login').addClass('active');
  });

}).call(this);
