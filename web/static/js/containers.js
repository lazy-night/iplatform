(function() {
  var animate_css, vm;

  animate_css = function(jquery_elem, motion) {
    jquery_elem.addClass('animated ' + motion);
    return jquery_elem.one('webkitAnimationEnd mozAnimationEnd MSAnimationEnd oanimationend animationend', function() {
      return jquery_elem.removeClass('animated ' + motion);
    });
  };

  $('.icon-btn').click(function() {
    return animate_css($(this), 'rubberBand');
  });

  vm = new Vue({
    el: '#vue-container',
    data: {
      header: "Create docker container",
      launch: false,
      dashboard: true,
      graph: false,
      settings: false
    },
    methods: {
      activate_launch: function() {
        this.header = "Create docker container";
        this.launch = true;
        this.dashboard = false;
        this.graph = false;
        return this.settings = false;
      },
      activate_dashborad: function() {
        this.header = "List docker containers";
        this.launch = false;
        this.dashboard = true;
        this.graph = false;
        return this.settings = false;
      },
      activate_graph: function() {
        this.header = "Docker container's condition";
        this.launch = false;
        this.dashboard = false;
        this.graph = true;
        return this.settings = false;
      },
      activate_settings: function() {
        this.header = "User settings";
        this.launch = false;
        this.dashboard = false;
        this.graph = false;
        return this.settings = true;
      }
    }
  });

  $('#navbar-launch').click(function() {
    return vm.activate_launch();
  });

  $('#navbar-dashboard').click(function() {
    return vm.activate_dashborad();
  });

  $('#navbar-graph').click(function() {
    return vm.activate_graph();
  });

  $('#navbar-settings').click(function() {
    return vm.activate_settings();
  });

  $('#nav-launch').click(function() {
    return vm.activate_launch();
  });

  $('#nav-dashboard').click(function() {
    return vm.activate_dashborad();
  });

  $('#nav-graph').click(function() {
    return vm.activate_graph();
  });

  $('#nav-settings').click(function() {
    return vm.activate_settings();
  });

  $('#img-launch').click(function() {
    return vm.activate_launch();
  });

  $('#img-dashboard').click(function() {
    return vm.activate_dashborad();
  });

  $('#img-graph').click(function() {
    return vm.activate_graph();
  });

  $('#img-settings').click(function() {
    return vm.activate_settings();
  });

}).call(this);