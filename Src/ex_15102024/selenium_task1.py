from selenium import webdriver
import allure

@allure.title("verify the demo cura app")
def test_open_cura():
    driver = webdriver.Chrome()

    driver.get("https://katalon-demo-cura.herokuapp.com/")

    print(driver.title)

    assert driver.title == "CURA Healthcare Service"
    ##