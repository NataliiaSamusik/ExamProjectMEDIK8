"""Tests related to start page"""
import logging

import pytest

from conftest import start_page, product_page
from constants.base import BaseConstants

@pytest.mark.parametrize("browser", [BaseConstants.CHROME, BaseConstants.FIREFOX])
class TestStartPage:
    """Stores tests for start page """

    # Open Product page via basket page
    def test_go_to_product_page_by_basket(self, start_page, product_page):
        """
        - Pre-conditions:
            - Open start page
        - Steps:
            - Click on basket icon
            - Click on 'Add products' button
            - Verify Products page
        """
        # Verify Products page
        product_page.verify_product_page()

    # Change to list view
    def test_change_view_on_product_page(self, start_page, product_page):
        """
        - Pre-conditions:
            - Open start page
            - Navigate to Product page
        - Steps:
            - Select LIST view icon
            - Verify that view of products is changed to LIST
        """

        # Select LIST view icon
        product_page.change_to_list_view()
        # Verify that view of products is changed to LIST
        product_page.verify_list_view()

    # Verify ERROR for empty email field
    def test_subscribe_empty(self, start_page):
        """
        - Pre-conditions:
            - Open start page
        - Steps:
            - Click on Subscribe button
            - Verify red borders of empty input field
        """

        # Click on Subscribe button
        red_border =  start_page.empty_field_for_subcription()
        # Verify red borders of empty input field
        start_page.verify_red_border()






