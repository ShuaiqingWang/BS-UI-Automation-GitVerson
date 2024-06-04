import re
import time

from playwright.sync_api import Page

def data_masking_assign(page: Page):
    time.sleep(2)
    page.get_by_role("tab", name="脱敏策略").click()
    time.sleep(3)

##
    page.get_by_role("button", name="编辑").click()

#
    page.locator("td").filter(has_text="全模糊保留前6位及后2位，其余模糊").locator("i").click()
    page.get_by_text("保留前6位及后2位，其余模糊").click()
    time.sleep(1)

    ##***
    # page.get_by_role("row", name="身份证号脱敏 请选择  请选择  —").locator("i").nth(1).click()
    # page.get_by_role("list").get_by_text("启用", exact=True).click()
    # page.get_by_role("row", name="手机号脱敏 请选择  请选择  —").locator("i").nth(1).click()
    # page.get_by_role("list").get_by_text("启用", exact=True).click()
    # page.locator("td").filter(has_text="启用不启用").locator("i").click()
    # page.get_by_role("list").get_by_text("启用", exact=True).click()



#启用
    #page.get_by_role("row", name="身份证号脱敏 请选择").locator("i").nth(1).click()
    #page.get_by_role("row", name="身份证号脱敏 请选择  请选择").locator("i").nth(1).click()
    page.get_by_role("row", name="身份证号脱敏").locator("i").nth(1).click()
    page.get_by_role("list").get_by_text("启用", exact=True).click()
#     time.sleep(3)
#指定
    page.get_by_role("cell", name="全局 ").locator("span").nth(1).click()
    page.get_by_role("radio", name="指定").click()
    page.get_by_label("修改策略生效范围").get_by_role("textbox").first.click()
    page.get_by_role("list").get_by_text("默认").click()
    page.get_by_label("修改策略生效范围").locator("i").nth(2).click()
    page.get_by_role("button", name="保 存").click()


    page.locator("td").filter(has_text="全模糊保留前3位及后4位，其余模糊").locator("i").click()
    page.get_by_text("保留前3位及后4位，其余模糊").click()
    # 启用
    page.get_by_role("row", name="手机号脱敏").locator("i").nth(1).click()
    page.get_by_role("list").get_by_text("启用", exact=True).click()
    # 指定
    page.get_by_role("cell", name="全局 ").locator("span").nth(1).click()
    page.get_by_role("radio", name="指定").click()
    page.get_by_label("修改策略生效范围").get_by_role("textbox").first.click()
    page.get_by_role("list").get_by_text("默认").click()
    page.get_by_label("修改策略生效范围").locator("i").nth(2).click()
    page.get_by_role("button", name="保 存").click()




    page.locator("td").filter(has_text="全模糊保留第一位，@及以后，其余模糊").locator("i").click()
    page.get_by_text("保留第一位，@及以后，其余模糊").click()
    # 启用
    page.get_by_role("row", name="邮箱脱敏").locator("i").nth(1).click()
    page.get_by_role("list").get_by_text("启用", exact=True).click()
    # 指定
    page.get_by_role("cell", name="全局 ").locator("span").nth(1).click()
    page.get_by_role("radio", name="指定").click()
    page.get_by_label("修改策略生效范围").get_by_role("textbox").first.click()
    page.get_by_role("list").get_by_text("默认").click()
    page.get_by_label("修改策略生效范围").locator("i").nth(2).click()
    page.get_by_role("button", name="保 存").click()





    page.get_by_role("button", name="保存").click()
    page.get_by_role("button", name="确 定").click()
