import re
import time
from playwright.sync_api import Page

def watermarking(page: Page):

    time.sleep(4)
    page.get_by_role("menuitem", name="策略管理").click()
    time.sleep(4)
    page.get_by_role("tab", name="水印策略").click()
    page.get_by_role("button", name="编辑").click()

    time.sleep(2)
    page.get_by_role("row", name="网页水印保护 请选择").locator("i").click()
    page.get_by_role("list").get_by_text("禁止").click()

    time.sleep(1)
    page.get_by_role("row", name="文件水印保护 请选择").locator("i").click()
    page.get_by_role("list").get_by_text("禁止").click()
    page.get_by_role("button", name="保存").click()
    page.get_by_role("button", name="确 定").click()
