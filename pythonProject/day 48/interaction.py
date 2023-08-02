from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

s = Service("/Users/hardik/Documents/Development/chromedriver")
browser = webdriver.Chrome(service=s)

url = "https://en.wikipedia.org/wiki/Main_Page"

browser.get(url)
total_articles = browser.find_element(By.XPATH,'//*[@id="articlecount"]/a[1]')
print(total_articles.text)

search =browser.find_element(By.NAME,"search")
search.send_keys("India")
search.send_keys(Keys.ENTER)
# browser.close()
