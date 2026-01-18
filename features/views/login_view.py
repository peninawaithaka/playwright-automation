from playwright.sync_api import Page, Locator, expect

class LoginScreen:
    def __init__(self, page:Page):
        self.page = page

    def user_textfield(self) -> Locator:
        """
        Returns the locator for the username textfield and ensure its present before returning it
        """
        self.page.wait_for_selector('#user-name')
        return self.page.locator('#user-name')

    def password_textfield(self) -> Locator:
        """
        Returns the locator for the password textfield and ensure its present before returning it
        """
        self.page.wait_for_selector('#password')
        return self.page.locator('#password')    
    
    def login_button(self) -> Locator:
        """
        Returns locator for the login button on the login screen
        """
        return self.page.locator('#login-button')