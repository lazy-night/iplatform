module.exports = (grunt) ->
    pkg = grunt.file.readJSON 'package.json'
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
        connect:
            options:
                port: 5000
                host: 'localhost'
        watch:
            coffee:
                files: ['coffee/*.coffee']
                tasks: ['coffee']
            sass:
                files: ['sass/*.sass']
                tasks: ['sass']
            options:
                livereload: 35729
            html:
                files: ['../templates/*.html']
                tasks: ['']
    
    for taskName of pkg.devDependencies when taskName.substring(0, 6) is 'grunt-'
            grunt.loadNpmTasks taskName

    grunt.registerTask 'default', ['coffee', 'sass']
