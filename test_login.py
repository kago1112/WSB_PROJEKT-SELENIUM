from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
import time
from login_credentials import LoginCreds
from locators import LoginLocators



def test01_valid_username_valid_password():
    chrome_options = Options()
    chrome_options.add_argument("--incognito")
    driver = webdriver.Chrome(options=chrome_options)
    url = "https://www.saucedemo.com/"

    driver.get(url)
    driver.maximize_window()

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(LoginLocators.login_input)
    )

    username = driver.find_element(*LoginLocators.login_input)
    username.send_keys(LoginCreds.valid_username)
    password = driver.find_element(*LoginLocators.password_input)
    password.send_keys(LoginCreds.valid_password)
    
    driver.find_element(*LoginLocators.login_button).click()

    logged_in_url = "https://www.saucedemo.com/inventory.html"
    assert logged_in_url in driver.current_url

    time.sleep(2)
    driver.quit()



def test02_invalid_username_valid_password():
    chrome_options = Options()
    chrome_options.add_argument("--incognito")
    driver = webdriver.Chrome(options=chrome_options)
    url = "https://www.saucedemo.com/"

    driver.get(url)
    driver.maximize_window()

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(LoginLocators.login_input)
    )

    username = driver.find_element(*LoginLocators.login_input)
    username.send_keys(LoginCreds.invalid_username)
    password = driver.find_element(*LoginLocators.password_input)
    password.send_keys(LoginCreds.valid_password)
    
    driver.find_element(*LoginLocators.login_button).click()

    driver.find_element(*LoginLocators.error_message)
    assert driver.find_element(*LoginLocators.error_message).text, "Epic sadface: Username and password do not match any user in this service"

    time.sleep(2)
    driver.quit()



def test03_valid_username_invalid_password():
    chrome_options = Options()
    chrome_options.add_argument("--incognito")
    driver = webdriver.Chrome(options=chrome_options)
    url = "https://www.saucedemo.com/"

    driver.get(url)
    driver.maximize_window()

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(LoginLocators.login_input)
    )

    username = driver.find_element(*LoginLocators.login_input)
    username.send_keys(LoginCreds.valid_username)
    password = driver.find_element(*LoginLocators.password_input)
    password.send_keys(LoginCreds.invalid_password)
    
    driver.find_element(*LoginLocators.login_button).click()

    driver.find_element(*LoginLocators.error_message)
    assert driver.find_element(*LoginLocators.error_message).text, "Epic sadface: Username and password do not match any user in this service"

    time.sleep(2)
    driver.quit()



def test04_invalid_username_invalid_password():
    chrome_options = Options()
    chrome_options.add_argument("--incognito")
    driver = webdriver.Chrome(options=chrome_options)
    url = "https://www.saucedemo.com/"

    driver.get(url)
    driver.maximize_window()

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(LoginLocators.login_input)
    )

    username = driver.find_element(*LoginLocators.login_input)
    username.send_keys(LoginCreds.invalid_username)
    password = driver.find_element(*LoginLocators.password_input)
    password.send_keys(LoginCreds.invalid_password)
    
    driver.find_element(*LoginLocators.login_button).click()

    driver.find_element(*LoginLocators.error_message)
    assert driver.find_element(*LoginLocators.error_message).text, "Epic sadface: Username and password do not match any user in this service"

    time.sleep(2)
    driver.quit()




def test05_empty_username_valid_password():
    chrome_options = Options()
    chrome_options.add_argument("--incognito")
    driver = webdriver.Chrome(options=chrome_options)
    url = "https://www.saucedemo.com/"

    driver.get(url)
    driver.maximize_window()

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(LoginLocators.password_input)
    )
    
    password = driver.find_element(*LoginLocators.password_input)
    password.send_keys(LoginCreds.valid_password)
    
    driver.find_element(*LoginLocators.login_button).click()

    driver.find_element(*LoginLocators.error_message)
    assert driver.find_element(*LoginLocators.error_message).text, "Epic sadface: Username is required"

    time.sleep(2)
    driver.quit()




def test06_empty_username_invalid_password():
    chrome_options = Options()
    chrome_options.add_argument("--incognito")
    driver = webdriver.Chrome(options=chrome_options)
    url = "https://www.saucedemo.com/"

    driver.get(url)
    driver.maximize_window()

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(LoginLocators.password_input)
    )
    
    password = driver.find_element(*LoginLocators.password_input)
    password.send_keys(LoginCreds.invalid_password)
    
    driver.find_element(*LoginLocators.login_button).click()

    driver.find_element(*LoginLocators.error_message)
    assert driver.find_element(*LoginLocators.error_message).text, "Epic sadface: Username is required"

    time.sleep(2)
    driver.quit()



def test07_valid_username_empty_password():
    chrome_options = Options()
    chrome_options.add_argument("--incognito")
    driver = webdriver.Chrome(options=chrome_options)
    url = "https://www.saucedemo.com/"

    driver.get(url)
    driver.maximize_window()

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(LoginLocators.login_input)
    )

    username = driver.find_element(*LoginLocators.login_input)
    username.send_keys(LoginCreds.valid_username)
    
    driver.find_element(*LoginLocators.login_button).click()

    driver.find_element(*LoginLocators.error_message)
    assert driver.find_element(*LoginLocators.error_message).text, "Epic sadface: Password is required"

    time.sleep(2)
    driver.quit()



def test08_invalid_username_empty_password():
    chrome_options = Options()
    chrome_options.add_argument("--incognito")
    driver = webdriver.Chrome(options=chrome_options)
    url = "https://www.saucedemo.com/"

    driver.get(url)
    driver.maximize_window()

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(LoginLocators.login_input)
    )

    username = driver.find_element(*LoginLocators.login_input)
    username.send_keys(LoginCreds.invalid_username)
    
    driver.find_element(*LoginLocators.login_button).click()

    driver.find_element(*LoginLocators.error_message)
    assert driver.find_element(*LoginLocators.error_message).text, "Epic sadface: Password is required"

    time.sleep(2)
    driver.quit()



def test09_empty_username_empty_password():
    chrome_options = Options()
    chrome_options.add_argument("--incognito")
    driver = webdriver.Chrome(options=chrome_options)
    url = "https://www.saucedemo.com/"

    driver.get(url)
    driver.maximize_window()

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(LoginLocators.login_button)
    )

    driver.find_element(*LoginLocators.login_button).click()

    driver.find_element(*LoginLocators.error_message)
    assert driver.find_element(*LoginLocators.error_message).text, "Epic sadface: Username is required"

    time.sleep(2)
    driver.quit()