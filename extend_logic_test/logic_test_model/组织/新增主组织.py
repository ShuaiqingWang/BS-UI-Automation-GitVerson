import re
import os
import time

from playwright.sync_api import Page

from extend_logic_test.logic_test_model.组织模块继承前置动作 import extend_organization_action
from test_scenario.用户组织设备合集.organization_utils import generate_random_org_name
from test_script.点击上边栏菜单动作模块.点击用户中心按钮动作 import click_user_center_action


def add_main_organization(page: Page, main_org_name=None):
    if main_org_name is None:
        main_org_name = generate_random_org_name()  # 生成随机-主组织名称

    extend_organization_action(page)
    page.get_by_label("创建组织").get_by_placeholder("请选择").click()
    page.get_by_role("radio").click()
    page.get_by_label("创建组织").get_by_placeholder("请输入组织名称").fill(main_org_name)
    page.get_by_role("button", name="确 定").click()

    time.sleep(2)
    # 文件存储部分
    # 获取当前脚本所在目录
    script_dir = os.path.dirname(os.path.abspath(__file__))
    # 构建 txt 文件相对路径
    txt_file_rel_path = os.path.join('..', '..', '..', 'data', 'extend_logic_data_collection', '组织', '主组织.txt')
    # 构建 txt 文件绝对路径
    txt_file_path = os.path.join(script_dir, txt_file_rel_path)

    # 写入文件
    with open(txt_file_path, 'w', encoding='utf-8') as file:
        file.write(main_org_name)

    print("主组织名称已成功写入到文件:", txt_file_path)
