import re
import os
import time

from playwright.sync_api import Page
from test_scenario.用户组织设备合集.device_utils import generate_random_device_name
from test_scenario.用户组织设备合集.device_utils import generate_random_device_id

def addDevice(page: Page, device_name=None, device_id=None):
    if device_name is None:
        device_name = generate_random_device_name()  # 生成随机-设备名

    if device_id is None:
        device_id = generate_random_device_id()  # 生成随机-设备ID



    time.sleep(1)
    # 获取当前脚本所在目录的上一级目录
    base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    # 拼接得到data目录下的文件路径
    file_path = os.path.join(base_path, 'data', 'last_created_device_group.txt')
    with open(file_path, 'r', encoding='utf-8') as file:
        last_creat_device_group = file.read().strip()

    page.get_by_text("用户中心").first.click()
    page.get_by_role("menuitem", name="设备管理").click()
    page.get_by_role("button", name="新增 ").click()
    page.get_by_text("设备", exact=True).click()
    page.get_by_label("添加设备").locator("i").nth(1).click()


#####
    page.get_by_label("添加设备").get_by_placeholder("请选择").click()
    page.get_by_label("添加设备").get_by_placeholder("请选择").fill(last_creat_device_group)
    page.locator("li").filter(has_text=last_creat_device_group).locator("span").click()
    page.get_by_placeholder("请输入设备ID", exact=True).fill(device_id)
    page.get_by_placeholder("请输入设备名称").click()
    page.get_by_placeholder("请输入设备名称").fill(device_name)
    ###

    data_directory = os.path.join(os.path.dirname(os.getcwd()), 'data')
    file_path = os.path.join(data_directory, 'last_created_device.txt')
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(device_name)

##
    time.sleep(1)
    page.get_by_role("button", name="确 定").click()


