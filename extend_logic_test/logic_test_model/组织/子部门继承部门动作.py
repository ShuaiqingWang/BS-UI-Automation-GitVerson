import os
import time

from playwright.sync_api import Page

from extend_logic_test.logic_test_model.组织模块继承前置动作 import extend_organization_action
from test_scenario.用户组织设备合集.organization_utils import generate_random_org_name


def child_dep_extend_dep_action(page: Page, current_depname=None):
    if current_depname is None:
        current_depname = generate_random_org_name()

###
    time.sleep(2)
    # 获取当前脚本所在目录
    script_dir = os.path.dirname(os.path.abspath(__file__))
    # 构建主组织.txt文件路径
    txt_file_rel_path = os.path.join('..', '..', '..', 'data', 'extend_logic_data_collection', '组织', '子组织下部门.txt')
    txt_file_path = os.path.join(script_dir, txt_file_rel_path)

    # 读取文件内容并存储到变量中
    with open(txt_file_path, 'r', encoding='utf-8') as file:
        dep_name = file.read().strip()

    print("部门名称已成功读取:", dep_name)


###
    extend_organization_action(page)
    page.get_by_label("创建组织").get_by_placeholder("请选择").click()
    page.get_by_label("创建组织").get_by_placeholder("请选择").fill(dep_name)
    page.locator("li").filter(has_text=dep_name).locator("span").click()
    page.get_by_label("创建组织").get_by_placeholder("请输入组织名称").click()
    page.get_by_label("创建组织").get_by_placeholder("请输入组织名称").fill(current_depname)
    page.get_by_role("button", name="确 定").click()

###
    time.sleep(2)
    # 获取当前脚本所在目录
    script_dir = os.path.dirname(os.path.abspath(__file__))
    # 构建 txt 文件相对路径
    txt_file_rel_path = os.path.join('..', '..', '..', 'data', 'extend_logic_data_collection', '组织', '部门下子部门.txt')
    # 构建 txt 文件绝对路径
    txt_file_path = os.path.join(script_dir, txt_file_rel_path)

    # 写入文件
    with open(txt_file_path, 'w', encoding='utf-8') as file:
        file.write(current_depname)

    print("子部门已成功写入到文件:", txt_file_path)