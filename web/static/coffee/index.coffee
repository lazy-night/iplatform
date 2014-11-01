animate_css = (jquery_elem, motion) ->
    jquery_elem.addClass 'animated ' + motion
    jquery_elem.one('webkitAnimationEnd mozAnimationEnd MSAnimationEnd oanimationend animationend', () -> jquery_elem.removeClass 'animated ' + motion)

$('#contact').click ->
    $('#home').removeClass 'active'
    $('#contact').addClass 'active'
    $('#explain').html 'Contact us -> Issue to <a href="https://github.com/lazy-night/iplatform/issues">GitHub</a>'
    animate_css($('#explain'), 'fadeIn')

$('#home').click ->
    $('#contact').removeClass 'active'
    $('#home').addClass 'active'
    $('#explain').html 'PaaS engine using Docker.'
    animate_css($('#explain'), 'fadeIn')

$('#login').click ->
    $('#home').removeClass 'active'
    $('#contact').removeClass 'active'
    $('#login').addClass 'active'
