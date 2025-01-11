import allure
import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.actions.mouse_button import MouseButton

@allure.title("JS")
@allure.description("JS Executor")
def test_selenium_js():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--incognito--")

    driver = webdriver.Chrome(chrome_options)
    driver.get("https://selectorshub.com/xpath-practice-page/")
    driver.maximize_window()

    title = driver.execute_script("return document.title")
    current_url = driver.execute_script("return document.URL")

    print(title)
    print(current_url)

    time.sleep(10)
    driver.quit()