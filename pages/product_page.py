from constants.product_page import ProductPageConst
from pages.base_page import BasePage
from pages.utils import log_wrapper

class ProductPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.const = ProductPageConst

    @log_wrapper
    def verify_product_page(self):
        """Verify product page is opened"""
        assert self.compare_element_text(xpath=self.const.STAFF_PAGE_XPATH, text= self.const.STAFF_PAGE_TEXT)

    @log_wrapper
    def change_to_list_view(self):
        """Change view to list view"""
        self.click(xpath=self.const.CHANGE_VIEW_XPATH)

    @log_wrapper
    def verify_list_view(self):
        """Verify view of products is changed to list"""
        assert self.is_element_exists(xpath=self.const.LIST_VIEW_XPATH)

    @log_wrapper
    def select_filter_pores(self):
        """Select filter"""
        self.click(xpath=self.const.FILTER_XPATH)
        self.click(xpath=self.const.PORES_XPATH)

        from pages.pores_page import PoresPage
        return PoresPage(self.driver)

    @log_wrapper
    def buy_product(self):
        """Select product from the list and click 'Buy' button"""
        self.click(xpath=self.const.BUY_PRODUCT_XPATH)

        from pages.window_buy import Window
        return Window(self.driver)


