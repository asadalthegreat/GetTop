from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

@given('I open the Gettop home page')
def open_gettop(context):
    context.app.main_page.open_main_page()

@when('I click on Mac in the header')
def click_mac(context):
    context.app.header.click_mac()

@when('I change to sort high to low')
def sort_high_low(context):
    context.app.product_category_page.sort_high_low()

@when('I change to sort low to high')
def sort_low_high(context):
    context.app.product_category_page.sort_low_high()

@then ('products are displayed from high to low price')
def verify_sorted_high_low(context):
    context.app.product_category_page.verify_sorted_high_low()

@then ('products are displayed from low to high price')
def verify_sorted_low_high(context):
    context.app.product_category_page.verify_sorted_low_high()



