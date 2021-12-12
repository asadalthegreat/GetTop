from pages.base_page import Page
from selenium.webdriver.common.by import By

class Homepage(Page):

    ARROW_LOCATOR = (By.XPATH, '//div[@class="slider-wrapper relative"]//button[@aria-label="{ARROW}"]')
    DOT_LOCATOR = (By.CSS_SELECTOR, 'li[aria-label="Page dot {DOT}"]')
    IPAD_BANNER = (By.CSS_SELECTOR, 'a[href="/product-category/ipad/"]')
    MACBOOK_BANNER = (By.CSS_SELECTOR, 'a[href="/product-category/macbook/"]')
    BROWSE_TEXT = (By.XPATH, '//span[text()="Browse our Categories"]')
    DEVICE_LOCATOR = (By.CSS_SELECTOR, 'img[alt="{DEVICE}"]')
    FOOTER_DEVICE_LOCATOR = (By.XPATH, '//ul[@id]//li//a[text()="{DEVICE}"]')
    BACK_TO_TOP = (By.CSS_SELECTOR, 'a.back-to-top')
    BEST_SELLING = (By.XPATH, '//span[text()="Best Selling"]')
    LATEST = (By.XPATH, '//span[text()="Latest"]')
    TOP_RATED = (By.XPATH, '//span[text()="Top Rated"]')


    def _get_expected_arrow(self, arrow):
        return [self.ARROW_LOCATOR[0], self.ARROW_LOCATOR[1].replace('{ARROW}', arrow)]

    def click_arrow(self, arrow: str):
        locator = self._get_expected_arrow(arrow)
        self.click(*locator)

    def _get_expected_dot(self, dot):
        return [self.DOT_LOCATOR[0], self.DOT_LOCATOR[1].replace('{DOT}', dot)]

    def click_dot(self, dot: str):
        locator = self._get_expected_dot(dot)
        self.click(*locator)


    def ipad_banner_is_visible(self):
        self.wait_for_element_appear(*self.IPAD_BANNER)

    def macbook_banner_is_visible(self):
        self.wait_for_element_appear(*self.MACBOOK_BANNER)

    def back_to_top_is_visible(self):
        self.wait_for_element_appear(*self.BACK_TO_TOP)

    def footer_categories_are_visible(self):
        self.wait_for_element_appear(*self.BEST_SELLING)
        self.wait_for_element_appear(*self.LATEST)
        self.wait_for_element_appear(*self.TOP_RATED)

    def footer_product_elements_are_visible(self):
        print('test')

    def click_ipad_banner(self):
        self.click(*self.IPAD_BANNER)

    def click_macbook_banner(self):
        self.click_arrow('Next')
        self.wait_for_element_appear(*self.MACBOOK_BANNER)
        self.click(*self.MACBOOK_BANNER)

    def verify_correct_url(self, device: str):
        self.verify_url_contains_query(device)

    def browse_our_categories_text(self):
        self.wait_for_element_appear(*self.BROWSE_TEXT)

    def _get_expected_device(self, device):
        return [self.DEVICE_LOCATOR[0], self.DEVICE_LOCATOR[1].replace('{DEVICE}', device)]

    def click_device_category(self, device: str):
        locator = self._get_expected_device(device)
        self.click(*locator)

    def _get_footer_expected_device(self, device):
        return [self.FOOTER_DEVICE_LOCATOR[0], self.FOOTER_DEVICE_LOCATOR[1].replace('{DEVICE}', device)]

    def click_footer_device_category(self, device: str):
        locator = self._get_footer_expected_device(device)
        self.click(*locator)

