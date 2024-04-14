import pytest
from selenium import webdriver


@pytest.fixture(scope="class")

def setup(request):
    driver = webdriver.Chrome()
    login_page_url = "https://www.saucedemo.com/"
    inventory_page_url = "https://www.saucedemo.com/inventory.html"
    cart_page_url = "https://www.saucedemo.com/cart.html"
    checkout_step_one_page_url = "https://www.saucedemo.com/checkout-step-one.html"
    checkout_step_two_page_url = "https://www.saucedemo.com/checkout-step-two.html"
    checkout_complete_page_url = "https://www.saucedemo.com/checkout-complete.html"
    request.cls.driver = driver
    request.cls.login_page_url = login_page_url
    request.cls.inventory_page_url = inventory_page_url
    request.cls.cart_page_url = cart_page_url
    request.cls.checkout_step_one_page_url = checkout_step_one_page_url
    request.cls.checkout_step_two_page_url = checkout_step_two_page_url
    request.cls.checkout_complete_page_url = checkout_complete_page_url

    #yield
    #driver.close()



