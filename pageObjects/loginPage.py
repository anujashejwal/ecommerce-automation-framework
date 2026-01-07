from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    # Locators
    username_input = (By.ID, "username")
    password_input = (By.ID, "password")
    sign_in_button = (By.ID, "signInBtn")
    error_message = (By.CSS_SELECTOR, ".alert-danger")

    # Actions
    def enter_username(self, username):
        self.driver.find_element(*self.username_input).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(*self.password_input).send_keys(password)

    def click_sign_in(self):
        self.driver.find_element(*self.sign_in_button).click()

    def get_error_message(self):
        wait = WebDriverWait(self.driver, 10)
        error = wait.until(
            EC.visibility_of_element_located(self.error_message)
        )
        return error.text
