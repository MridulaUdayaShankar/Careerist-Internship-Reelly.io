from behave import given, when, then
from time import sleep

@when ('Click on Settings')
def click_settings(context):
    context.app.settings_page.click_settings()

@then ('Click on the verification option')
def click_verification_option(context):
    context.app.settings_page.click_verification_option()

@then ('Verify if upload image page opens')
def verify_upload_image_page_opens(context):
    context.app.settings_page.verify_upload_image_page_opens()

@then('Verify upload image button is available')
def verify_upload_image_button_is_available(context):
    context.app.settings_page.verify_upload_image_button_is_available()

@then('Verify next step button is available')
def verify_next_step_button_is_available(context):
    context.app.settings_page.verify_next_step_button_is_available()