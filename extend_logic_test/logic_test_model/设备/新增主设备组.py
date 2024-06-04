import re
import os
import time

from playwright.sync_api import Page

from extend_logic_test.logic_test_model.组织模块继承前置动作 import extend_organization_action
from extend_logic_test.logic_test_model.设备模块继承前置动作 import extend_device_action
from test_scenario.用户组织设备合集.device_group_utils import generate_random_device_group_name
from test_scenario.用户组织设备合集.organization_utils import generate_random_org_name
from test_script.点击上边栏菜单动作模块.点击用户中心按钮动作 import click_user_center_action


def add_main_device_group(page: Page, main_device_group_name=None):
    if main_device_group_name is None:
        main_device_group_name = generate_random_device_group_name()

    time.sleep(2)
    extend_device_action(page)
#
    time.sleep(2)
    page.get_by_label("添加设备组").get_by_placeholder("请选择").click()
    page.get_by_role("radio").click()
    page.get_by_label("添加设备组").get_by_placeholder("请输入组织名称").click()
    page.get_by_label("添加设备组").get_by_placeholder("请输入组织名称").fill(main_device_group_name)
    page.get_by_role("button", name="确 定").click()

    time.sleep(2)
    # 文件存储部分
    # 获取当前脚本所在目录
    script_dir = os.path.dirname(os.path.abspath(__file__))
    # 构建 txt 文件相对路径
    txt_file_rel_path = os.path.join('..', '..', '..', 'data', 'extend_logic_data_collection', '设备', '主设备组.txt')
    # 构建 txt 文件绝对路径
    txt_file_path = os.path.join(script_dir, txt_file_rel_path)

    # 写入文件
    with open(txt_file_path, 'w', encoding='utf-8') as file:
        file.write(main_device_group_name)

    print("主设备组名称已成功写入到文件:", txt_file_path)
    time.sleep(2)
