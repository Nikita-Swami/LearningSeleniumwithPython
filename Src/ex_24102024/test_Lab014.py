import time

import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
#from dotenv import load_dotenv
import os

from selenium.webdriver.ie.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@allure.title("Alerts")
@allure.description("Verify Alerts")

def test_alerts_prompt():
    driver = webdriver.Chrome()
    driver.get("https://the-internet.heroapp.com/javascript_alerts")
    driver.maximize_window()

    element_prompt = driver.find_element(By.XPATH,"//button[@onclick='jsAlert()']")

    element_prompt.click()


    WebDriverWait(driver=driver,timeout=5).until(EC.alert_is_present())

    alert = driver.switch_to.alert
    alert.accept()
    alert.dismiss()

    result_text = driver.find_element(By.ID, "result").text

    assert result_text == "You sucessfully clicked as alert"


    time.sleep(5)

def test_alerts_confirm():
    driver = webdriver.Chrome()
    driver.get("https://the-internet.heroapp.com/javascript_alerts")
    driver.maximize_window()


    element_confirm = driver.find_element(By.XPATH, "//button[@onclick='jsConfirm()']")

    element_confirm.click()

    WebDriverWait(driver=driver,timeout=5).until(EC.alert_is_present())

    alert = driver.switch_to.alert
    alert.accept()
    alert.dismiss()

    result_text = driver.find_element(By.ID, "result").text


    assert result_text == "You clicked : Cancel"

    time.sleep(5)