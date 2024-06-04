import re
import time

from playwright.sync_api import Playwright, sync_playwright, expect
from server_ports.服务器端口 import open_base_url, create_context_and_page
from test_script.切换设备动作模块.切换设备组动作 import switch_device_action
from test_script.点击上边栏菜单动作模块.点击策略按钮动作 import click_strategy_action
from test_script.登录 import login
from test_script.组织策略_安全策略不控制_全局 import secure1
from playwright.sync_api import sync_playwright

def run():
    with sync_playwright() as playwright:
        browser, context, page = create_context_and_page(playwright, headless=False)

        open_base_url(page)

    #登录
        login(page)

        click_strategy_action(page)
        switch_device_action(page)
    #组织安全策略
        secure1(page)


        # ---------------------
        context.close()
        browser.close()


if __name__ == "__main__":
    run()
