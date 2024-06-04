import re
import os
import time

from playwright.sync_api import Page

from extend_logic_test.logic_test_model.组织模块继承前置动作 import extend_organization_action
from extend_logic_test.logic_test_model.设备模块继承前置动作 import extend_device_action
from test_scenario.用户组织设备合集.device_group_utils import generate_random_device_group_name
from test_scenario.用户组织设备合集.organization_utils import generate_random_org_name
from test_script.点击上边栏菜单动作模块.点击用户中心按钮动作 import click_user_center_action


def extend_device_group3(page: Page, device_group3_name=None):
    if device_group3_name is None:
        device_group3_name = generate_random_device_group_name()

    ###
    time.sleep(2)
    # 获取当前脚本所在目录
    script_dir = os.path.dirname(os.path.abspath(__file__))
    # 构建主组织.txt文件路径
    txt_file_rel_path = os.path.join('..', '..', '..', 'data', 'extend_logic_data_collection', '设备', '设备组2.txt')
    txt_file_path = os.path.join(script_dir, txt_file_rel_path)

    # 读取文件内容并存储到变量中
    with open(txt_file_path, 'r', encoding='utf-8') as file:
        device_group2_name = file.read().strip()

    print("设备组2名称已成功读取:", device_group2_name)

    ###
    extend_device_action(page)
    page.get_by_label("添加设备组").get_by_placeholder("请选择").click()
    page.get_by_label("添加设备组").get_by_placeholder("请选择").fill(device_group2_name)
    page.get_by_text(device_group2_name).click()
    page.get_by_label("添加设备组").get_by_placeholder("请输入组织名称").click()
    page.get_by_label("添加设备组").get_by_placeholder("请输入组织名称").fill(device_group3_name)
    page.get_by_role("button", name="确 定").click()

    time.sleep(2)
    # 文件存储部分
    # 获取当前脚本所在目录
    script_dir = os.path.dirname(os.path.abspath(__file__))
    # 构建 txt 文件相对路径
    txt_file_rel_path = os.path.join('..', '..', '..', 'data', 'extend_logic_data_collection', '设备', '设备组3.txt')
    # 构建 txt 文件绝对路径
    txt_file_path = os.path.join(script_dir, txt_file_rel_path)

    # 写入文件
    with open(txt_file_path, 'w', encoding='utf-8') as file:
        file.write(device_group3_name)

    print("设备组3名称已成功写入到文件:", txt_file_path)
