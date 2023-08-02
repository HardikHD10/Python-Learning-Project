from flask import Flask, render_template
from post import Post
import requests


app = Flask(__name__)


posts = requests.get("https://api.npoint.io/2275a660cfe5aec03397").json()
post_objects = []
for post in posts:
    post_obj = Post(post["id"], post["title"], post["subtitle"], post["body"])
    post_objects.append(post_obj)


@app.route('/')
def home():
    return render_template("index.html",posts=post_objects)


@app.route('/blog/<int:num>')
def blog(num):
    requested_post = None
    for blog_post in post_objects:
        if blog_post.id == num:
            requested_post = blog_post
    return render_template("post.html",posts=requested_post)

if __name__ == "__main__":
    app.run(debug=True)

from flask import request


def shutdown_server():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()


@app.get('/shutdown')
def shutdown():
    shutdown_server()
    return 'Server shutting down...'
