import time

from flask import Flask

app = Flask(__name__)

print(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


# if __name__ == "__main__":
#     app.run()

# python decorator Function
def delay_decorator_function(function):
    def wrapper_function():
        time.sleep(2)
        # do something before
        function()
        # do something after

    return wrapper_function


@delay_decorator_function
def say_hello():
    print("Hello")

# same as :
# decorated_function = delay_decorator_function(say_hello)
# decorated_function()


say_hello()
