import re
import time
from playwright.sync_api import Page

def client_un(page: Page):


    time.sleep(2)
    page.get_by_role("tab", name="客户端策略").click()
    time.sleep(2)
    page.get_by_role("button", name="编辑").click()

    time.sleep(2)
    page.get_by_role("row", name="地址栏 请选择").locator("i").click()
    page.get_by_role("list").get_by_text("不显示", exact=True).click()

    time.sleep(1)
    page.get_by_role("row", name="收藏栏 请选择").locator("i").click()
    page.get_by_role("list").get_by_text("不显示", exact=True).click()

    time.sleep(1)
    page.get_by_role("row", name="扩展程序 请选择").locator("i").click()
    page.get_by_role("list").get_by_text("不显示", exact=True).click()

    time.sleep(1)
    page.get_by_role("button", name="保存").click()
    page.get_by_role("button", name="确 定").click()

