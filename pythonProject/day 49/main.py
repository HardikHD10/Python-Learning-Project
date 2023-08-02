import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

s = Service("/Users/hardik/Documents/Development/chromedriver")
browser = webdriver.Chrome(service=s)

url = "https://www.linkedin.com/"

browser.get(url)

# login
i1 = browser.find_element(By.XPATH, '//*[@id="session_key"]')
i1.send_keys("hardikinani.professional@gmail.com")
i2 = browser.find_element(By.XPATH,'//*[@id="session_password"]')
i2.send_keys("Hardik@1007")
b = browser.find_element(By.XPATH,'//*[@id="main-content"]/section[1]/div/div/form/button')
b.click()

time.sleep(5)
all_listings = browser.find_elements(By.CSS_SELECTOR,".job-card-container--clickable")

try:
    apply_button = browser.find_element(By.CSS_SELECTOR,".jobs-s-apply button")
    apply_button.click()
    time.sleep(5)

    # If phone field is empty, then fill your phone number.
    phone = browser.find_element(By.CLASS_NAME,"fb-single-line-text__input")
    if phone.text == "":
        phone.send_keys("9829657691")

    submit_button = browser.find_element(By.CSS_SELECTOR,"footer button")

    if submit_button.get_attribute("data-control-name") == "continue_unify":
                close_button = browser.find_element(By.CLASS_NAME,"artdeco-modal__dismiss")
                close_button.click()
                time.sleep(2)
                discard_button = browser.find_elements(By.CLASS_NAME,"artdeco-modal__confirm-dialog-btn")[1]
                discard_button.click()
                print("Complex application, skipped.")

    else:
        submit_button.click()
#Once application completed, close the pop-up window.
        time.sleep(2)
        close_button = browser.find_element(By.CLASS_NAME,"artdeco-modal__dismiss")
        close_button.click()

    #If already applied to job or job is no longer accepting applications, then skip.
except NoSuchElementException:
    print("No application button, skipped.")

time.sleep(5)
browser.quit()