from pages.base_page import Page
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select

class Header(Page):

    MAC = (By.CSS_SELECTOR, 'a[href="https://gettop.us/product-category/macbook/"]')

    def click_mac(self):
        self.click(*self.MAC)