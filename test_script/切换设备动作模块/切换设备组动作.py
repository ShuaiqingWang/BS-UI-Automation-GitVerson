import re
import time
from playwright.sync_api import Page

def switch_device_action(page: Page):

    time.sleep(2)
    page.get_by_role("tab", name="设备分组").click()