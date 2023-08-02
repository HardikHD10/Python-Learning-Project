# https://selenium-python.readthedocs.io/
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s=Service("/Users/hardik/Documents/Development/chromedriver")
browser = webdriver.Chrome(service=s)

browser.get("https://www.amazon.in/Morphy-Richards-Europa-Espresso-Cappuccino/dp/B008P7IF02/ref=sr_1_1_sspa?crid=H8PGD4GR5EHF&keywords=coffee+machine&qid=1656848256&sprefix=%2Caps%2C203&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEyNVhTQUQ5TTZLWk04JmVuY3J5cHRlZElkPUEwMzc0ODk0MTdZNVhBNFMxTkVZTyZlbmNyeXB0ZWRBZElkPUEwNTg1MTA1UzFXTTJCNFpaNTVFJndpZGdldE5hbWU9c3BfYXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ==")
price = browser.find_element(By.CLASS_NAME, "a-price-whole")
print(price.text)


# driver.close()
browser.quit()