import os
from playwright.sync_api import sync_playwright

class BrowserInterface:
    """Common Interface for all browsers"""

    def launch(self, headless=True):
        #implemented by child classes
        raise NotImplementedError
    
class ChromeBrowser(BrowserInterface):
    def __init__(self, playwright):
        self.playwright = playwright
        self.browser = None
        self.context = None

    def launch(self, headless=True):

        self.browser = self.playwright.chromium.launch(
            headless=headless,
            args=["--disable-dev-shm-usage"]
        )
        self.context = self.browser.new_context(
            viewport={"width": 1920, "height": 1080}
        )
        return self.context.new_page()
    
class FirefoxBrowser(BrowserInterface):
    def __init__(self, playwright):
        self.playwright = playwright
        self.browser = None
        self.context = None

    def launch(self, headless=True):
        self.browser = self.playwright.firefox.launch(
            headless = headless,
            firefox_user_prefs = {
                "dom.webdriver.enabled": False
            }
        )
        self.context = self.browser.new_context()
        return self.context.new_page()

class SafariBrowser(BrowserInterface):
    def __init__(self, playwright):
        self.playwright = playwright
        self.browser = None
        self.context = None
    
    def launch(self, headless=True):
        self.browser = self.playwright.webkit.launch(headless=headless)
        self.context = self.browser.new_context()
        return self.context.new_page()
    
