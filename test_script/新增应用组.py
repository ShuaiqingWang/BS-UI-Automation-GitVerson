import re
import os
import time

from playwright.sync_api import Page

from test_scenario.应用应用组合集.application_group_utils import generate_random_application_group_name
from test_scenario.用户组织设备合集.organization_utils import generate_random_org_name
from test_script.点击上边栏菜单动作模块.点击应用中心按钮动作 import click_application_center_action


def add_application_group(page: Page, application_gropu_name=None):
    if application_gropu_name is None:
        application_gropu_name = generate_random_application_group_name()  # 生成随机-应用组名称


    #
    # 获取当前脚本所在目录的上一级目录
    base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    # 拼接得到data目录下的文件路径
    file_path = os.path.join(base_path, 'data', 'last_created_application.txt')
    with open(file_path, 'r', encoding='utf-8') as file:
        last_created_application = file.read().strip()


#
    page.get_by_role("menuitem", name="应用管理").click()

    page.get_by_role("button", name="创建 ").click()
    page.get_by_text("应用组", exact=True).click()
    page.get_by_placeholder("请输入应用组名称").click()
    page.get_by_placeholder("请输入应用组名称").fill(application_gropu_name)


    page.get_by_placeholder("请输入搜索内容").first.click()
    page.get_by_placeholder("请输入搜索内容").first.fill(last_created_application)

    time.sleep(1)
    page.get_by_role("group", name="checkbox-group").locator("span").nth(1).click()


    time.sleep(1)
    page.get_by_role("button", name="").click()
    page.get_by_role("button", name="保存").click()
    time.sleep(1)




    data_directory = os.path.join(os.path.dirname(os.getcwd()), 'data')
    file_path = os.path.join(data_directory, 'last_created_application_group.txt')

    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(application_gropu_name)
