"""Tests related to start page"""
import logging
import pytest

from conftest import start_page
from constants.base import BaseConstants


@pytest.mark.parametrize("browser", [BaseConstants.CHROME, BaseConstants.FIREFOX])
class TestProductPage:
    """Stores tests for Product page"""
    # Select filters Pores and check that correct page is opened
    def test_filter_product(self, start_page, product_page):
        """
        - Pre-conditions:
            - Open start page
            - Navigate to Product Page
        - Steps:
            - Open filters
            - Select Pores filter
            - Verify correct page is opened
        """
        # Open filters and Select Pores filter
        pores_page = product_page.select_filter_pores()
        # Verify correct page is opened
        pores_page.verify_pores_page()