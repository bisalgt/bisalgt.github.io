from flask import Flask, url_for, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def hello_world():
    return 'Hello World'

def index(name):
    return name

app.add_url_rule('/<name>', 'index', index)


@app.route('/<int:id>')
def page2(id):
    return f"<h1>{id}</h1><a href={url_for('index', name='bishal bhai')}>linnk </a>"


@app.route('/<path:path>')
def page3(path):
    return f'<h1>Path: {path}</h1>'

from markupsafe import escape

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % escape(username)