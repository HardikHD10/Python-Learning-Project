import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException,ElementNotInteractableException

s = Service("/Users/hardik/Documents/Development/chromedriver")
driver = webdriver.Chrome(service=s)

url = "https://this-person-does-not-exist.com/en"

driver.get(url)
try:
    b0 = driver.find_element(By.XPATH,"/html/body/div[4]/div/div[2]/span")
    b0.send_keys(Keys.ENTER)
    time.sleep(2)
    b = driver.find_element(By.ID,"reload-button")
    b.click()
    time.sleep(5)
except ElementClickInterceptedException :
    print("You tried well!")
except  ElementNotInteractableException:
    print("You tried well!")
