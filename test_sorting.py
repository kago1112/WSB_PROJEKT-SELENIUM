from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
from login_credentials import LoginCreds
from locators import LoginLocators, SortingLocators


def test14_sort_A_to_Z():
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

    product_page_url = "https://www.saucedemo.com/inventory.html"
    assert product_page_url in driver.current_url

    time.sleep(2)

    driver.find_element(*SortingLocators.sort_A_to_Z).click()
    
    items = driver.find_elements(By.CLASS_NAME, "inventory_item_name")
    items_list = []
    for product in items:
        items_list.append(product.text)
    assert items_list == sorted(items_list)

    time.sleep(2)
    driver.quit()



def test15_sort_Z_to_A():
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

    product_page_url = "https://www.saucedemo.com/inventory.html"
    assert product_page_url in driver.current_url

    time.sleep(2)

    driver.find_element(*SortingLocators.sort_Z_to_A).click()
    
    items = driver.find_elements(By.CLASS_NAME, "inventory_item_name")
    items_list = []
    for product in items:
        items_list.append(product.text)
    assert items_list == sorted(items_list, reverse=True)

    time.sleep(2)
    driver.quit()



def test16_sort_low_to_high():
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

    product_page_url = "https://www.saucedemo.com/inventory.html"
    assert product_page_url in driver.current_url

    time.sleep(2)

    driver.find_element(*SortingLocators.sort_low_to_high).click()

    items = driver.find_elements(By.CLASS_NAME, "inventory_item_price")
    items_price_list = []
    for item_price in items:
        price = float(item_price.text.replace("$", ""))
        items_price_list.append(price)
    
    assert items_price_list == sorted(items_price_list)

    time.sleep(2)
    driver.quit()




def test17_sort_high_to_low():
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

    product_page_url = "https://www.saucedemo.com/inventory.html"
    assert product_page_url in driver.current_url

    time.sleep(2)

    driver.find_element(*SortingLocators.sort_high_to_low).click()

    items = driver.find_elements(By.CLASS_NAME, "inventory_item_price")
    items_price_list = []
    for item_price in items:
        price = float(item_price.text.replace("$", ""))
        items_price_list.append(price)
    
    assert items_price_list == sorted(items_price_list, reverse=True)

    time.sleep(2)
    driver.quit()