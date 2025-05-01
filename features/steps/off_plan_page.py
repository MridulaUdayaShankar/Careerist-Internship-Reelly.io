from behave import given, when, then
from time import sleep

# @given('Open reelly main page')
# def open_main_page(context):
#     context.app.login.open_main_page()

@given('click on Off-plan at the left side menu')
def click_offplan(context):
    context.app.off_plan_page.click_offplan()

@then('verify the offplan page opens')
def verify_offplan_page_opens(context):
    context.app.off_plan_page.verify_off_plan_page_opens()

@when ('click on filter by sale status')
def click_on_filter_by_sale_status(context):
    context.app.off_plan_page.click_on_filter_by_sale_status_of_announced()

@when ('click on announced filter')
def click_announced_filter(context):
    context.app.off_plan_page.click_announced_filter()

@then ('verify each product contains the filter Announced')
def verify_announced_filter(context):
    context.app.off_plan_page.verify_announced_filter()



