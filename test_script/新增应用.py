import re
import os
import time

from playwright.sync_api import Page

from test_scenario.应用应用组合集.application_utils import generate_random_application_name
from test_scenario.应用应用组合集.application_utils import generate_random_application_url
from test_script.点击上边栏菜单动作模块.点击应用中心按钮动作 import click_application_center_action


def add_application(page: Page, application_name=None, application_url=None):
    if application_name is None:
        application_name = generate_random_application_name()
    if application_url is None:
        application_url = generate_random_application_url()


    page.get_by_role("menuitem", name="应用管理").click()

    time.sleep(1)

    page.get_by_role("button", name="创建").click()
    page.get_by_text("应用", exact=True).click()
    page.get_by_placeholder("请输入名称").click()
    page.get_by_placeholder("请输入名称").fill(application_name)
    page.locator(".preset-logos > img").first.click()
    page.get_by_placeholder("请输入 URL").click()
    page.get_by_placeholder("请输入 URL").fill(application_url)
    time.sleep(1)

    page.get_by_role("button", name="保存").click()

    time.sleep(1)

    data_directory = os.path.join(os.path.dirname(os.getcwd()), 'data')
    file_path = os.path.join(data_directory, 'last_created_application.txt')

    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(application_name)
