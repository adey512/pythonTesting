import time

import pytest
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("setup")
class TestLogin:

    def test_verify_login_url(self, setup):
        self.driver.get(self.login_page_url)
        current_url = self.driver.current_url
        assert current_url == self.login_page_url
        time.sleep(3)
# Log in with a valid Username and Password

    def test_standard_user_success_login(self,setup):
        self.driver.find_element(By.ID, "user-name").send_keys("standard_user")
        self.driver.find_element(By.ID, "password").send_keys("secret_sauce")
        self.driver.find_element(By.ID, "login-button").click()
        current_url = self.driver.current_url
        assert current_url == self.inventory_page_url
        time.sleep(3)

