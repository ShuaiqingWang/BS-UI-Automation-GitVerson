import re
import time
from playwright.sync_api import Page

def access2(page: Page):

    time.sleep(2)
    page.get_by_role("tab", name="访问策略").click()
    time.sleep(3)
    page.get_by_role("button", name="编辑").click()


    #使用绑定设备访问
    time.sleep(3)
    page.get_by_role("row", name="使用绑定设备访问 请选择").get_by_placeholder("请选择").click()
    page.get_by_role("list").get_by_text("启用", exact=True).click()
    #指定
    time.sleep(0.5)
    page.get_by_role("row", name="使用绑定设备访问 请选择").locator("span").nth(3).click()
    page.get_by_role("radio", name="指定").click()
    time.sleep(0.5)
    page.get_by_label("修改策略生效范围").get_by_role("textbox").first.click()
    page.get_by_role("list").get_by_text("默认").click()
    page.get_by_label("修改策略生效范围").locator("i").nth(2).click()
    page.get_by_role("button", name="保 存").click()


    #日常工作时间访问
    time.sleep(0.5)
    page.get_by_role("row", name="日常工作时间访问 请选择").get_by_placeholder("请选择").click()
    page.get_by_role("list").locator("li").filter(has_text=re.compile(r"^启用$")).click()
    #指定
    # time.sleep(0.5)
    # page.get_by_role("row", name="日常工作时间访问 请选择").locator("span").nth(3).click()
    # page.get_by_role("radio", name="指定").click()
    # page.get_by_label("修改策略生效范围").get_by_role("textbox").first.click()
    # page.get_by_role("list").get_by_text("默认").click()
    # page.get_by_label("修改策略生效范围").locator("i").nth(2).click()
    # page.get_by_role("button", name="保 存").click()


    #使用公司网络访问
    time.sleep(0.5)
    page.get_by_role("row", name="使用公司网络访问 请选择").get_by_placeholder("请选择").click()
    page.get_by_role("list").locator("li").filter(has_text=re.compile(r"^启用$")).click()
    page.get_by_role("cell", name="全局 ").locator("span").nth(1).click()
    page.get_by_role("radio", name="指定").click()
    page.get_by_label("修改策略生效范围").get_by_role("textbox").first.click()
    page.locator("li").filter(has_text="默认").click()
    page.get_by_label("修改策略生效范围").locator("i").nth(2).click()
    #page.get_by_label("修改策略生效范围").nth(2).click()

    page.get_by_role("button", name="保 存").click()


    time.sleep(0.5)
    page.get_by_role("button", name="保存").click()
    page.get_by_role("button", name="确 定").click()

    # ---------------------
