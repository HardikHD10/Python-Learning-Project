from bs4 import BeautifulSoup
import requests


user = input("Which Year you would like to travel to? Type your date in YYYY-MM-DD format: ")
response = requests.get(url="https://www.billboard.com/charts/hot-100/"+user)
data = response.text

soup = BeautifulSoup(data, "html.parser")
hits = soup.select(selector="li ul li h3")
hits_list = [hit.getText().strip("/n").split("\t",10)[9] for hit in hits]
print(hits_list)