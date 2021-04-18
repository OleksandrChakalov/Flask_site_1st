from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('hello.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/<string:name>')
def greeting(name: str):
    return f'<h1>Hello {name.capitalize()}!<h1>'


if __name__ == '__main__':
    app.run()
