from behave import when, then


@then('I click on the {direction} banner arrow')
def click_arrow(context, direction):
    context.app.homepage.click_arrow(direction)


@then('I click on bottom dot {num}')
def click_dot(context, num):
    context.app.homepage.click_dot(num)


@then('the iPad banner is visible')
def ipad_banner_is_visible(context):
    context.app.homepage.ipad_banner_is_visible()


@then('the Macbook banner is visible')
def macbook_banner_is_visible(context):
    context.app.homepage.macbook_banner_is_visible()


@when('I click on the iPad banner')
def click_ipad_banner(context):
    context.app.homepage.click_ipad_banner()


@when('I click on the macbook banner')
def click_macbook_banner(context):
    context.app.homepage.click_macbook_banner()


@then('I verify that I\'ve navigated to the {device} category page')
def verify_correct_url(context, device):
    device = device.lower()
    context.app.homepage.verify_correct_url(device)


@when('Browse Our Categories text is visible')
def browse_our_categories_text(context):
    context.app.homepage.browse_our_categories_text()


@when('best Selling, Latest, and Top Rated Categories are visible')
def footer_categories_are_visible(context):
    context.app.homepage.footer_categories_are_visible()


@when('all products in the footer have a price, name, and star-rating')
def footer_product_elements_are_visible(context):
    context.app.footer_product_elements_are_visible(context)


@when('footer has a button to go back to the top')
def back_to_top_is_visible(context):
    context.app.homepage.back_to_top_is_visible()

@then('I click on the {device} category')
def click_device_category(context, device):
    context.app.homepage.click_device_category(device)

@then('I click on the footer device {device}')
def click_footer_device_category(context, device):
    context.app.homepage.click_footer_device_category(device)
