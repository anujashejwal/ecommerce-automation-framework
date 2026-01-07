import json
import pytest
from pageObjects.loginPage import LoginPage
from pageObjects.shopPage import ShopPage
from pageObjects.checkoutPage import CheckoutPage
from utilities.baseClass import BaseClass


def get_test_data():
    with open("testData/checkoutData.json") as f:
        data = json.load(f)
        return data["users"]


class TestE2ECheckout(BaseClass):

    @pytest.mark.regression
    @pytest.mark.parametrize("user", get_test_data())
    def test_end_to_end_purchase(self, user):
        self.driver.get("https://rahulshettyacademy.com/loginpagePractise/")

        login_page = LoginPage(self.driver)
        login_page.enter_username(user["username"])
        login_page.enter_password(user["password"])
        login_page.click_sign_in()

        shop_page = ShopPage(self.driver)
        shop_page.add_product_to_cart(user["product"])
        shop_page.go_to_cart()
        shop_page.click_checkout()

        checkout_page = CheckoutPage(self.driver)
        checkout_page.enter_country("Ind")
        checkout_page.select_country()
        checkout_page.agree_terms()
        checkout_page.click_purchase()

        success_text = checkout_page.get_success_message()
        assert "Success" in success_text
