import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException


@allure.title("Stale Element")
@allure.description("stale_element exception")
def test_stale_element_exp_demo():
    driver = webdriver.Chrome()
    driver.get("https://google.com")
    try:
        textarea = driver.find_element(By.NAME, "q")
        driver.refresh()
        textarea.send_keys("The Testing Academy")
    except StaleElementReferenceException as see:
        print(see)
        print("Stale element reference")

    time.sleep(5)
