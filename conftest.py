import pytest

from pages.start_page import StartPage
from pages.utils import create_driver

@pytest.fixture()
def driver(browser):
    """Creates selenium driver"""
    driver = create_driver(browser=browser)
    yield driver
    driver.close()


@pytest.fixture()
def start_page(driver):
    """Creates start page object"""
    return StartPage(driver)

@pytest.fixture()
def product_page(start_page):
    """Navigate to PRODUCT page"""
    product_page = start_page.go_to_products_by_basket()
    return product_page
