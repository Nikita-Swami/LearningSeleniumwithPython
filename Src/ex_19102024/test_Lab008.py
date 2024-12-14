from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.by import By


def test_negative_vwo_login_project():
    driver = webdriver.Chrome()
    driver.get("https://app.vwo.com/#/login")

    email_web_element = driver.find_element(By.ID,"login-username")
    email_web_element.send_keys("abc@gmail.com")

    #Find the email
    #Find the password

    password_web_element = driver.find_element(By.NAME,"password")
    password_web_element.send_keys("Password@1234")


    #Click on submit

    submit_btn_web_element = driver.find_element(By.ID, "js-login-btn")
    submit_btn_web_element.click()

    time.sleep(3)
    #Verify that message is visible

    error_message_web_element = driver.find_element(By.CLASS_NAME,"notification-box-description")
    print(error_message_web_element.text)
    assert error_message_web_element == "Your email, password, IP address or location did not match"



    time.sleep(10)
    driver.quit()