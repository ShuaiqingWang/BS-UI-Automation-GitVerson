import re
import time
from playwright.sync_api import Page

def watermarking_assign(page: Page):

    page.get_by_role("tab", name="水印策略").click()
    page.get_by_role("button", name="编辑").click()

    time.sleep(2)
    page.get_by_role("row", name="网页水印保护 请选择").locator("i").click()
    page.get_by_text("允许，明水印").click()


#指定
    page.get_by_role("cell", name="全局").locator("span").nth(1).click()
    page.get_by_role("radio", name="指定").click()
    page.get_by_label("修改策略生效范围").get_by_role("textbox").first.click()
    page.get_by_role("list").get_by_text("默认").click()
    page.get_by_label("修改策略生效范围").locator("i").nth(2).click()
    page.get_by_role("button", name="保 存").click()


    time.sleep(1)
    page.get_by_role("row", name="文件水印保护 请选择").locator("i").click()
    page.get_by_text("允许，文件头暗水印").click()
    # 指定
    page.get_by_role("cell", name="全局").locator("span").nth(1).click()
    page.get_by_role("radio", name="指定").click()
    page.get_by_label("修改策略生效范围").get_by_role("textbox").first.click()
    page.get_by_role("list").get_by_text("默认").click()
    page.get_by_label("修改策略生效范围").locator("i").nth(2).click()
    page.get_by_role("button", name="保 存").click()






    page.get_by_role("button", name="保存").click()
    page.get_by_role("button", name="确 定").click()
