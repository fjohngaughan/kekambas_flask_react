from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def hello_world():
    context = {
        'title': 'Kekambas Blog | HOME',
        'customer_name': 'Brian',
        'customer_username': 'bstanton',
        'items': {
            1: 'Ice Cream',
            2: 'Bread',
            3: 'Lemons',
            4: 'Cereal'
        },
        'followers': [
            {
                'username': 'sdavitt',
                'created_at': '2021-02-28'
            },
            {
                'username': 'jcarter',
                'created_at': '2021-03-01'
            }
        ]
    }
    return render_template('index.html', **context)


@app.route('/register')
def register():
    title = "Kekambas Blog | REGISTER"
    return render_template('register.html', title=title)