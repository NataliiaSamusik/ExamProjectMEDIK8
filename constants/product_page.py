
class ProductPageConst:
    """Stores constants related to Product"""
    # Product page
    STAFF_PAGE_XPATH = './/h1'
    STAFF_PAGE_TEXT = "Продукти"
    CHANGE_VIEW_XPATH = './/div[@data-value="list"]'
    LIST_VIEW_XPATH = './/div[@class="description"]'
    # Filters
    FILTER_XPATH ='.//div[@class="utils-filter icon-m js-is-hint js-show-filter-menu"]'
    PORES_XPATH = './/div[@class="filter-list"]//ul[.//li[.//a[contains(text(),"Розширені пори")]]]'
    # Buy product
    BUY_PRODUCT_XPATH = './/a[@item_id="69"]'


