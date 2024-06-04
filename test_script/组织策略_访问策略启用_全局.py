import re
import time
from playwright.sync_api import Page

def access1(page: Page):
    time.sleep(3)
    page.get_by_role("tab", name="访问策略").click()
    time.sleep(3)
    page.get_by_role("button", name="编辑").click()

    time.sleep(3)
    page.get_by_role("row", name="使用绑定设备访问 请选择").get_by_placeholder("请选择").click()
    page.get_by_role("list").get_by_text("启用", exact=True).click()

    time.sleep(0.5)
    page.get_by_role("row", name="日常工作时间访问 请选择").get_by_placeholder("请选择").click()
    page.get_by_role("list").locator("li").filter(has_text=re.compile(r"^启用$")).click()

    time.sleep(0.5)
    page.get_by_role("row", name="使用公司网络访问 请选择").get_by_placeholder("请选择").click()
    page.get_by_role("list").get_by_text("启用", exact=True).click()

    time.sleep(0.5)
    page.get_by_role("button", name="保存").click()
    page.get_by_role("button", name="确 定").click()

    # ---------------------
