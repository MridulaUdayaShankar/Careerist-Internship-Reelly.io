from behave import given, when, then
from time import sleep

@when ('Click on Market button')
def click_market_btn(context):
    context.app.market_page.click_market_btn()

@then ('Verify Market page opens')
def verify_market_page_opens(context):
    context.app.market_page.verify_market_page_opens()

@when ('Click on Add Company button')
def click_add_company(context):
    context.app.market_page.click_add_company()

# @then ('Verify Publish my company button is available')
# def click_publish_my_company(context):
#     context.app.market_page.click_publish_my_company()

@then ('Click on View page template')
def click_view_page_template(context):
    context.app.market_page.click_view_page_template()

@then ('Click on Send my cv')
def click_send_my_cv(context):
    context.app.market_page.click_send_my_cv()

