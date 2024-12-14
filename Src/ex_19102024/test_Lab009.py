from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.by import By


def test_verify_link_text_project():
    driver = webdriver.Chrome()
    driver.get("https://app.vwo.com/#/login")

    anchor_tag_element = driver.find_element(By.LINK_TEXT,"Start a free trial")
    anchor_tag_element.click()

    assert driver.current_url == "https://vwo.com/free-trial/?utm_medium=website&utm_source=login-page&utm_campaign=mof_eg_loginpage"

    time.sleep(5)
    driver.quit()