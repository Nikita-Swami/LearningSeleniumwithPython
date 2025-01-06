import allure
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
#from selenium.webdriver.common.keys import ActionChains.ActionBuilder
from selenium.webdriver.common.actions.mouse_button import MouseButton

@allure.title("Actions P4")
@allure.description("Verify Drag and Drop")
def test_selenium_action_drag_and_drop():
    driver = webdriver.Chrome()
    driver.get("https://awesomeqa.com/selenium/mouse_interaction.html")

    drag = driver.find_element(By.ID,"draggable")
    drop = driver.find_element(By.ID,"droppable")

    time.sleep(5)

    actions = ActionChains(driver)
    ActionChains(driver).drag_and_drop(drag, drop).perform()

    time.sleep(10)
