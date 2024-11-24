from allure_pytest.utils import allure_title
from selenium import webdriver
import allure
import pytest


def test_sample():
    driver = webdriver.Chrome()
    driver.get("https://sdet.live")
