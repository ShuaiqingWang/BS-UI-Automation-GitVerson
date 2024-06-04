import re
import time
from playwright.sync_api import Page


def click_application_center_action(page: Page):
    time.sleep(4)
    page.get_by_role("menuitem", name="应用中心").click()
    time.sleep(4)