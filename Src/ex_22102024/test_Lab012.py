import time

import allure
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
#from dotenv import load_dotenv
import os


@allure.title("Find all buttons by TagName")
@allure.description("Verify that FREE trial button is clicked, Navigate to next page")

def test_5():
    driver = webdriver.Chrome
    driver.get("https://awesomeqa.com/ui/index.php?route=account/register")

