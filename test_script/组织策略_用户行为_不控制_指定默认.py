import re
import time
from playwright.sync_api import Page



def userAction2(page: Page):

#编辑
    time.sleep(3.5)
    page.get_by_role("button", name="编辑").click()
    #page.get_by_role("row", name="页面复制 请选择  全局 ").get_by_placeholder("请选择").click()
    page.get_by_role("row", name="页面复制 请选择").get_by_placeholder("请选择").click()
    page.get_by_role("list").get_by_text("不控制").click()
    # 指定
    time.sleep(0.5)
    page.locator(".el-icon-edit-outline").first.click()
    page.get_by_role("radio", name="指定").click()
    page.get_by_label("修改策略生效范围").get_by_role("textbox").first.click()
    page.get_by_role("list").get_by_text("默认").click()
    page.get_by_label("修改策略生效范围").locator("i").nth(2).click()
    page.get_by_role("button", name="保 存").click()

#页面打印
    time.sleep(0.5)
    page.get_by_role("row", name="页面打印 请选择").get_by_placeholder("请选择").click()
    page.get_by_role("list").get_by_text("不控制").click()
    #指定
    page.get_by_role("row", name="页面打印 请选择").locator("span").nth(3).click()
    page.get_by_role("radio", name="指定").click()
    page.get_by_label("修改策略生效范围").get_by_role("textbox").first.click()
    page.get_by_role("list").get_by_text("默认").click()
    page.get_by_label("修改策略生效范围").locator("i").nth(2).click()
    page.get_by_role("button", name="保 存").click()


#网页另存为
    time.sleep(0.5)
    page.get_by_role("row", name="网页另存为 请选择").get_by_placeholder("请选择").click()
    page.get_by_role("list").get_by_text("不控制").click()
    #指定
    page.get_by_role("row", name="网页另存为 请选择").locator("span").nth(3).click()
    page.get_by_role("radio", name="指定").click()
    page.get_by_label("修改策略生效范围").get_by_role("textbox").first.click()
    page.get_by_role("list").get_by_text("默认").click()
    page.get_by_label("修改策略生效范围").locator("i").nth(2).click()
    page.get_by_role("button", name="保 存").click()



#查看页面源代码
    time.sleep(0.5)
    page.get_by_role("row", name="查看页面源代码 请选择").get_by_placeholder("请选择").click()
    page.get_by_role("list").get_by_text("不控制").click()
    # 指定
    page.get_by_role("row", name="查看页面源代码 请选择").locator("span").nth(3).click()
    page.get_by_role("radio", name="指定").click()
    page.get_by_label("修改策略生效范围").get_by_role("textbox").first.click()
    page.get_by_role("list").get_by_text("默认").click()
    page.get_by_label("修改策略生效范围").locator("i").nth(2).click()
    page.get_by_role("button", name="保 存").click()

#文件上传
    time.sleep(0.5)
    page.get_by_role("row", name="文件上传 请选择").get_by_placeholder("请选择").click()
    page.get_by_role("list").get_by_text("不控制").click()
    # 指定
    page.get_by_role("row", name="文件上传 请选择").locator("span").nth(3).click()
    page.get_by_role("radio", name="指定").click()
    page.get_by_label("修改策略生效范围").get_by_role("textbox").first.click()
    page.get_by_role("list").get_by_text("默认").click()
    page.get_by_label("修改策略生效范围").locator("i").nth(2).click()
    page.get_by_role("button", name="保 存").click()



#文件下载
    time.sleep(0.5)
    page.get_by_role("row", name="文件下载 请选择").get_by_placeholder("请选择").click()
    page.get_by_role("list").get_by_text("不控制").click()
    # 指定
    page.get_by_role("row", name="文件下载 请选择").locator("span").nth(3).click()
    page.get_by_role("radio", name="指定").click()
    page.get_by_label("修改策略生效范围").get_by_role("textbox").first.click()
    page.get_by_role("list").get_by_text("默认").click()
    page.get_by_label("修改策略生效范围").locator("i").nth(2).click()
    page.get_by_role("button", name="保 存").click()


#页面截图
    time.sleep(0.5)
    page.get_by_role("row", name="页面截图 请选择").get_by_placeholder("请选择").click()
    page.get_by_role("list").get_by_text("不控制").click()
    # 指定
    page.get_by_role("row", name="页面截图 请选择").locator("span").nth(3).click()
    page.get_by_role("radio", name="指定").click()
    page.get_by_label("修改策略生效范围").get_by_role("textbox").first.click()
    page.get_by_role("list").get_by_text("默认").click()
    page.get_by_label("修改策略生效范围").locator("i").nth(2).click()
    page.get_by_role("button", name="保 存").click()


#开发者工具
    time.sleep(0.5)
    page.get_by_role("row", name="开发者工具 请选择").get_by_placeholder("请选择").click()
    page.get_by_role("list").get_by_text("不控制").click()
    # 指定
    page.get_by_role("row", name="开发者工具 请选择").locator("span").nth(3).click()
    page.get_by_role("radio", name="指定").click()
    page.get_by_label("修改策略生效范围").get_by_role("textbox").first.click()
    page.get_by_role("list").get_by_text("默认").click()
    page.get_by_label("修改策略生效范围").locator("i").nth(2).click()
    page.get_by_role("button", name="保 存").click()

    #保存
    page.get_by_role("button", name="保存").click()
    page.get_by_role("button", name="确 定").click()

