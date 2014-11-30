# -*- encoding: utf-8 -*-

import json
from functools import wraps
from flask import Flask, render_template, session, g, \
                  request, redirect, url_for, flash

app = Flask(__name__)
app.config.from_object('config')

from web.database import db_session, User, insert_user, varify_user
from api.dockerclient import DockerClient

@app.before_request
def load_current_user():
    g.user = User.query.get(session['user_id']) \
        if 'user_id' in session else None


@app.teardown_request
def remove_db_session(exception):
    db_session.remove()


def requires_login(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if g.user is None:
            flash('You need to be signed in.')
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        name = request.form['name']
        password = request.form['password']
        user = varify_user(name, password)
        if user:
            session['user_id'] = user.id
            g.user = user
            return redirect(url_for('container'))

    return render_template('login.html')


@app.route('/signup', methods=['POST', 'GET'])
def signup():
    if request.method == 'POST':
        name = request.form['name']
        password = request.form['password']
        user = varify_user(name, password)
        if user == None:
            insert_user(name, password)
            return redirect(url_for('login'))

    return render_template('signup.html')


@app.route('/logout')
def logout():
    session.pop('user_id', None)
    return redirect(url_for('index'))


@app.route('/containers')
@requires_login
def container():
    name = g.user.name
    dockerc = DockerClient()
    images = dockerc.images(name=name)
    containers = dockerc.containers(name=name)
    return render_template('containers.html', **locals())


@app.route('/')
def index():
    return render_template('index.html', **locals())


def getPortAndPortbindings(port):
    if port == [0]:
        return None, None
    port_bindings = {}
    for p in port:
        port_bindings[p] = None
    return port, port_bindings

@app.route('/launch', methods=['POST'])
def launch():
    result = False
    if request.method == 'POST':
        inputdata = request.json
        image = inputdata['image']
        app = inputdata['app']
        port, port_bindings = getPortAndPortbindings(inputdata['port'])
        id_rsa_pub = inputdata['id_rsa_pub']
        tag = g.user.name + '/' + inputdata['tag']

        dockerc = DockerClient()
        dicimage = dockerc.build(
            image=image, app=app, port=port,
            id_rsa_pub=id_rsa_pub, tag=tag
        ) # {'Id': imageid, 'Repository': tag}
        container_id = dockerc.create_container(
            image=tag,
            command='/sbin/my_init',
            ports=port
        )
        result = dockerc.start(
            container=container_id,
            port_bindings=port_bindings
        ) # True or False
    return json.dumps({ 'result' : result })


@app.route('/delete_containers', methods=['POST'])
def delete_containers():
    result = False
    if request.method == 'POST':
        containers_id = request.json
        # containers_id=['aaaaa', 'bbbbb']
        dockerc = DockerClient()

        result = {}
        for cid in containers_id:
            res = False
            if dockerc.stop(container=cid) and dockerc.remove_container(container=cid):
                res = True
            result[cid] = res
    return json.dumps(result)


@app.route('/delete_images', methods=['POST'])
def delete_images():
    result = False
    if request.method == 'POST':
        images = request.json
        # images=['koide/aaaaa', 'koide/bbbbb']
        dockerc = DockerClient()

        result = {}
        for img in images:
            result[img] = dockerc.remove_image(image=img)
    return json.dumps(result)
