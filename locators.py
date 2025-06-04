from selenium.webdriver.common.by import By


class LoginLocators:
    login_input = (By.ID, "user-name")
    password_input = (By.ID, "password")
    login_button = (By.ID, "login-button")
    error_message = (By.CLASS_NAME, "error-message-container")
    menu_button = (By.ID, "react-burger-menu-btn")
    logout_button = (By.ID, "logout_sidebar_link")


class InventoryLocators:
    backpack_item = (By.ID, "item_4_title_link")
    add_to_cart_backpack = (By.ID, "add-to-cart-sauce-labs-backpack")
    go_to_cart_button = (By.ID, "shopping_cart_container")
    checkout_button = (By.ID, "checkout")
    continue_shopping_button = (By.ID, "continue-shopping")
    remove_backpack_button =  (By.ID, "remove-sauce-labs-backpack")


class SortingLocators:
    sort_A_to_Z = (By.XPATH, "//option[@value='az']")
    sort_Z_to_A = (By.XPATH, "//option[@value='za']")
    sort_low_to_high = (By.XPATH, "//option[@value='lohi']")
    sort_high_to_low = (By.XPATH, "//option[@value='hilo']")