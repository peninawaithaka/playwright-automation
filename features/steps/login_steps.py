import time
from behave import given, when, then

from features.views.login_view import LoginScreen

@given('I am on the login page')
def step_impl(context):
    context.page.goto(context.base_url)

@when(u'I login as "{user_type}" user in the sauce demo application')
def step_impl(context, user_type):
    login_screen = LoginScreen(context.page)

    user = context.users[user_type]

    username_field = login_screen.user_textfield()
    password_field = login_screen.password_textfield()

    username_field.fill(user['username'])
    password_field.fill(user['password'])

    login_button = login_screen.login_button()
    login_button.click()    

@then(u'I should be logged in successfully')
def step_impl(context):
    login_screen = LoginScreen(context.page)
    app_logo = login_screen.get_logo()
    assert app_logo.text_content() == 'Swag Labs', f"Expected: {'Swag Labs'} but found: {app_logo.text_content()}"


@when(u'I login with all configured credential')
def step_impl(context):

    context.results = []

    for user_type, user in context.users.items():
        login_screen = LoginScreen(context.page)

        login_screen.user_textfield().fill(user['username'])
        login_screen.password_textfield().fill(user['password'])
        login_screen.login_button().click()

        if login_screen.get_error_message().is_visible():
            actual = 'error'
        else:
            actual = 'success'

        expected = user.get("expected", "success")

        context.results.append({
            'user': user_type,
            'expected': expected,
            'actual': actual
                                })

        #resetting state for each user login
        context.page.goto(context.base_url)


@then(u'Login behaviour should be correct')
def step_impl(context):
    for result in context.results:
        assert result['expected'] == result['actual'], (
            f"Expected: {result['expected']} from {result['user']} but found: {result['actual']}")



# #running multiple users for the given test - examples: written within the feature file
# @when(u'I login with username "{username}" and password "{password}" on the sauce demo page')
# def step_impl(context, username, password):
#     login_screen = LoginScreen(context.page)
    
#     username_field = login_screen.user_textfield()
#     password_field = login_screen.password_textfield()

#     username_field.fill(username)
#     password_field.fill(password)

#     login_button = login_screen.login_button()
#     login_button.click()
#     time.sleep(10)


# @then(u'I should see a "{results}" message')
# def step_impl(context, results):
#     login_screen = LoginScreen(context.page)

#     if results == 'success':
#         app_logo = login_screen.get_logo()
#         assert app_logo.text_content() == 'Swag Labs', f"Expected: {'Swag Labs'} but found: {app_logo.text_content()}"
#     else:
#         error_msg = login_screen.get_error_message()
#         assert error_msg.is_visible()

