import pytest
from pageObjects.loginPage import LoginPage
from utilities.baseClass import BaseClass


class TestLogin(BaseClass):

    def test_login_failure(self):
        login_page = LoginPage(self.driver)

        self.driver.get("https://rahulshettyacademy.com/loginpagePractise/")

        login_page.enter_username("wronguser")
        login_page.enter_password("wrongpassword")
        login_page.click_sign_in()

        error_text = login_page.get_error_message()
        assert "Incorrect" in error_text
