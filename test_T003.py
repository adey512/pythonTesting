import time

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


@pytest.mark.usefixtures("setup")
class TestProductInventory:

    # Test to check product inventory is not empty
    def test_standard_user_product_inventory(self, setup):
        self.driver.get(self.login_page_url)
        self.driver.find_element(By.ID, "user-name").send_keys("standard_user")
        self.driver.find_element(By.ID, "password").send_keys("secret_sauce")
        self.driver.find_element(By.ID, "login-button").click()
        results = self.driver.find_elements(By.XPATH, "//div[@class='inventory_list']/div")
        count = len(results)

        assert count > 0

    # Tests to sort inventory list

    # Check if products are sorted according to price low to high
    def test_standard_user_sort_product_price(self, setup):

        # Get before sort inventory price (without sort )

        beforeSortedElement = []

        inventory_prices = self.driver.find_elements(By.CLASS_NAME, "inventory_item_price")

        for element in inventory_prices:
            ele_price = element.text
            string_ele = ele_price.replace("$", "")
            float_ele = float(string_ele)
            beforeSortedElement.append(float_ele)

        # Sort using code and store price in lo to hi beforeSortedElement list

        beforeSortedElement.sort()

        # After Sort based on price - Low to High
        # Select dropdown lo to hi (browser sorting) and store in list afterSortedElement
        afterSortedElement = []
        dropdown = Select(self.driver.find_element(By.CLASS_NAME, "product_sort_container"))
        dropdown.select_by_value("lohi")
        inventory_price_new = self.driver.find_elements(By.CLASS_NAME, "inventory_item_price")
        for element1 in inventory_price_new:
            ele_price_new = element1.text
            string_ele_new = ele_price_new.replace("$", "")
            float_ele_new = float(string_ele_new)
            afterSortedElement.append(float_ele_new)

        # Check if before sort list is equal to after sort list
        assert beforeSortedElement == afterSortedElement

    # Check if products are sorted according to price from high to low

    def test_standard_user_sort_product_price_desc(self, setup):

        # Get before sort inventory price (without sort )

        descBeforeSortedElement = []
        inventory_prices = self.driver.find_elements(By.CLASS_NAME, "inventory_item_price")

        for element in inventory_prices:
            ele_price = element.text
            string_ele = ele_price.replace("$", "")
            float_ele = float(string_ele)
            descBeforeSortedElement.append(float_ele)

        # Sort using code and store price in hi to lo beforeSortedElement list

        descBeforeSortedElement.sort(reverse=True)

        # After Sort based on price - High to Low
        # Select dropdown hi to lo (browser sorting) and store in list afterSortedElement
        afterSortedElement = []
        dropdown = Select(self.driver.find_element(By.CLASS_NAME, "product_sort_container"))
        dropdown.select_by_value("hilo")
        inventory_price_new = self.driver.find_elements(By.CLASS_NAME, "inventory_item_price")

        for element1 in inventory_price_new:
            ele_price_new = element1.text
            string_ele_new = ele_price_new.replace("$", "")
            float_ele_new = float(string_ele_new)
            afterSortedElement.append(float_ele_new)

        # Check if before sort list is equal to after sort list
        assert descBeforeSortedElement == afterSortedElement

    # Check if products are sorted in asc order alphabetically

    def test_standard_user_sort_product_atoz(self, setup):

        # Get before sort inventory price (without sort )

        beforeSortedElement = []

        inventory_names = self.driver.find_elements(By.CLASS_NAME, "inventory_item_name")
        for element in inventory_names:
            ele_price = element.text
            string_ele = ele_price.replace("Sauce Labs ", "")
            beforeSortedElement.append(string_ele)

        # Sort using code and store in asc of inventory name beforeSortedElement list
        beforeSortedElement.sort()

        # After Sort based on price - Low to High
        # Select dropdown a to z (browser sorting) and store in list afterSortedElement
        afterSortedElement = []
        dropdown = Select(self.driver.find_element(By.CLASS_NAME, "product_sort_container"))
        dropdown.select_by_value("az")
        inventory_name_new = self.driver.find_elements(By.CLASS_NAME, "inventory_item_name")
        for element1 in inventory_name_new:
            ele_price_new = element1.text
            string_ele_new = ele_price_new.replace("Sauce Labs ", "")
            afterSortedElement.append(string_ele_new)

        # Check if before sort list is equal to after sort list
        assert beforeSortedElement == afterSortedElement

    # Check if products are sorted in desc order alphabetically

    def test_standard_user_sort_product_ztoa(self, setup):

        # Get before sort inventory price (without sort )

        beforeSortedElement = []

        inventory_names = self.driver.find_elements(By.CLASS_NAME, "inventory_item_name")
        for element in inventory_names:
            ele_price = element.text
            string_ele = ele_price.replace("Sauce Labs ", "")
            beforeSortedElement.append(string_ele)

        # Sort using code and store price in desc order of inventory names beforeSortedElement list
        beforeSortedElement.sort(reverse=True)

        # After Sort based on price - Low to High
        # Select dropdown z to a (browser sorting) and store in list afterSortedElement
        afterSortedElement = []
        dropdown = Select(self.driver.find_element(By.CLASS_NAME, "product_sort_container"))
        dropdown.select_by_value("za")
        inventory_name_new = self.driver.find_elements(By.CLASS_NAME, "inventory_item_name")
        for element1 in inventory_name_new:
            ele_price_new = element1.text
            string_ele_new = ele_price_new.replace("Sauce Labs ", "")
            afterSortedElement.append(string_ele_new)

        # Check if before sort list is equal to after sort list
        assert beforeSortedElement == afterSortedElement

# Test to check if clicked on an inventory name, it is redirected to point to correct inventory item page
    def test_standard_user_if_correct_product_link(self, setup):
        product = self.driver.find_elements(By.CLASS_NAME, "inventory_item_name")[0]
        prod1 = product.text
        self.driver.find_elements(By.CLASS_NAME, "inventory_item_name")[0].click()
        check_product = self.driver.find_element(By.CLASS_NAME, "inventory_details_name")
        prod2 = check_product.text
        assert prod1 == prod2





