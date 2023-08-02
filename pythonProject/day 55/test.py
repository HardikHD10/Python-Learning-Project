from flask import Flask

app = Flask(__name__)


def make_bold(function):
    def wrapper():
        return "<b>" + function() + "</b>"
    return wrapper


def make_italics(function):
    def wrapper():
        return "<em>" + function() + "</em>"
    return wrapper


@app.route('/')
def hello_world():
    return '<h1>Hello World</h1>' \
           '<img src = "https://media.giphy.com/media/13PMpiayBvKFck/giphy.gif" width="200px"> '


@app.route("/bye")
@make_bold
@make_italics
def bye():
    return "Bye!"


@app.route("/username/<name>")
def greet(name):
    return f"Hello there {name}"


if __name__ == "__main__":
    app.run(debug=True)

