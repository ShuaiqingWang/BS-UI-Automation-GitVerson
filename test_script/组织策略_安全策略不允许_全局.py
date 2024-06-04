import re
import time
from playwright.sync_api import Page

def secure3(page: Page):
    time.sleep(3)
    page.get_by_role("tab", name="安全策略").click()
    time.sleep(3)
    page.get_by_role("button", name="编辑").click()

    time.sleep(3)
    page.get_by_role("row", name="清除浏览器历史记录 请选择").get_by_placeholder("请选择").click()
    #page.get_by_role("row", name="清除浏览器历史记录 请选择").locator("i").click()
    page.get_by_role("list").get_by_text("不允许").click()

    time.sleep(0.5)
    page.get_by_role("row", name="禁止跟踪DNT功能 请选择").get_by_placeholder("请选择").click()
    #page.get_by_role("row", name="禁止跟踪DNT功能 请选择").locator("i").click()
    page.get_by_role("list").get_by_text("不允许").click()


    time.sleep(0.5)
    page.get_by_role("button", name="保存").click()
    page.get_by_role("button", name="确 定").click()
