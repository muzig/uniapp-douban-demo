from flask import Flask

app = Flask(__name__)


@app.route('/index/detail')
def detail():
    with open("detail.json", 'r') as f:
        return f.read()
