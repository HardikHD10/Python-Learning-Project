from bs4 import BeautifulSoup
import requests
# # import lxml
#
# with open("website.html", mode="r") as file:
#     content = file.read()
#
# # print(content)
#
# soup = BeautifulSoup(content,"html.parser")
# # print(soup.title.string)
# # print(soup.prettify())
# # print(soup.p)
#
# all_anchor_tags = soup.find_all(name="a")
#
# for tag in all_anchor_tags :
#     print(tag.getText())
#     print(tag.get("href"))
#
# heading = soup.find(name="h3",class_="heading")
# print(heading.getText())
#
# comany_url = soup.select_one(selector="p em a")
# print(comany_url)
#
# name = soup.select_one(selector="#name")
# print(name)
#
# headings = soup.select(".heading")
# print(headings)

# response = requests.get(url="https://news.ycombinator.com/news")
# yc_webpage = response.text

# soup =BeautifulSoup(yc_webpage, "html.parser")
# heading = soup.find(name="td",class_="subtext")
# print(heading.getText())