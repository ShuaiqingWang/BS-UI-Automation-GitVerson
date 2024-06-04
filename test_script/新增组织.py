import re
import os
from playwright.sync_api import Page
from test_scenario.用户组织设备合集.organization_utils import generate_random_org_name


def add_organization(page: Page, orgname=None):
    if orgname is None:
        orgname = generate_random_org_name()  # 生成随机-组织名称

    page.get_by_text("用户中心").first.click()
    page.get_by_role("menuitem", name="用户管理").click()
    page.get_by_role("button", name="创建 ").click()
    page.get_by_text("组织", exact=True).click()
    page.get_by_label("创建组织").get_by_placeholder("请选择").click()
    page.get_by_role("radio").click()
    page.get_by_label("创建组织").get_by_placeholder("请输入组织名称").fill(orgname)
    page.get_by_role("button", name="确 定").click()

    # with open('data/last_organization_name.txt', 'w', encoding='utf-8') as file:
    #     file.write(name)
    data_directory = os.path.join(os.path.dirname(os.getcwd()), 'data')
    file_path = os.path.join(data_directory, 'last_organization_name.txt')

    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(orgname)
