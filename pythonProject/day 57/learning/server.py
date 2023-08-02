import random
import requests
from datetime import datetime

from flask import Flask, render_template

app = Flask(__name__)


def api(name):
    response_1 = requests.get(f"https://api.agify.io?name={name}")
    age = response_1.json()["age"]

    response_2 = requests.get(f"https://api.nationalize.io?name={name}")
    nationality = response_2.json()["country"][0]["country_id"]

    response_3 = requests.get(f"https://api.genderize.io?name={name}")
    gender = response_3.json()["gender"]

    return f"according to us your predicted age is {age}, your predicted nationality is {nationality}, and your predicted gender is {gender}"

@app.route('/')
def home():
    randon_number = random.randint(1,10)
    year = datetime.now().year
    return render_template("index.html",num=randon_number,year=year)

@app.route('/guess/<name>')
def return_parameter(name):
    message_user = api(name)
    return render_template("index.html",message = message_user)

@app.route('/blog/<num>')
def blog(num):
    blog_url = "https://api.npoint.io/2275a660cfe5aec03397"
    response = requests.get(blog_url)
    all_posts = response.json()
    return render_template("blog.html",posts=all_posts)


if __name__ == "__main__":
    app.run(debug=True)

