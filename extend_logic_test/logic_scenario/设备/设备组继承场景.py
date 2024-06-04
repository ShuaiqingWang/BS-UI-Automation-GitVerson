
import re
from playwright.sync_api import Playwright, sync_playwright, expect

from extend_logic_test.logic_test_model.组织.子部门继承部门动作 import child_dep_extend_dep_action
from extend_logic_test.logic_test_model.组织.新增主组织 import add_main_organization
from extend_logic_test.logic_test_model.组织.子组织继承主组织动作 import add_extend_organization_action
from extend_logic_test.logic_test_model.组织.部门继承子组织动作 import department_extend_organization_action
from extend_logic_test.logic_test_model.设备.新增主设备组 import add_main_device_group
from extend_logic_test.logic_test_model.设备.新增设备组1动作 import extend_device_group1
from extend_logic_test.logic_test_model.设备.新增设备组2动作 import extend_device_group2
from extend_logic_test.logic_test_model.设备.新增设备组3动作 import extend_device_group3
from server_ports.服务器端口 import open_base_url, create_context_and_page
from test_script.登录 import login
from test_script.新增组织 import add_organization
from test_script.新增用户 import addUser
from playwright.sync_api import sync_playwright

def run():
    with sync_playwright() as playwright:
        browser, context, page = create_context_and_page(playwright, headless=False)

        open_base_url(page)

    #登录
        login(page)

    #新增设备组
        add_main_device_group(page)

    #设备组1
        extend_device_group1(page)

    # 设备组2
        extend_device_group2(page)


    # 设备组3
        extend_device_group3(page)

        # ---------------------
        context.close()
        browser.close()


if __name__ == "__main__":
    run()