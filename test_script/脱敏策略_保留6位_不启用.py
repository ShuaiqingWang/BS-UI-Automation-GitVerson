import re
import time

from playwright.sync_api import Page

def data_masking(page: Page):


    page.get_by_role("tab", name="脱敏策略").click()
    time.sleep(3)

##
    page.get_by_role("button", name="编辑").click()
    page.locator("td").filter(has_text="全模糊保留前6位及后2位，其余模糊").locator("i").click()
    page.get_by_text("保留前6位及后2位，其余模糊").click()
 #不启用
    page.get_by_role("row", name="身份证号脱敏 请选择").locator("i").nth(1).click()
    page.get_by_role("list").get_by_text("不启用").click()


    page.locator("td").filter(has_text="全模糊保留前3位及后4位，其余模糊").locator("i").click()
    page.get_by_text("保留前3位及后4位，其余模糊").click()
    # 不启用
    page.get_by_role("row", name="手机号脱敏 请选择").locator("i").nth(1).click()
    page.get_by_role("list").get_by_text("不启用").click()


    page.locator("td").filter(has_text="全模糊保留第一位，@及以后，其余模糊").locator("i").click()
    page.get_by_text("保留第一位，@及以后，其余模糊").click()
    # 不启用
    page.get_by_role("row", name="邮箱脱敏 请选择").locator("i").nth(1).click()
    page.get_by_role("list").get_by_text("不启用").click()




    page.get_by_role("button", name="保存").click()
    page.get_by_role("button", name="确 定").click()
