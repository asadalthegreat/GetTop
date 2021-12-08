from pages.base_page import Page
from selenium.webdriver.common.by import By

class Homepage(Page):

    ARROW_LOCATOR = (By.XPATH, '//div[@class="slider-wrapper relative"]//button[@aria-label="{ARROW}"]')
    DOT_LOCATOR = (By.CSS_SELECTOR, 'li[aria-label="Page dot {DOT}"]')
    IPAD_BANNER = (By.CSS_SELECTOR, 'a[href="/product-category/ipad/"]')
    MACBOOK_BANNER = (By.CSS_SELECTOR, 'a[href="/product-category/macbook/"]')
    BROWSE_TEXT = (By.XPATH, '//span[text()="Browse our Categories"]')
    ACCESS_CATEGORY = (By.CSS_SELECTOR, 'img[alt="Accessories"]')
    IPAD_CATEGORY = (By.CSS_SELECTOR, 'img[alt="iPad"]')
    IPHONE_CATEGORY = (By.CSS_SELECTOR, 'img[alt="iPhone"]')
    MACBOOK_CATEGORY = (By.CSS_SELECTOR, 'img[alt="MacBook"]')
    DEVICE_LOCATOR = (By.CSS_SELECTOR, 'img[alt="{DEVICE}"]') #This locator isn't working, I'm not sure why - something with uppercase


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

    def browse_our_categories_text(self):
        self.wait_for_element_appear(*self.BROWSE_TEXT)

    # More efficient implementation if done correctly
    def _get_expected_device(self, device):
        return [self.DEVICE_LOCATOR[0], self.DEVICE_LOCATOR[1].replace('{DEVICE}', device)]

    def click_device_category(self, device: str):
        locator = self._get_expected_device(device)
        self.click(*locator)

    def click_accessories_cat(self):
        self.click(*self.ACCESS_CATEGORY)

    def click_ipad_cat(self):
        self.click(*self.IPAD_CATEGORY)

    def click_iphone_cat(self):
        self.click(*self.IPHONE_CATEGORY)

    def click_macbook_cat(self):
        self.click(*self.MACBOOK_CATEGORY)
