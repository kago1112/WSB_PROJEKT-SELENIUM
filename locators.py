from selenium import webdriver
from selenium.webdriver.common.by import By


class LoginLocators:
    login_input = (By.ID, "user-name")
    password_input = (By.ID, "password")
    login_button = (By.ID, "login-button")
    error_message = (By.CLASS_NAME, "error-message-container")
    menu_button = (By.ID, "react-burger-menu-btn")
    logout_button = (By.ID, "logout_sidebar_link")