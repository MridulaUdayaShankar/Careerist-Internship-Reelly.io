from behave import given, when, then


@when ('Click on “Secondary” option at the left side menu')
def click_secondary_menu(context):
    context.app.main_menu.click_secondary_menu()


@then ('Verify the right page opens')
def verify_right_page_opens(context):
    context.app.main_menu.verify_right_page_opens()


