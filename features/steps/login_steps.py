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




# #access the users via a config file
# # @when('I login as "{user_type}" user')
# # def step_impl(context, user_type):
# #     login_screen = LoginScreen(context.page)
    
# #     user = USERS[user_type]
# #     if not user:
# #         raise ValueError(f"User type '{user_type}' not found in USERS")

# #     username_field = login_screen.user_textfield()
# #     password_field = login_screen.password_textfield()
# #     username_field.fill(user['username'])
# #     password_field.fill(user['password'])

# #     login_button = login_screen.login_button()
# #     login_button.click()

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

