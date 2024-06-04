import re
import time
from playwright.sync_api import Page


def click_main_page_action(page: Page):
    time.sleep(1)
    page.get_by_role("menuitem", name="首页").click()
    time.sleep(1)