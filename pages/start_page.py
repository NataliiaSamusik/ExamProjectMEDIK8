from constants.start_page import StartPageConst
from pages.base_page import BasePage
from pages.utils import wait_until_ok, log_wrapper

class StartPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.const = StartPageConst

    @wait_until_ok(timeout=10, period=1)
    @log_wrapper
    def go_to_products_by_basket(self):
        """Navigate to product page via basket"""
        self.click(xpath=self.const.BASKET_XPATH)
        self.click(xpath=self.const.BASKET_ADD_XPATH)

        from pages.product_page import ProductPage
        return ProductPage(self.driver)

    @log_wrapper
    def empty_field_for_subcription(self):
        """Click on Subscribe button, leave input field empty"""
        self.click(xpath=self.const.SUBSCRIBE_BUTTON_XPATH)

    @log_wrapper
    def verify_red_border(self):
        """Verify that input field has red borders"""
        assert self.is_element_visible(xpath=self.const.RED_BORDER_XPATH)
