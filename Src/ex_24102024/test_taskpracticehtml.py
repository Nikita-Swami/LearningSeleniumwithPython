import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select


@allure.title("Select radio,checkbox elements")
@allure.description("Verify radio,checkbox elements")
def test_checkbox_radio():
    driver = webdriver.Chrome()
    driver.get("https://awesomeqa.com/practice.html")
    driver.maximize_window()

    #firstname = driver.find_element(By.NAME,"firstname")
    #firstname.send_keys("Nikita")
    #firstname_value = firstname.get_attribute("value")

    #lastname = driver.find_element(By.NAME,"lastname")
    #lastname.send_keys("Swami")
    #lastname_value = lastname.get_attribute("value")

    #gender = driver.find_element(By.XPATH, "//input[@id='sex-1']")
    #gender.click()
    #gender_value = gender.get_attribute("value")
    #print(f"My name is {firstname_value} {lastname_value} and I am ", gender_value)

    #experience = driver.find_element(By.XPATH,"//input[@id='exp-2'")
    #experience.click()
    #experience_value = experience.get_attribute("value")
    #print(f"My name is {firstname_value} {lastname_value} and I have {experience_value} years of experience")

    #profession = driver.find_element(By.XPATH,"//input[@value='Automation Tester']")
    #profession.click()
    #profession_value = profession.get_attribute("value")
    #print(f"My name is {firstname_value} {lastname_value} and I am ", profession_value)

    #time.sleep(5)

    first_name = driver.find_element(By.NAME, "firstname")
    first_name.send_keys("Nikita")
    first_name_value = first_name.get_attribute("value")

    last_name = driver.find_element(By.NAME, "lastname")
    last_name.send_keys("Swami")
    last_name_value = last_name.get_attribute("value")

    gender = driver.find_element(By.XPATH, "//input[@id='sex-1']")
    gender.click()
    gender_value = gender.get_attribute("value")
    print(f"My name is {first_name_value} {last_name_value} and I am a", gender_value)

    experience = driver.find_element(By.XPATH, "//input[@id='exp-2']")
    experience.click()
    experience_value = experience.get_attribute("value")
    print(f"My name is {first_name_value} {last_name_value} and I have a {experience_value} years of experience")

    profession = driver.find_element(By.XPATH, "//input[@value='Automation Tester']")
    profession.click()
    profession_value = profession.get_attribute("value")
    print(f"My name is {first_name_value} {last_name_value} and I am a", profession_value)

    time.sleep(5)