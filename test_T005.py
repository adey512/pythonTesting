import time
import random

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


@pytest.mark.usefixtures("setup")
class TestLogoutUser:
    # Test to log out standard user
    def test_logout_standard_user(self, setup):
        self.driver.get(self.login_page_url)
        self.driver.find_element(By.ID, "user-name").send_keys("standard_user")
        self.driver.find_element(By.ID, "password").send_keys("secret_sauce")
        self.driver.find_element(By.ID, "login-button").click()
        self.driver.find_element(By.CLASS_NAME, "bm-burger-button").click()
        self.driver.find_elements(By.XPATH, "//div[@class='summary_subtotal_label']")
        self.driver.find_elements(By.CLASS_NAME, "bm-item")[2].click()


