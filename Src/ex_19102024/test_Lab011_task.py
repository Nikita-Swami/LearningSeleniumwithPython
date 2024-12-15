import time

import allure
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
#from dotenv import load_dotenv
import os


@allure.title("Verify the registration page")
@allure.description(
    "Complete all the required fields , ensure the user is successfully registered, and verify that the 'Your Account "
    "has been Created!' message is displayed")


def test_registration_page_project():
    driver = webdriver.Chrome()
    driver.get("https://awesomeqa.com/ui/index.php?route=account/register")

    #registration details
    first_name = driver.find_element(By.NAME,"firstname")
    first_name.send_keys("Firstname")

    last_name = driver.find_element(By.NAME,"lastname")
    last_name.send_keys("Lastname")

    email = driver.find_element(By.NAME, "email")
    email.send_keys("niks1@gmail.com")

    telephone = driver.find_element(By.NAME,"telephone")
    telephone.send_keys("1234567891")

    password = driver.find_element(By.NAME,"password")
    password.send_keys("Test@1234")

    confirm_password = driver.find_element(By.ID,"input-confirm")
    confirm_password.send_keys("Test@1234")

    checkbox = driver.find_element(By.XPATH,"//input[@type='checkbox'][@value=1]")
    checkbox.click()
    time.sleep(5)

    continue_btn = driver.find_element(By.XPATH, "//input[@value='Continue']")
    continue_btn.submit()
    time.sleep(5)

    current_title = driver.title
    if current_title == "Your Account Has Been Created!":
        verify_text = driver.find_element(By.XPATH, "// h1[text() = 'Your Account Has Been Created!'] / parent::div / "
                                                    "h1")
        assert verify_text.text == current_title
        print("Title:", current_title)
        print("Webpage text:", verify_text)
        time.sleep(5)




