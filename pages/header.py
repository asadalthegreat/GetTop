from pages.base_page import Page
from selenium.webdriver.common.by import By

class Header(Page):

    SEARCH_ICON = (By.CSS_SELECTOR, 'i.icon-search')
    SEARCH_FIELD = (By.CSS_SELECTOR, 'input#woocommerce-product-search-field-0')
    NO_PRODUCTS = (By.CSS_SELECTOR, 'p.woocommerce-info')
    CATEGORY = (By.CSS_SELECTOR, 'p.category')
    MAC = (By.CSS_SELECTOR, 'a[href="https://gettop.us/product-category/macbook/"]')

    def search_in_searchbar(self, text):
        self.input_text(text, *self.SEARCH_FIELD)
        self.hit_enter(*self.SEARCH_FIELD)

    def click_search(self):
        self.click(*self.SEARCH_ICON)

    def verify_correct_category(self, expected_text):
        self.verify_text(expected_text, *self.CATEGORY)

    def verify_no_products(self, expected_text):
        self.verify_text(expected_text, *self.NO_PRODUCTS)

    def click_mac(self):
        self.click(*self.MAC)