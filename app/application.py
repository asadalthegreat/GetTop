from pages.main_page import MainPage
from pages.header import Header
from pages.homepage import Homepage
from pages.product_category_page import Category



class Application:

    def __init__(self, driver):
        self.driver = driver
        self.main_page = MainPage(self.driver)
        self.homepage = Homepage(self.driver)
        self.header = Header(self.driver)
        self.product_category_page = Category(self.driver)

