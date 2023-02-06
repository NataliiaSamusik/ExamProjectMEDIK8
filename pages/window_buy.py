from constants.buy_window import BuyWindowConst

from pages.base_page import BasePage
from pages.start_page import StartPage
from pages.utils import log_wrapper


class Window(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.const = BuyWindowConst


    @log_wrapper
    def product_window(self):
        """Navigate to basket"""
        self.click(self.const.GO_TO_BASKET_XPATH)

        from pages.basket_page import BasketPage
        return BasketPage(self.driver)
