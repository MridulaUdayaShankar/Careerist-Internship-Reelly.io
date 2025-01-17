from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

# @given('Open reelly main page')
# def open_main_page(context):
#     context.app.login.open_main_page()


@then('Enter email')
def enter_email(context):
    context.app.login_page.enter_email()


@then('Enter password')
def enter_password(context):
    context.app.login_page.enter_password()


@when('Click Continue')
def click_continue(context):
    context.app.login_page.click_continue()


@then('Verify "Off-plan" tab is opened')
def verify_login(context):
    context.app.login_page.verify_login()
