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
    visibleTag = $(this).parents('ul').attr('visibleTag')
    hiddenTag = $(this).parents('ul').attr('hiddenTag')
    $(visibleTag).html($(this).attr('value'))
    $(hiddenTag).val($(this).attr('value'))

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

# get_image = () ->
# 
# get_app = () ->
# 
# get_port = () ->
# 
# get_sshkey = () ->
# 
# get_tag = () ->
# 
# $('#create-container').click ->
#   data =
#     image: get_image()
#     app: get_app()
#     port: get_port()
#     id_rsa_pub: get_sshkey()
#     tag: get_tag()
# 
#   $.ajax '/launch'
#     type: 'post'
#     data: data
#     success: () ->
#     error: () ->
