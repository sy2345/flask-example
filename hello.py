from flask import Flask
from markupsafe import escape

app = Flask(__name__)

@app.route('/')
def index():
    return \
f'''
<html>
  <head>
    <title>index</title>
  </head>
</html>

'''


@app.route('/hello')
def hello():
    return 'Hello, World'

@app.route("/<name>")
def hello2(name):
    return f"Hello, {escape(name)}!"

@app.route('/user/<username>')
def profile(username):
    return f'{username}\'s profile'