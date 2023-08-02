from bs4 import BeautifulSoup
import requests

response = requests.get(url="https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
data = response.text

soup = BeautifulSoup(data, "html.parser")
all_movies = soup.find_all(name="h3", class_="title")
movie_title=[movie.getText() for movie in all_movies]
movies = movie_title[::-1]
print(movies)

with open("file.txt","w") as file:
    for movie in movies:
        file.write(f"{movie}\n")