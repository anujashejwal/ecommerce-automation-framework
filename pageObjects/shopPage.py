from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ShopPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # Shop page locators
    product_cards = (By.CSS_SELECTOR, "div.card.h-100")
    product_name = (By.CSS_SELECTOR, "h4.card-title a")
    add_to_cart_button = (By.XPATH, "div/button")
    # Navbar / cart navigation
    cart_link = (By.CSS_SELECTOR, "a.nav-link.btn.btn-primary")
    # Cart page checkout button
    checkout_button = (By.XPATH, "//button[normalize-space()='Checkout']")

    def add_product_to_cart(self, expected_product_name):
        self.wait.until(
            EC.visibility_of_element_located(self.product_cards)
        )

        products = self.driver.find_elements(*self.product_cards)

        for product in products:
            name = product.find_element(*self.product_name).text.strip()
            if name == expected_product_name:
                product.find_element(*self.add_to_cart_button).click()
                return

        raise Exception(f"Product '{expected_product_name}' not found")

    def go_to_cart(self):
        self.wait.until(
            EC.element_to_be_clickable(self.cart_link)
        ).click()

    def click_checkout(self):
        self.wait.until(
            EC.element_to_be_clickable(self.checkout_button)
        ).click()
