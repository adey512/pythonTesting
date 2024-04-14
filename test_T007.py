import time
import random

import pytest
import requests
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


# Test for Problem User

@pytest.mark.usefixtures("setup")
class TestLoginForProblemUser:
    def test_login_problem_user(self, setup):
        self.driver.get(self.login_page_url)
        self.driver.find_element(By.ID, "user-name").send_keys("problem_user")
        self.driver.find_element(By.ID, "password").send_keys("secret_sauce")
        self.driver.find_element(By.ID, "login-button").click()

        # Check if login is successfully and page is redirected to inventory page
        current_url = self.driver.current_url
        assert current_url == self.inventory_page_url

    def test_problem_user_images(self, setup):
        # Validate if image is broken in inventory Page

        image_list = self.driver.find_elements(By.TAG_NAME, "img")
        iBrokenImageCount = 0
        for img in image_list:
            try:
                response = requests.get(img.get_attribute('src'), stream=True)
                print(response)
                if response.status_code != 200:
                    print(img.get_attribute('outerHTML') + " is broken.")
                    iBrokenImageCount = (iBrokenImageCount + 1)

            except requests.exceptions.MissingSchema:
                print("Encountered MissingSchema Exception")
            except requests.exceptions.InvalidSchema:
                print("Encountered InvalidSchema Exception")
            except:
                print("Encountered Some other Exception")

    def test_problem_user_checkout_information_page(self, setup):

        results = self.driver.find_elements(By.XPATH, "//div[@class='inventory_list']/div")
        product_to_add = results[:2]
        for result in product_to_add:
            result.find_element(By.CLASS_NAME, "btn").click()
        self.driver.find_element(By.ID, "shopping_cart_container").click()
        self.driver.find_element(By.ID, "checkout").click()

        # Enter Your information in checkout
        self.driver.find_element(By.ID, "first-name").send_keys("John")
        self.driver.find_element(By.ID, "last-name").send_keys("Doe")
        self.driver.find_element(By.ID, "postal-code").send_keys("100")
        self.driver.find_element(By.ID, "continue").click()
        message = self.driver.find_element(By.CLASS_NAME, "error-message-container").text
        try:
            response = requests.get(self.checkout_step_two_page_url)
            if response.status_code != 200:
                print("Checkout unsuccessful" + message)
                self.driver.get(self.login_page_url)

        except:
            print("Sorry Problem User Cannot Checkout")
            self.driver.get(self.login_page_url)
