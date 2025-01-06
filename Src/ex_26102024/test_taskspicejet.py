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

@allure.title("Actions P5")
@allure.description("Verify Click and Hold")
def test_selenium_action_spice_jet_click_and_hold():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--incognito")

    driver = webdriver.Chrome(chrome_options)
    driver.get("https://www.spicejet.com/")

    fromCity = driver.find_element(By.XPATH, "//div[text()='From']")

    time.sleep(3)

    actions = ActionChains(driver)
    (actions.
     move_to_element(fromCity)
     .click().send_keys_to_element(fromCity, "del")
     .perform())

    time.sleep(10)