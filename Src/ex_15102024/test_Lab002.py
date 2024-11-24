from selenium import webdriver

def test_open_vwo_login():
    driver = webdriver.Chrome()
    #POST request to create a New Fresh Copy of Chrome
    #Session ID

    driver.get("https://app.vwo.com")
    #code-HTTP request-Handled by selenium manager

    print(driver.title)
    assert driver.title == "Login - VWO"
