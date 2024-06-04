from playwright.sync_api import Page, Playwright, Browser, BrowserContext

# Define a variable to hold the current page's URL at the module level
#current_page_url = "http://10.21.20.227:7443/"

#current_page_url = "http://10.21.20.193:7443/"
current_page_url = "http://10.21.20.226:7443/"

#current_page_url = "https://10.21.20.226:7443/"


# http://10.21.20.193:7443/
#
#
# http://10.21.20.226:18080/
#
#
# http://10.21.20.193:18080/
#
#
# http://10.21.20.227:18080/


def open_base_url(page: Page) -> None:

# # 当前启用端口 URL
    # Navigate to the base URL
    page.goto(current_page_url)
    # page.goto(current_page_url + "login?redirect=%2F")


def create_context_and_page(playwright: Playwright, headless: bool = False) -> (Browser, BrowserContext, Page):
    browser = playwright.chromium.launch(headless=headless, args=["--ignore-certificate-errors"])
    context = browser.new_context(ignore_https_errors=True)
    page = context.new_page()
    return browser, context, page


def get_testing_endpoint():
    # Return the current page URL
    return current_page_url
