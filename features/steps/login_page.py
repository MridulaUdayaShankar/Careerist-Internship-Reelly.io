from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@given('Open reelly main page')
def open_main_page(context):
    context.app.login.open_main_page()


@when('Click Continue')
def click_continue(context):
    context.app.click_continue()

@then('Verify Sign in or create new account text is shown')
def verify_login(context):
    context.app.login.verify_login()
