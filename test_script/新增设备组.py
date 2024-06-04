import re
import os
import time

from playwright.sync_api import Page
from test_scenario.用户组织设备合集.device_group_utils import generate_random_device_group_name


def addDeviceGroup(page: Page, device_group_name=None):

    if device_group_name is None:
        device_group_name = generate_random_device_group_name()  # 生成随机-设备组名

    page.get_by_text("用户中心").first.click()
    page.get_by_role("menu").get_by_text("用户中心").click()
    page.get_by_role("menuitem", name="设备管理").click()
    page.get_by_role("button", name="新增 ").click()
    #page.get_by_text("设备组").click()
    page.get_by_text("设备组", exact=True).click()
    page.get_by_label("添加设备组").get_by_placeholder("请选择").click()
    page.get_by_role("radio").click()
    page.get_by_label("添加设备组").get_by_placeholder("请输入组织名称").click()
    page.get_by_label("添加设备组").get_by_placeholder("请输入组织名称").fill(device_group_name)
    page.get_by_role("button", name="确 定").click()

    data_directory = os.path.join(os.path.dirname(os.getcwd()), 'data')
    file_path = os.path.join(data_directory, 'last_created_device_group.txt')

    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(device_group_name)

    time.sleep(2)