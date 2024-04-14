import time
import random

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


# Test for Locked out User

@pytest.mark.usefixtures("setup")
class TestLoginForLockedUser:

    def test_login_locked_out_user(self, setup):
        self.driver.get(self.login_page_url)
        self.driver.find_element(By.ID, "user-name").send_keys("locked_out_user")
        self.driver.find_element(By.ID, "password").send_keys("secret_sauce")
        self.driver.find_element(By.ID, "login-button").click()
        current_url = self.driver.current_url
        assert current_url == self.login_page_url
        locked_out_user_message = self.driver.find_element(By.CLASS_NAME, "error-message-container").text
        assert "Sorry, this user has been locked out." in locked_out_user_message
