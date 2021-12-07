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
    context.app.homepage.verify_correct_url(device)