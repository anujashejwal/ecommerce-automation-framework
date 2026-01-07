from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CheckoutPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # Locators
    checkout_button = (By.CSS_SELECTOR, "button[class*='btn-success']")
    country_input = (By.ID, "country")
    country_option = (By.LINK_TEXT, "India")
    checkbox = (By.CSS_SELECTOR, "div[class*='checkbox-primary']")
    submit_button = (By.CSS_SELECTOR, "[type='submit']")
    success_msg = (By.CLASS_NAME, "alert-success")

    def click_checkout(self):
        self.wait.until(
            EC.element_to_be_clickable(self.checkout_button)
        ).click()

    def enter_country(self, country_name):
        country = self.wait.until(
            EC.visibility_of_element_located(self.country_input)
        )
        country.send_keys(country_name)

    def select_country(self):
        self.wait.until(
            EC.element_to_be_clickable(self.country_option)
        ).click()

    def agree_terms(self):
        self.driver.find_element(*self.checkbox).click()

    def click_purchase(self):
        self.driver.find_element(*self.submit_button).click()

    def get_success_message(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.success_msg)
        ).text

    def get_title(self):
        return self.driver.title
