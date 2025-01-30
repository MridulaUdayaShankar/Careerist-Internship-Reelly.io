from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@given('Click on Filters')
def click_filters(context):
    context.app.filters.click_filters()


@when('Filter the products by “want to buy”')
def filter_by(context):
    context.app.filters.filter_by()


@when('Click on Apply Filter')
def click_apply_filter(context):
    context.app.filters.click_apply_filter()


@then ('Verify “want to buy” is seen on each card')
def verify_want_to_buy_filter(context):
    context.app.secondary_listings_page.verify_want_to_buy_filter()


@then('Go to the final page using the pagination button')
def forward_pagination(context):
    context.app.secondary_listings_page.forward_pagination()


@then('Go back to the first page using the pagination button')
def backward_pagination(context):
    context.app.secondary_listings_page.backward_pagination()