from playwright.sync_api import Page, Locator, expect

class LoginScreen:
    def __init__(self, page:Page):
        self.page = page

    def user_textfield(self) -> Locator:
        return self.page.locator('#user-name')

    def password_textfield(self) -> Locator:
        return self.page.locator('#password')    
    
    def login_button(self) -> Locator:
        return self.page.locator('#login-button')
    
    def get_logo(self) -> Locator:
        return self.page.locator('.app_logo')
    
    def get_error_message(self) -> Locator:
        return self.page.locator('.error-message-container')