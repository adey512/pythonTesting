import time

import pytest
from selenium.webdriver.common.by import By


@pytest.mark.usefixtures("setup")
class TestLoginNegative:
    def test_standard_user_incorrect_password(self, setup):
        self.driver.get(self.login_page_url)
        self.driver.find_element(By.ID, "user-name").send_keys("standard_user")
        self.driver.find_element(By.ID, "password").send_keys("WRONG")
        self.driver.find_element(By.ID, "login-button").click()
        current_url = self.driver.current_url
        assert current_url == self.login_page_url
        incorrect_password_message = self.driver.find_element(By.CLASS_NAME, "error-message-container").text
        assert "Username and password do not match any user in this service" in incorrect_password_message

    def test_standard_user_incorrect_username(self, setup):
        self.driver.get(self.login_page_url)
        self.driver.find_element(By.ID, "user-name").send_keys("WRONG")
        self.driver.find_element(By.ID, "password").send_keys("secret_sauce")
        self.driver.find_element(By.ID, "login-button").click()
        current_url = self.driver.current_url
        assert current_url == self.login_page_url
        incorrect_username_message = self.driver.find_element(By.CLASS_NAME, "error-message-container").text
        assert "Username and password do not match any user in this service" in incorrect_username_message

    def test_standard_user_case_insensitive_password(self, setup):
        self.driver.get(self.login_page_url)
        self.driver.find_element(By.ID, "user-name").send_keys("standard_user")
        self.driver.find_element(By.ID, "password").send_keys("secreT_Sauce")
        self.driver.find_element(By.ID, "login-button").click()
        current_url = self.driver.current_url
        assert current_url == self.login_page_url
        incorrect_password_message = self.driver.find_element(By.CLASS_NAME, "error-message-container").text
        assert "Username and password do not match any user in this service" in incorrect_password_message

    def test_standard_user_empty_username(self, setup):
        self.driver.get(self.login_page_url)
        self.driver.find_element(By.ID, "user-name").send_keys("")
        self.driver.find_element(By.ID, "password").send_keys("secret_sauce")
        self.driver.find_element(By.ID, "login-button").click()
        current_url = self.driver.current_url
        assert current_url == self.login_page_url
        empty_username_message = self.driver.find_element(By.CLASS_NAME, "error-message-container").text
        assert "Username is required" in empty_username_message

    def test_standard_user_empty_password(self, setup):
        self.driver.get(self.login_page_url)
        self.driver.find_element(By.ID, "user-name").send_keys("standard_user")
        self.driver.find_element(By.ID, "password").send_keys("")
        self.driver.find_element(By.ID, "login-button").click()
        current_url = self.driver.current_url
        assert current_url == self.login_page_url
        empty_password_message = self.driver.find_element(By.CLASS_NAME, "error-message-container").text
        assert "Password is required" in empty_password_message
