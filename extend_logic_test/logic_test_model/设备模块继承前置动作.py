import re
import os
import time

from playwright.sync_api import Page
from test_scenario.用户组织设备合集.organization_utils import generate_random_org_name
from test_script.点击上边栏菜单动作模块.点击用户中心按钮动作 import click_user_center_action
from test_script.点击上边栏菜单动作模块.点击首页按钮动作 import click_main_page_action


def extend_device_action(page: Page):
    click_main_page_action(page)
    click_user_center_action(page)

    time.sleep(2)
    page.get_by_role("menuitem", name="设备管理").click()
    page.get_by_role("button", name="新增").click()
    page.get_by_text("设备组", exact=True).click()