import re
import time

from playwright.sync_api import Playwright, sync_playwright, expect
from server_ports.服务器端口 import open_base_url, create_context_and_page
from test_script.登录 import login
from test_script.新增设备 import addDevice
from playwright.sync_api import sync_playwright

def run():
    with sync_playwright() as playwright:
        browser, context, page = create_context_and_page(playwright, headless=False)

        open_base_url(page)

    #登录
        login(page)

    #新增设备
        addDevice(page)


        # ---------------------
        context.close()
        browser.close()


if __name__ == "__main__":
    run()
