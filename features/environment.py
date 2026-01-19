import os
from playwright.sync_api import sync_playwright

def before_all(context):
    """
    Runs once before all tests.
    Sets up Playwright, browser, and page.
    Reads HEADLESS from environment for CI flexibility.
    """
    headless_str = context.config.userdata.get("headless", "true")
    context.headless = headless_str.lower() == "true"

    context.playwright = sync_playwright().start()

    context.browser = context.playwright.chromium.launch(
        headless=context.headless,
        args=["--disable-dev-shm-usage"]  # CI-friendly
    )
    context.page = context.browser.new_page()


def after_step(context, step):
    """
    Runs after each step.
    Captures screenshot if the step fails.
    """
    if step.status == "failed":
        # Ensure reports/screenshots exists
        os.makedirs("reports/screenshots", exist_ok=True)
        # Build screenshot filename
        filename = f"reports/screenshots/{step.name.replace(' ', '_')}.png"
        context.page.screenshot(path=filename)
        print(f"Screenshot captured: {filename}")


def after_all(context):
    """
    Runs once after all tests.
    Closes browser and stops Playwright.
    """
    context.page.close()
    context.browser.close()
    context.playwright.stop()
