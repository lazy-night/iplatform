# -*- encoding: utf-8 -*-

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
    containers = dockerc.containers(name=name)
    return render_template('containers.html', **locals())


@app.route('/')
def index():
    return render_template('index.html', **locals())
