import re
from playwright.sync_api import Playwright, sync_playwright, expect
from server_ports.服务器端口 import open_base_url
from test_script.登录 import login

import time

def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()


    open_base_url(page)

    # 登录
    login(page)

#策略
    page.get_by_role("menuitem", name="策略管理").click()
    page.get_by_role("button", name="编辑").click()
###################################################################################
    time.sleep(1)
    # 找到并点击下拉箭头，并确保点击后下拉菜单稳定显示
    page.wait_for_selector(".el-table__row:has-text('页面复制') .el-select__caret", state="visible")
    caret = page.query_selector(".el-table__row:has-text('页面复制') .el-select__caret")
    if caret:
        page.evaluate("element => element.click()", caret)
        time.sleep(1)  # 等待1秒确保下拉菜单稳定打开

    # 点击选项
    option = page.wait_for_selector(".el-select-dropdown__list li:text('不控制')", state="visible")
    if option:
        option.click()
        time.sleep(1)  # 等待1秒确保选项被成功选中

    # 重复对“页面打印”的处理
    caret_print = page.wait_for_selector(".el-table__row:has-text('页面打印') .el-select__caret", state="visible")
    if caret_print:
        page.evaluate("element => element.click()", caret_print)
        time.sleep(1)  # 等待下拉菜单打开
        option_audit = page.wait_for_selector(".el-select-dropdown__list li:text('审计')", state="visible")
        if option_audit:
            option_audit.click()
            time.sleep(1)  # 等待选项被成功选中

    # 保存和确认
    save_button = page.locator("button:has-text('保存')")
    if save_button.is_visible():
        save_button.click()
        time.sleep(1)  # 等待保存操作完成

    confirm_button = page.locator("button:has-text('确 定')")
    if confirm_button.is_visible():
        confirm_button.click()
        time.sleep(1)  # 确保确认对话框处理完成


    # page.get_by_role("button", name="保存").click()
    # page.get_by_role("button", name="确 定").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
