from behave import given, when, then
from time import sleep

# @given('Open reelly main page')
# def open_main_page(context):
#     context.app.login.open_main_page()

@given('Click on Off-plan at the left side menu')
def click_offplan(context):
    context.app.off_plan_page.click_offplan()

@then('Verify the offplan page opens')
def verify_offplan_page_opens(context):
    context.app.off_plan_page.verify_offplan_page_opens()

@when ('Click on filter by sale status')
def click_sale_status(context):
    context.app.off_plan_page.click_sale_status()

@when ('Click on announced filter')
def click_announced_filter(context):
    context.app.off_plan_page.click_announced_filter()

@then ('Click on filter by sale status')
def click_sale_status(context):
    context.app.off_plan_page.click_sale_status()

@then ('Verify each product contains the filter Announced')
def verify_announced_filter(context):
    context.app.off_plan_page.verify_announced_filter()



