import re
import time
from playwright.sync_api import Page

def watermarking_custom_assign(page: Page):

    page.get_by_role("tab", name="水印策略").click()
    time.sleep(2)
    page.get_by_role("button", name="编辑").click()

    time.sleep(2)
    page.get_by_role("row", name="网页水印保护 请选择").locator("i").click()
    page.get_by_text("允许，明水印").click()

    time.sleep(0.5)
#自定义
    # page.get_by_role("button", name="详情").click()
    page.click("text=详情")
    page.get_by_role("button", name=" 编辑水印").click()
    page.locator("label").filter(has_text="自定义内容").locator("span").nth(1).click()
    page.get_by_placeholder("请输入内容").click()
    page.get_by_placeholder("请输入内容").fill("啊水印啊水印水印救救我")
    page.locator("div").filter(has_text=re.compile(r"^水印字号特小小中\(推荐\)大特大$")).locator("i").click()
    page.get_by_text("小", exact=True).click()
    time.sleep(1)
    page.locator(".color-ctn > div:nth-child(2)").click()
    page.get_by_role("button", name="保 存").click()

    time.sleep(1)
    page.get_by_role("button", name="Close").click()

##
    time.sleep(1)
    page.get_by_role("row", name="文件水印保护 请选择").locator("i").click()
    page.get_by_text("允许，文件头暗水印").click()

    # 自定义
    page.get_by_role("row", name="文件水印保护 请选择").get_by_role("button").click()
    page.get_by_role("button", name=" 编辑水印").click()
    page.locator("label").filter(has_text="xlsx").locator("span").nth(1).click()
    page.locator("label").filter(has_text=re.compile(r"^xls$")).locator("span").nth(1).click()
    page.get_by_role("button", name="保 存").click()
    time.sleep(2)
    page.get_by_role("button", name="Close").click()


    page.get_by_role("button", name="保存").click()
    page.get_by_role("button", name="确 定").click()