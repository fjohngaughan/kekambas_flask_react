from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def hello_world():
    title = "Kekambas Blog | HOME"
    return render_template('index.html', title=title)