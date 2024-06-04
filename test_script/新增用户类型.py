import re
import time
from playwright.sync_api import Page

def userType(page: Page):

    page.get_by_text("用户中心").first.click()
    page.get_by_role("menuitem", name="用户类型管理").click()
    page.get_by_role("button", name="新增").click()
    page.get_by_role("dialog", name="新增用户类型").get_by_placeholder("请输入用户类型名称").click()
    page.get_by_role("dialog", name="新增用户类型").get_by_placeholder("请输入用户类型名称").fill("测试新增用户类型")
    page.locator("label").filter(has_text="全选/全不选").locator("span").nth(1).click()
    page.get_by_role("button", name="确 定").click()



    # ---------------------
