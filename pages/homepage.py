from pages.base_page import Page
from selenium.webdriver.common.by import By

class Homepage(Page):

    ARROW_LOCATOR = (By.XPATH, '//div[@class="slider-wrapper relative"]//button[@aria-label="{ARROW}"]')
    DOT_LOCATOR = (By.CSS_SELECTOR, 'li[aria-label="Page dot {DOT}"]')
    IPAD_BANNER = (By.CSS_SELECTOR, 'a[href="/product-category/ipad/"]')
    MACBOOK_BANNER = (By.CSS_SELECTOR, 'a[href="/product-category/macbook/"]')
    DEVICE_LOCATOR = (By.CSS_SELECTOR, 'a[href="/product-category/{DEVICE}/"]')

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

    def click_ipad_banner(self):
        self.click(*self.IPAD_BANNER)

    def click_macbook_banner(self):
        self.click_arrow('Next')
        self.wait_for_element_appear(*self.MACBOOK_BANNER)
        self.click(*self.MACBOOK_BANNER)

    def verify_correct_url(self, device: str):
        self.verify_url_contains_query(device)

