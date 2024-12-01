from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.by import By

def test_chrome_current_url_verification():
    driver = webdriver.Chrome()
    driver.get("https://katalon-demo-cura.herokuapp.com/")

    #Find the element anchor tag
    #Find the element by strategy or locator

    #<a   - open tag
    # id="btn-make-appointment"
    # href="./profile.php#login"
    # class="btn btn-dark btn-lg">
    # Make Appointment
    # </a>  - close tag

    make_appointment_element = driver.find_element(By.ID, "btn-make-appointment")

    #We need to find the unique attribute which can find the web element
    #Click on it

    make_appointment_element.click()

    #Verify that URL changes


    assert driver.current_url == "https://katalon-demo-cura.herokuapp.com/profile.php#login"

    time.sleep(10)
    driver.quit()


