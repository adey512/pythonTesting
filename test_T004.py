import time
import random

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


@pytest.mark.usefixtures("setup")
class TestAddToCard:
    # Test to add and remove products to cart
    def test_standard_user_add_to_cart(self, setup):
        self.driver.get(self.login_page_url)
        self.driver.find_element(By.ID, "user-name").send_keys("standard_user")
        self.driver.find_element(By.ID, "password").send_keys("secret_sauce")
        self.driver.find_element(By.ID, "login-button").click()
        results = self.driver.find_elements(By.XPATH, "//div[@class='inventory_list']/div")

        # Randomize and Add 3 products to cart
        random.shuffle(results)
        # random module to pick any 4 products from inventory list
        product_to_add = results[:4]
        for result in product_to_add:
            result.find_element(By.CLASS_NAME, "btn").click()

    # Add to Cart Page validate url
    def test_standard_user_add_to_cart_validate_url(self, setup):
        self.driver.find_element(By.ID, "shopping_cart_container").click()
        current_url = self.driver.current_url
        assert current_url == self.cart_page_url
        # Count number of items in the cart
        cart_items = self.driver.find_elements(By.XPATH, "//div[@class='cart_list']/div[@class='cart_item']")
        count_cart = len(cart_items)
        assert count_cart == 4

    def test_standard_user_add_to_cart_remove_item(self, setup):
        # Remove top item from the cart
        self.driver.find_elements(By.CLASS_NAME, "cart_button")[0].click()

        # Check if count of items in cart is 3
        cart_items = self.driver.find_elements(By.XPATH, "//div[@class='cart_list']/div[@class='cart_item']")
        count_cart = len(cart_items)
        assert count_cart == 3

    def test_standard_user_validate_continue_shopping(self, setup):
        # Continue Shopping and validations
        self.driver.find_element(By.ID, "continue-shopping").click()

        # Check if back to inventory url page
        current_url = self.driver.current_url
        assert current_url == self.inventory_page_url

    def test_standard_user_add_to_cart_validate_number_of_cart_items(self, setup):
        # Back to add to cart Page and recheck if 3 items are added to cart
        self.driver.find_element(By.ID, "shopping_cart_container").click()
        cart_items = self.driver.find_elements(By.XPATH, "//div[@class='cart_list']/div[@class='cart_item']")
        count_cart = len(cart_items)
        assert count_cart == 3

    # Test to check out items from the cart
    def test_standard_user_cart_checkout(self, setup):
        self.driver.find_element(By.ID, "checkout").click()

        # Validate if redirected to checkout-step 1 page

        current_url = self.driver.current_url
        assert current_url == self.checkout_step_one_page_url

    def test_standard_user_checkout_form_validate_cancel(self, setup):
        # Cancel from Checkout step one page. Validate if redirected to add to cart page
        self.driver.find_element(By.ID, "cancel").click()
        current_url = self.driver.current_url
        assert current_url == self.cart_page_url

    def test_standard_user_checkout_cancel_verify_cart_count(self, setup):
        self.driver.find_element(By.ID, "shopping_cart_container").click()
        cart_items = self.driver.find_elements(By.XPATH, "//div[@class='cart_list']/div[@class='cart_item']")
        count_cart = len(cart_items)
        assert count_cart == 3
        # Click continue and back to check out page
        self.driver.find_element(By.ID, "checkout").click()
        current_url = self.driver.current_url
        assert current_url == self.checkout_step_one_page_url

    def test_standard_user_checkout_form_validation_correct_fields(self, setup):
        # Add info
        self.driver.find_element(By.ID, "first-name").send_keys("Jane")
        self.driver.find_element(By.ID, "last-name").send_keys("Doe")
        self.driver.find_element(By.ID, "postal-code").send_keys("95136")
        self.driver.find_element(By.ID, "continue").click()

    def test_standard_user_checkout_overview_validate_url(self, setup):
        # Check if redirected to check out step-two-page
        current_url = self.driver.current_url
        assert current_url == self.checkout_step_two_page_url

    def test_standard_user_checkout_overview_validate_total_cart_items(self, setup):

        cart_items = self.driver.find_elements(By.XPATH, "//div[@class='cart_list']/div[@class='cart_item']")
        count_cart = len(cart_items)
        assert count_cart == 3

    def test_standard_user_checkout_validate_price_sum(self, setup):

        # Take prices of items from the cart and sum them
        prices = self.driver.find_elements(By.CLASS_NAME, "inventory_item_price")
        sum_prices = 0.00
        for price in prices:
            str_price = price.text
            string_price = str_price.replace("$", "")
            float_price = float(string_price)
            sum_prices = sum_prices + float_price

        # Check Item sun-total price (before tac)
        float_subtotal = 0.00
        subtotal_str = self.driver.find_elements(By.XPATH, "//div[@class='summary_subtotal_label']")
        for subtotal in subtotal_str:
            subtotal_price = subtotal.text
            subtotal_price1 = subtotal_price.replace("Item total: $", "")
            float_subtotal = float(subtotal_price1)

        # Validate if summation of prices from cart inventory is equal to the sun total price displayed
        assert sum_prices == float_subtotal

    def test_standard_user_checkout_overview_cancel(self, setup):
        # Cancel from Checkout step two page. Validate if redirected to add to inventory page
        self.driver.find_element(By.ID, "cancel").click()
        current_url = self.driver.current_url
        assert current_url == self.inventory_page_url

        # Return back to check out pages
        self.driver.find_element(By.ID, "shopping_cart_container").click()
        self.driver.find_element(By.ID, "checkout").click()
        time.sleep(3)

    def test_standard_user_checkout_form_validation_empty_fname(self, setup):
        # Add empty first_name
        self.driver.find_element(By.ID, "first-name").send_keys("")
        self.driver.find_element(By.ID, "last-name").send_keys("Doe")
        self.driver.find_element(By.ID, "postal-code").send_keys("95136")
        self.driver.find_element(By.ID, "continue").click()

        current_url = self.driver.current_url
        assert current_url == self.checkout_step_one_page_url
        empty_fname_message = self.driver.find_element(By.CLASS_NAME, "error-message-container").text
        assert "First Name is required" in empty_fname_message

    def test_standard_user_checkout_form_validation_empty_lname(self, setup):
        # Add empty first_name
        self.driver.find_element(By.ID, "cancel").click()
        self.driver.find_element(By.ID, "checkout").click()
        self.driver.find_element(By.ID, "first-name").send_keys("John")
        self.driver.find_element(By.ID, "last-name").send_keys("")
        self.driver.find_element(By.ID, "postal-code").send_keys("95136")
        self.driver.find_element(By.ID, "continue").click()

        current_url = self.driver.current_url
        assert current_url == self.checkout_step_one_page_url
        empty_lname_message = self.driver.find_element(By.CLASS_NAME, "error-message-container").text
        assert "Last Name is required" in empty_lname_message

    def test_standard_user_checkout_form_validation_empty_zip(self, setup):
        # Add empty first_name
        self.driver.find_element(By.ID, "cancel").click()
        self.driver.find_element(By.ID, "checkout").click()
        self.driver.find_element(By.ID, "first-name").send_keys("John")
        self.driver.find_element(By.ID, "last-name").send_keys("Doe")
        self.driver.find_element(By.ID, "postal-code").send_keys("")
        self.driver.find_element(By.ID, "continue").click()

        current_url = self.driver.current_url
        assert current_url == self.checkout_step_one_page_url
        empty_zip_message = self.driver.find_element(By.CLASS_NAME, "error-message-container").text
        assert "Postal Code is required" in empty_zip_message

        # Go to continue with correct credentials

        self.driver.find_element(By.ID, "first-name").send_keys("Jane")
        self.driver.find_element(By.ID, "last-name").send_keys("Doe")
        self.driver.find_element(By.ID, "postal-code").send_keys("95136")
        self.driver.find_element(By.ID, "continue").click()

    def test_standard_user_checkout_overview_finish(self, setup):
        # Finish from Checkout step two page. Validate if redirected to check out complete page
        self.driver.find_element(By.ID, "finish").click()
        current_url = self.driver.current_url
        assert current_url == self.checkout_complete_page_url

    def test_standard_user_checkout_complete_return_home(self, setup):
        self.driver.find_element(By.ID, "back-to-products").click()
        # Check if back to inventory page

        current_url = self.driver.current_url
        assert current_url == self.inventory_page_url

