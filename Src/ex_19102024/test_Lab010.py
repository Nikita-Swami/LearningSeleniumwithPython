from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.by import By


def test_verify_button_link_text_project():
    driver = webdriver.Chrome()
    driver.get("https://app.vwo.com/#/login")

    all_buttons = driver.find_element(By.TAG_NAME, "button")
    print(len(all_buttons))
    for i in all_buttons:
        print(i.text)

    

    time.sleep(5)
    driver.quit()