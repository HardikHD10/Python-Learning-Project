import random
from flask import Flask

app = Flask(__name__)

num = random.randint(0, 9)


@app.route('/')
def hello():
    return '<h1>Welcome to number Guessing Game!</h1>' \
           '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif">'


@app.route('/<int:guess>')
def number(guess):
    if guess < num:
        return '<h1>Number too low!</h1>' \
               '<img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif">'
    elif guess > num:
        return '</h1>Number too High!</h1>' \
               '<img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif">'
    else:
        return '<h1>Correct guess!</h1>' \
               '<img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif">'


if __name__ == "__main__":
    app.run(debug=True)
