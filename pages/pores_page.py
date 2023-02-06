from constants.pores_page import PoresPageConst
from pages.base_page import BasePage
from pages.utils import log_wrapper

class PoresPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.const = PoresPageConst

    @log_wrapper
    def verify_pores_page(self):
        """Verify that correct page is opened"""
        assert self.compare_element_text(xpath=self.const.PORES_PAGE_XPATH, text=self.const.PORES_PAGE_TEXT)
