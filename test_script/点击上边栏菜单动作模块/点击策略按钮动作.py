import re
import time
from playwright.sync_api import Page


def click_strategy_action(page: Page):
    time.sleep(4.5)
    page.get_by_role("menuitem", name="策略管理").click()
    time.sleep(4)