module.exports = (grunt) ->
  grunt.initConfig
    coffee:
      compile:
        expand: true
        flatten: true
        src: ['coffee/*.coffee']
        dest: 'js'
        ext: '.js'
    sass:
      compile:
        expand: true
        flatten: true
        src: ['sass/*.sass']
        dest: 'css'
        ext: '.css'
    watch:
      coffee:
        files: ['coffee/*.coffee']
        tasks: ['coffee']
      sass:
        files: ['sass/*.sass']
        tasks: ['sass']

  grunt.loadNpmTasks 'grunt-contrib-watch'
  grunt.loadNpmTasks 'grunt-contrib-coffee'
  grunt.loadNpmTasks 'grunt-contrib-sass'
  grunt.registerTask 'default', ['coffee', 'sass']
