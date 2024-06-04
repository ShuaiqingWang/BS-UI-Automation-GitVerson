import re
from playwright.sync_api import Playwright, sync_playwright, expect
from server_ports.服务器端口 import open_base_url, create_context_and_page
from test_script.切换设备动作模块.切换设备组动作 import switch_device_action
from test_script.点击上边栏菜单动作模块.点击策略按钮动作 import click_strategy_action
from test_script.登录 import login
from test_script.新增设备组 import addDeviceGroup
from test_script.新增设备 import addDevice
from test_script.脱敏策略_保留6位_不启用 import data_masking
from test_script.脱敏策略_保留6位_启用_指定 import data_masking_assign
from playwright.sync_api import sync_playwright

def run():
    with sync_playwright() as playwright:
        browser, context, page = create_context_and_page(playwright, headless=False)

        open_base_url(page)

    #登录
        login(page)

        click_strategy_action(page)
        switch_device_action(page)
        data_masking_assign(page)


        # ---------------------
        context.close()
        browser.close()


if __name__ == "__main__":
    run()
