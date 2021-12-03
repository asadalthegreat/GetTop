from behave import when, then


@when('I click on the search icon')
def click_search_icon(context):
    context.app.header.click_search()


@when('I input {text} into the search bar and hit enter')
def search_in_searchbar(context, text):
   context.app.header.search_in_searchbar(text)


@then('I verify the results are in the {expected_text} category')
def verify_correct_search_results(context, expected_text):
    expected_text = expected_text.upper()
    context.app.header.verify_correct_category(expected_text)


@then('I verify the text {expected_text}')
def verify_no_product_results(context, expected_text):
    context.app.header.verify_no_products(expected_text)