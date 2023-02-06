"""Tests related to start page"""
import logging
import pytest
from conftest import start_page
from constants.base import BaseConstants


@pytest.mark.parametrize("browser", [BaseConstants.CHROME, BaseConstants.FIREFOX])
class TestBasketPage:
    """Stores tests for Basket page"""

    def test_delete_product(self, start_page, product_page):
        """
        - Pre-conditions:
            - Open Product page
        - Steps:
            - Select product and click on BUY button
            - Click on Go to basket button
            - Delete product from basket
            - Verify empty basket
        """
        # Select product and click on BUY button
        go_to_basket = product_page.buy_product()
        # Click on Go to basket button
        basket_page = go_to_basket.product_window()
        # Delete product from basket
        empty_basket = basket_page.delete_product()
        # Verify empty basket
        basket_page.verify_empty_basket()



