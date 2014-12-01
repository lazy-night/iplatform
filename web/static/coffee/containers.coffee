animate_css = (jquery_elem, motion) ->
    jquery_elem.addClass 'animated ' + motion
    jquery_elem.one('webkitAnimationEnd mozAnimationEnd MSAnimationEnd oanimationend animationend', () -> jquery_elem.removeClass 'animated ' + motion)

$('.icon-btn').click ->
    animate_css($(this), 'rubberBand')

vm = new Vue
    el: '#vue-container'
    data:
        header: "List docker containers"
        launch: false
        dashboard: true
        graph: false
        settings: false
    methods:
        activate_launch: ->
            this.header = "Create docker container"
            this.launch = true
            this.dashboard = false
            this.graph = false
            this.settings = false
        activate_dashborad: ->
            this.header = "List docker containers"
            this.launch = false
            this.dashboard = true
            this.graph = false
            this.settings = false
        activate_graph: ->
            this.header = "Docker container's condition"
            this.launch = false
            this.dashboard = false
            this.graph = true
            this.settings = false
        activate_settings: ->
            this.header = "User settings"
            this.launch = false
            this.dashboard = false
            this.graph = false
            this.settings = true
    

$('#navbar-launch').click -> vm.activate_launch()
$('#navbar-dashboard').click -> vm.activate_dashborad()
$('#navbar-graph').click -> vm.activate_graph()
$('#navbar-settings').click -> vm.activate_settings()

$('#nav-launch').click -> vm.activate_launch()
$('#nav-dashboard').click -> vm.activate_dashborad()
$('#nav-graph').click -> vm.activate_graph()
$('#nav-settings').click -> vm.activate_settings()

$('#img-launch').click -> vm.activate_launch()
$('#img-dashboard').click -> vm.activate_dashborad()
$('#img-graph').click -> vm.activate_graph()
$('#img-settings').click -> vm.activate_settings()

$ ->
  $('.dropdown-menu a').click ->
    u_visibleTag = $(this).parents('ul').attr('u_visibleTag')
    u_hiddenTag = $(this).parents('ul').attr('u_hiddenTag')
    $(u_visibleTag).html($(this).attr('value'))
    $(u_hiddenTag).val($(this).attr('value'))

$('#container-name').keyup ->
  cc = $('#create-container')
  if $(this).val()
    cc.removeClass('btn-warning')
    cc.addClass('btn-success')
    cc.val('Launch')
    cc.removeAttr('disabled')
  else
    cc.removeClass('btn-success')
    cc.addClass('btn-warning')
    cc.val('Get ready')
    cc.attr('disabled', 'disabled')

$('.application').click ->
  $('.application').each( -> $(this).removeClass('enabled') )
  $(this).addClass('enabled')

get_image = () ->
  os = 'ubuntu'
  return os + ':' + $('#u_visibleValue').text()

get_app = () ->
  app = $('.application' + '.enabled')
  return app.attr("alt")

get_port = () ->
  sl = $('#port').val().split(',')
  l = []
  for s in sl
    l.push(Number(s))
  return l

get_sshkey = () ->
  return $('#ssh-key').val()

get_tag = () ->
  return $('#container-name').val()

$('#create-container').click ->
  d =
    image: get_image()
    app: get_app()
    port: get_port()
    id_rsa_pub: get_sshkey()
    tag: get_tag()
  js = JSON.stringify(d)
  #$('body').prepend("<div id='over'>")
  #$('#over').fadeIn(200)
  #$('spinner').removeClass('visible-false')
  #$('spinner').addClass('visible-true')


  $.ajax '/launch',
    type: 'post'
    data: js
    contentType: "application/json"
    success: (status) ->
      #alert('success')
      alert(status)
      #$('#over').remove()
      #$('spinner').removeClass('visible-true')
      #$('spinner').addClass('visible-false')
      location.reload();
    error: (status) ->
      #alert('error')
      alert(status)
      #$('#over').remove()
      #$('spinner').removeClass('visible-true')
      #$('spinner').addClass('visible-false')
      location.reload();
