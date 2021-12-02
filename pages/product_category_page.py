from pages.base_page import Page
from selenium.webdriver.common.by import By

class Category(Page):

    SORT = (By.CSS_SELECTOR, "form.woocommerce-ordering select.orderby")
    HIGH_TO_LOW = (By.XPATH, "//*[contains(text(), 'high to low')]")
    LOW_TO_HIGH = (By.XPATH, "//*[contains(text(), 'low to high')]")
    PRICES = (By.XPATH, "//div[@class='price-wrapper']/span")

    def sort_high_low(self):
        self.click(*self.SORT)
        self.click(*self.HIGH_TO_LOW)


    def sort_low_high(self):
        self.click(*self.SORT)
        self.click(*self.LOW_TO_HIGH)


    def verify_sorted_high_low(self):
        elements = self.find_elements(*self.PRICES)
        prices = []
        for x in elements:
            a = x.text
            if " " in a:
                a = a.split(" ")
                a = a[1]
                prices.append(a)
            else:
                prices.append(a)

        new_prices = []
        for i in prices:
            price = i.replace("$", "")
            price = price.replace(",", "")
            new_prices.append(price)

        int_prices = []
        for i in new_prices:
            i = float(i)
            int_prices.append(i)

        assert int_prices[0] > int_prices[1] > int_prices[2], f'Expected {int_prices[0]} to be the highest price but it is not'

    def verify_sorted_low_high(self):
        elements = self.find_elements(*self.PRICES)
        prices = []
        for x in elements:
            a = x.text
            if " " in a:
                a = a.split(" ")
                a = a[1]
                prices.append(a)
            else:
                prices.append(a)

        new_prices = []
        for i in prices:
            price = i.replace("$", "")
            price = price.replace(",", "")
            new_prices.append(price)

        int_prices = []
        for i in new_prices:
            i = float(i)
            int_prices.append(i)

        assert int_prices[0] < int_prices[1] < int_prices[2], f'Expected {int_prices[0]} to be the lowest price but it is not'



