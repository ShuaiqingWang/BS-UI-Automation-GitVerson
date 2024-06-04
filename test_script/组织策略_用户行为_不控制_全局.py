import re
import time
from playwright.sync_api import Page



def userAction1(page: Page):
    time.sleep(4.5)
    page.get_by_role("button", name="编辑").click()
    #page.get_by_role("row", name="页面复制 请选择  全局 ").get_by_placeholder("请选择").click()
    page.get_by_role("row", name="页面复制 请选择").get_by_placeholder("请选择").click()

    #* time.sleep(3)
    #expect(page.get_by_role("list").locator("li").filter(has_text="审计")).to_be_visible()
    # time.sleep(3)
    page.get_by_role("list").get_by_text("不控制").click()

    time.sleep(0.5)
    page.get_by_role("row", name="页面打印 请选择").get_by_placeholder("请选择").click()
    page.get_by_role("list").get_by_text("不控制").click()
    time.sleep(0.5)
    page.get_by_role("row", name="网页另存为 请选择").get_by_placeholder("请选择").click()
    page.get_by_role("list").get_by_text("不控制").click()
    time.sleep(0.5)
    page.get_by_role("row", name="查看页面源代码 请选择").get_by_placeholder("请选择").click()
    page.get_by_role("list").get_by_text("不控制").click()
    time.sleep(0.5)
    page.get_by_role("row", name="文件上传 请选择").get_by_placeholder("请选择").click()
    page.get_by_role("list").get_by_text("不控制").click()
    time.sleep(0.5)
    page.get_by_role("row", name="文件下载 请选择").get_by_placeholder("请选择").click()
    page.get_by_role("list").get_by_text("不控制").click()
    time.sleep(0.5)
    page.get_by_role("row", name="页面截图 请选择").get_by_placeholder("请选择").click()
    page.get_by_role("list").get_by_text("不控制").click()
    time.sleep(0.5)
    page.get_by_role("row", name="开发者工具 请选择").get_by_placeholder("请选择").click()
    page.get_by_role("list").get_by_text("不控制").click()

    page.get_by_role("button", name="保存").click()
    page.get_by_role("button", name="确 定").click()