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



class TestSelenium:

   def __init__(self):
       self.driver = None

   def open_browser(self):
       self.chrome_options = webdriver.ChromeOptions()
       self.chrome_options.add_argument("--incognito--")
       self.driver = webdriver.Chrome(self.chrome_options)
       self.driver.get("https://selectorshub.com/xpath-practice-page/")
       self.driver.maximize_window()


   def test_selenium_js(self):
      title = self.driver.execute_script("return document.title")
      current_url = self.driver.execute_script("return document.URL")
      print(title)
      print(current_url)

   def close_browser(self):
      time.sleep(10)
      self.driver.quit()


test = TestSelenium()
test.open_browser()
test.test_selenium_js()
test.close_browser()
