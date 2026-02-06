import os
import json
from playwright.sync_api import sync_playwright
from config.browser import ChromeBrowser, FirefoxBrowser, SafariBrowser

def get_browser_instance(playwright):
    browser_name = os.getenv("BROWSER", "chrome").lower() #defaults to chrome
    if browser_name == 'chrome':
        return ChromeBrowser(playwright)
    if browser_name == 'firefox':
        return FirefoxBrowser(playwright)
    if browser_name == 'safari':
        return SafariBrowser(playwright)
    else:
        raise ValueError(f"Unsupported browser: {browser_name}")


def before_all(context):
    """Run once before all tests."""

    context.playwright = sync_playwright().start()

    browser_instance = get_browser_instance(context.playwright)

    headless = os.getenv("HEADLESS", "true").lower() == 'true'
    context.page = browser_instance.launch(headless=headless)

    # Load JSON config
    config_path = os.path.join(os.path.dirname(__file__), '..', 'config', 'config.json')
    with open(config_path, 'r') as f:
        config = json.load(f)

    # Choose environment
    env = os.getenv('TEST_ENV', 'staging')
    context.config = config['environments'][env]
    context.base_url = context.config['url']
    context.users = context.config['users']


def after_step(context, step):
    """Runs after each step; takes screenshot if step failed."""
    if step.status == "failed" and hasattr(context, "page"):
        os.makedirs("reports/screenshots", exist_ok=True)
        # Build safe filename
        step_name_safe = step.name.replace(" ", "_").replace('"', '').replace("'", "")
        filename = f"reports/screenshots/{step_name_safe}.png"
        context.page.screenshot(path=filename)
        print(f"Screenshot captured: {filename}")


def after_all(context):
    """Run once after all tests; safely close Playwright."""
    if hasattr(context, "page"):
        context.page.close()
    if hasattr(context, "browser"):
        context.browser.close()
    if hasattr(context, "playwright"):
        context.playwright.stop()
