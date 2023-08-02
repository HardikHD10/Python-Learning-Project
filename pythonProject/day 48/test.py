from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

s=Service("/Users/hardik/Documents/Development/chromedriver")
browser = webdriver.Chrome(service=s)

url = "http://secure-retreat-92358.herokuapp.com/"
browser.get(url)
i1= browser.find_element(By.XPATH,'/html/body/form/input[1]')
i1.send_keys("Hardik")
i2 = browser.find_element(By.XPATH,'/html/body/form/input[2]')
i2.send_keys("Inani")
i3= browser.find_element(By.XPATH,'/html/body/form/input[3]')
i3.send_keys("hardikinani1007@gmail.com")
b = browser.find_element(By.XPATH,'/html/body/form/button')
b.click()