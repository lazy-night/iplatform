# -*- encoding: utf-8 -*-

from functools import wraps
from flask import Flask, render_template, session, g, \
                  Markup, request, redirect, url_for, flash

app = Flask(__name__)
app.config.from_object('config')

from web.database import db_session, User, insert_user, varify_user

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
            return redirect(url_for('index'))

    return render_template('login.html')


@app.route('/add_user', methods=['POST'])
def add_user():
    name = request.form['name']
    password = request.form['password']
    insert_user(name, password)
    return redirect(url_for('login'))


@app.route('/logout')
def logout():
    session.pop('user_id', None)
    return redirect(url_for('login'))


@app.route('/')
@requires_login
def index():
    name = g.user.name
    return render_template('index.html', **locals())
