import re
import time
from playwright.sync_api import Page


def click_user_center_action(page: Page):

    page.get_by_text("用户中心").first.click()


