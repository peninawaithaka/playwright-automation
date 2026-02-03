import os
import json
from playwright.sync_api import sync_playwright

def before_all(context):
    """Run once before all tests."""

    # Headless toggle via environment variable
    headless_str = os.getenv("HEADLESS", "true")
    context.headless = headless_str.lower() == "true"

    # Start Playwright
    context.playwright = sync_playwright().start()
    context.browser = context.playwright.chromium.launch(
        headless=context.headless,
        args=["--disable-dev-shm-usage"]
    )
    context.page = context.browser.new_page()

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
