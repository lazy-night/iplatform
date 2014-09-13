# IPLatform web interface

Web UI & Web Api

# For developer

develop by Python + Node.

### Server side

* Flask
* SQLAlchemy

### Frontend

* Node
  * Grunt
    * grunt-contrib-sass
	* grunt-contrib-coffee
	* grunt-contrib-watch
	* grunt-contrib-connect

## Environment for Python

Setup(require pip)

    $ pip install Flask Flask-SQLAlchemy

Run server

    $ python run.py

## Environment for Node

Setup(require npm)

    $ npm init
	$ npm install -g grunt-cli
	$ npm install --save-dev grunt
	$ npm install --save-dev grunt-contrib-sass
	$ npm install --save-dev grunt-contrib-coffee
	$ npm install --save-dev grunt-contrib-watch
	$ npm install --save-dev grunt-contrib-connect

Gruntfile.coffee

```coffeescript
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
```

* compile coffeescript
* compile sass
* watch coffeescript and sass
* live reload

Run grunt

    $ grunt watch
