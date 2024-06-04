from playwright.sync_api import Page, Playwright, Browser, BrowserContext


current_page_url = "http://10.21.20.226:7443/"
def open_base_url(page: Page) -> None:

## 当前启用端口 URL
    page.goto(current_page_url)


def create_context_and_page(playwright: Playwright, headless: bool = False) -> (Browser, BrowserContext, Page):
    browser = playwright.chromium.launch(headless=headless, args=["--ignore-certificate-errors"])
    context = browser.new_context(ignore_https_errors=True)
    page = context.new_page()
    return browser, context, page


def get_testing_endpoint():
    # Return the current page URL
    return current_page_url
