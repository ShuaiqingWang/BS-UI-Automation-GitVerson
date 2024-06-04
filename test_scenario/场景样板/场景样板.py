import re
import time
from playwright.sync_api import sync_playwright

from server_ports.服务器端口 import create_context_and_page
from server_ports.服务器端口样例 import open_sample_base_url
from test_script.样板.样板 import example1
###############################################
from test_script.登录 import login  #login 场景


#def 后的run 可以改成任何你期望的名字
def run():
    with sync_playwright() as playwright:
        browser, context, page = create_context_and_page(playwright, headless=False)

    #打开网页
        open_sample_base_url(page)

    #登录
        login(page)

    #这里可以放置任何你想法放置的动作：
        example1(page)
    # -------结束-----------
        context.close()
        browser.close()

if __name__ == "__main__":
    run()
