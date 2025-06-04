from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
from login_credentials import LoginCreds
from locators import LoginLocators, InventoryLocators




def test11_adding_item_to_cart():
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

    driver.find_element(*InventoryLocators.add_to_cart_backpack).click()
    driver.find_element(*InventoryLocators.go_to_cart_button).click()
    
    time.sleep(2)
    
    cart_url = "https://www.saucedemo.com/cart.html"
    assert cart_url in driver.current_url

    assert driver.find_element(*InventoryLocators.backpack_item).is_displayed()
    assert driver.find_element(*InventoryLocators.checkout_button).is_displayed()

    driver.quit()




def test12_removing_item_from_cart_cart_page():
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

    driver.find_element(*InventoryLocators.add_to_cart_backpack).click()
    driver.find_element(*InventoryLocators.go_to_cart_button).click()
    
    time.sleep(2)
    
    cart_url = "https://www.saucedemo.com/cart.html"
    assert cart_url in driver.current_url

    assert driver.find_element(*InventoryLocators.backpack_item).is_displayed()
    assert driver.find_element(*InventoryLocators.checkout_button).is_displayed()
    assert driver.find_element(*InventoryLocators.continue_shopping_button).is_displayed()

    assert driver.find_element(*InventoryLocators.remove_backpack_button).is_displayed()
    driver.find_element(*InventoryLocators.remove_backpack_button).click()

    time.sleep(2)

    assert cart_url in driver.current_url
    assert not driver.find_elements(*InventoryLocators.backpack_item)

    driver.quit()



def test13_removing_item_from_cart_inventory_page():
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

    driver.find_element(*InventoryLocators.add_to_cart_backpack).click()
    driver.find_element(*InventoryLocators.go_to_cart_button).click()
    
    time.sleep(2)
    
    cart_url = "https://www.saucedemo.com/cart.html"
    assert cart_url in driver.current_url

    assert driver.find_element(*InventoryLocators.backpack_item).is_displayed()
    assert driver.find_element(*InventoryLocators.checkout_button).is_displayed()
    assert driver.find_element(*InventoryLocators.continue_shopping_button).is_displayed()

    driver.find_element(*InventoryLocators.continue_shopping_button).click()

    time.sleep(2)
    assert product_page_url in driver.current_url

    assert driver.find_element(*InventoryLocators.remove_backpack_button).is_displayed()
    driver.find_element(*InventoryLocators.remove_backpack_button).click()

    driver.find_element(*InventoryLocators.go_to_cart_button).click()

    time.sleep(2)

    assert cart_url in driver.current_url
    assert not driver.find_elements(*InventoryLocators.backpack_item)

    driver.quit()