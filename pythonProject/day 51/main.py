import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

s = Service("/Users/hardik/Documents/Development/chromedriver")
driver = webdriver.Chrome(service=s)

url = "https://speedtest.net"
driver.get(url)
b = driver.find_element(By.XPATH,'//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a')
b.click()

time.sleep(45)
data1 = driver.find_element(By.XPATH,'//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span')
download_speed = data1.text

data2 = driver.find_element(By.XPATH,'//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span')
upload_speed = data2.text

url_2 = "https://twitter.com/login"
username = "+919829657691"
pass_word =  "Hardik@1007"

driver.get(url_2)
time.sleep(10)
email = driver.find_element(By.NAME,'text')
email.send_keys(username)
email.send_keys(Keys.ENTER)
time.sleep(5)
password = driver.find_element(By.NAME,'password')
password.send_keys(pass_word)
password.send_keys(Keys.ENTER)
time.sleep(2)
tweet_box = driver.find_element(By.XPATH,'//*[@id="react-root"]/div/div/div[2]/header/div/div/div/div[1]/div[3]/a')
tweet_box.send_keys(Keys.ENTER)
time.sleep(2)
tweet_chat =driver.find_element(By.CLASS_NAME, 'public-DraftStyleDefault-block')
tweet_chat.send_keys(f"@reliancejio speed update at Bhilwara : download Speed = {download_speed} MBPS, upload speed = {upload_speed}MBPS.\nThis is a Bot Generated Tweet.")
time.sleep(2)

action = ActionChains(driver)
action.key_down(Keys.COMMAND).send_keys(Keys.ENTER).key_up(Keys.COMMAND).perform()
driver.quit()
