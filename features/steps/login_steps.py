from behave import given, when, then
from config.config import BASE_URL
from config.users import USERS
import time
from features.views.login_view import LoginScreen

@given('I am on the login page')
def step_impl(context):
    context.page.goto(BASE_URL)

@when('I login as "{user_type}" user')
def step_impl(context, user_type):
    login_screen = LoginScreen(context.page)
    
    user = USERS[user_type]
    if not user:
        raise ValueError(f"User type '{user_type}' not found in USERS")

    username_field = login_screen.user_textfield()
    password_field = login_screen.password_textfield()
    username_field.fill(user['username'])
    password_field.fill(user['password'])

    login_button = login_screen.login_button()
    login_button.click()
    time.sleep(10)


