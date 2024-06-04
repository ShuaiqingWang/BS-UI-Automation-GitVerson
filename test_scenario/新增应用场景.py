import re
import time

from playwright.sync_api import Playwright, sync_playwright, expect
from server_ports.服务器端口 import open_base_url, create_context_and_page
from test_script.切换设备动作模块.切换设备组动作 import switch_device_action
from test_script.新增应用 import add_application
from test_script.新增用户类型 import userType
from test_script.点击上边栏菜单动作模块.点击应用中心按钮动作 import click_application_center_action
from test_script.点击上边栏菜单动作模块.点击策略按钮动作 import click_strategy_action
from test_script.登录 import login
from test_script.组织策略_安全策略不控制_全局 import secure1
from test_script.组织策略_安全策略允许_全局 import secure2
from playwright.sync_api import sync_playwright

def run():
    with sync_playwright() as playwright:
        browser, context, page = create_context_and_page(playwright, headless=False)

        open_base_url(page)

    #登录
        login(page)

        click_application_center_action(page)

        add_application(page)


        # ---------------------
        context.close()
        browser.close()


if __name__ == "__main__":
    run()
