from behave import given, when, then

@then('Verify "Off-plan" tab is opened')
def verify_login(context):
    context.app.main_menu.verify_login()


@when ('Click on “Secondary” option at the left side menu')
def click_secondary_menu(context):
    context.app.main_menu.click_secondary_menu()


@when('Click on “Secondary” option at the left side menu for mobile')
def click_secondary_menu_mobile(context):
    context.app.main_menu.click_secondary_menu_mobile()

@then ('Verify the right page opens')
def verify_right_page_opens(context):
    context.app.main_menu.verify_right_page_opens()


@then ('Verify the right page opens for mobile view')
def verify_right_page_opens_mobile(context):
    context.app.main_menu.verify_right_page_opens_mobile()


