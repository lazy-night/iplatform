(function() {
  var animate_css, get_app, get_image, get_port, get_sshkey, get_tag, vm;

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
      header: "List docker containers",
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

  $(function() {
    return $('.dropdown-menu a').click(function() {
      var u_hiddenTag, u_visibleTag;
      u_visibleTag = $(this).parents('ul').attr('u_visibleTag');
      u_hiddenTag = $(this).parents('ul').attr('u_hiddenTag');
      $(u_visibleTag).html($(this).attr('value'));
      return $(u_hiddenTag).val($(this).attr('value'));
    });
  });

  $('#container-name').keyup(function() {
    var cc;
    cc = $('#create-container');
    if ($(this).val()) {
      cc.removeClass('btn-warning');
      cc.addClass('btn-success');
      cc.val('Launch');
      return cc.removeAttr('disabled');
    } else {
      cc.removeClass('btn-success');
      cc.addClass('btn-warning');
      cc.val('Get ready');
      return cc.attr('disabled', 'disabled');
    }
  });

  $('.application').click(function() {
    $('.application').each(function() {
      return $(this).removeClass('enabled');
    });
    return $(this).addClass('enabled');
  });

  get_image = function() {
    var os;
    os = 'ubuntu';
    return os + ':' + $('#u_visibleValue').text();
  };

  get_app = function() {
    var app;
    app = $('.application' + '.enabled');
    return app.attr("alt");
  };

  get_port = function() {
    var l, s, sl, _i, _len;
    sl = $('#port').val().split(',');
    l = [];
    for (_i = 0, _len = sl.length; _i < _len; _i++) {
      s = sl[_i];
      l.push(Number(s));
    }
    return l;
  };

  get_sshkey = function() {
    return $('#ssh-key').val();
  };

  get_tag = function() {
    var user;
    user = 'yano';
    return user + '/' + $('#container-name').val();
  };

  $('#create-container').click(function() {
    var d, js;
    d = {
      image: get_image(),
      app: get_app(),
      port: get_port(),
      id_rsa_pub: get_sshkey(),
      tag: get_tag()
    };
    js = JSON.stringify(d);
    return $.ajax('/launch', {
      type: 'post',
      data: js,
      contentType: "application/json",
      success: function(status) {
        alert(status);
        return location.reload();
      },
      error: function(status) {
        alert(status);
        return location.reload();
      }
    });
  });

}).call(this);
