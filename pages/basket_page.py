from constants.basket_page import BacketConst

from pages.base_page import BasePage
from pages.start_page import StartPage
from pages.utils import log_wrapper


class BasketPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.const = BacketConst

    @log_wrapper
    def delete_product(self):
        """Click on Delete button"""
        self.click(self.const.DELETE_PRODUCT_XPATH)

    def verify_empty_basket(self):
        """Verify that basket is empty"""
        assert self.compare_element_text(xpath=self.const.EMPTY_BASKET_XPATH, text=self.const.EMPTY_BASKET_TEXT)
