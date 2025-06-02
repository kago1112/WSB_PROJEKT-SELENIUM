from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
import time
from login_credentials import LoginCreds
from locators import LoginLocators, InventoryLocators, CartLocators




def test10_adding_item_to_cart():
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





    # Add item to cart
    add_to_cart = 
    cart_url = "https://www.saucedemo.com/cart.html"
    driver.get(cart_url)
    time.sleep(2)
    # Verify item is in the cart
    cart_items = driver.find_elements(By.CSS_SELECTOR, ".cart_item")
    assert len(cart_items) > 0, "Cart is empty, item was not added successfully."
    print("Item successfully added to the cart.")
    time.sleep(2)
    driver.quit()