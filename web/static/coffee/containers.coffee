animate_css = (jquery_elem, motion) ->
    jquery_elem.addClass 'animated ' + motion
    jquery_elem.one('webkitAnimationEnd mozAnimationEnd MSAnimationEnd oanimationend animationend', () -> jquery_elem.removeClass 'animated ' + motion)

$('.icon-btn').click ->
    animate_css($(this), 'rubberBand')

vm = new Vue
    el: '#vue-container'
    data:
        header: "Create docker container"
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
