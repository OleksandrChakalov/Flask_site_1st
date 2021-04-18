from flask import Flask, render_template

app = Flask(__name__)

def get_films():
    return [
        {
            'id' : 1,
            'title' : 'Forsage 1',
            'release_day' : '2001'
        },
        {
            'id': 2,
            'title': 'Forsage 2',
            'release_day': '2002'
        }
    ]

@app.route('/')
def index():
    films = get_films()
    return render_template('hello.html', films = films)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/<string:name>')
def greeting(name: str):
    return f'<h1>Hello {name.capitalize()}!<h1>'


if __name__ == '__main__':
    app.run()
