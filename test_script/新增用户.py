import re
import os
from playwright.sync_api import Page
from test_scenario.用户组织设备合集.userinfo_utils import generate_random_user_name
from test_scenario.用户组织设备合集.userinfo_utils import generate_random_user_email
from test_scenario.用户组织设备合集.userinfo_utils import generate_random_phone_number

def addUser(page: Page, username=None, email=None, phoneNumber=None):
    if username is None:
        username = generate_random_user_name()  # 生成随机-用户名称
    if email is None:
        email = generate_random_user_email()    # 生成随机-邮箱
    if phoneNumber is None:
        phoneNumber = generate_random_phone_number()   # 生成随机-号码

    page.get_by_text("用户中心").first.click()
    page.get_by_role("menuitem", name="用户管理").click()
    page.get_by_role("button", name="创建 ").click()
    page.get_by_text("用户", exact=True).click()
    page.get_by_label("新增用户").get_by_placeholder("请选择", exact=True).click()

    # 获取当前脚本所在目录的上一级目录
    base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    # 拼接得到data目录下的文件路径
    file_path = os.path.join(base_path, 'data', 'last_organization_name.txt')
    with open(file_path, 'r', encoding='utf-8') as file:
        organization_name = file.read().strip()
    page.get_by_label("新增用户").get_by_placeholder("请选择", exact=True).fill(organization_name)
    page.locator("li").filter(has_text="测试组织").locator("span").click()

    #用户名
    page.get_by_placeholder("请输入用户名", exact=True).click()
    page.get_by_placeholder("请输入用户名", exact=True).fill(username)

    page.get_by_placeholder("请选择账号类型").click()
    page.locator("span").filter(has_text="终端用户").click()
    page.get_by_placeholder("请输入用户密码").click()
    page.get_by_placeholder("请输入用户密码").fill("ceshi@")
    page.get_by_placeholder("请输入用户密码").press("CapsLock")
    page.get_by_placeholder("请输入用户密码").fill("ceshi@QQ")
    page.get_by_placeholder("请输入用户密码").press("CapsLock")

    #手机号
    page.get_by_placeholder("请输入手机号").click()
    page.get_by_placeholder("请输入手机号").fill(phoneNumber)

    #邮箱
    page.get_by_placeholder("请输入电子邮箱").click()
    page.get_by_placeholder("请输入电子邮箱").fill(email)
    page.get_by_role("button", name="确 定").click()



    data_directory = os.path.join(os.path.dirname(os.getcwd()), 'data')
    file_path = os.path.join(data_directory, 'last_user_name.txt')

    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(username)