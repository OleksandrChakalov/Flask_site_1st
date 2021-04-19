from flask import Flask, render_template
from utils.view_modifiers import response

app = Flask(__name__)


def get_films():
    return [
        {
            'id': 1,
            'title': 'Forsage 1',
            'release_day': '2001'
        },
        {
            'id': 2,
            'title': 'Forsage 2',
            'release_day': '2002'
        }
    ]


@app.route('/')
@response(template_file='hello.html')
def index():
    films = get_films()
    return {'films': films}


@app.route('/about')
@response(template_file='about.html')
def about():
    # return render_template('about.html', title='About')
    return {'title': 'About'}


@app.route('/<string:name>')
def greeting(name: str):
    return f'<h1>Hello {name.capitalize()}!<h1>'


if __name__ == '__main__':
    app.run()
