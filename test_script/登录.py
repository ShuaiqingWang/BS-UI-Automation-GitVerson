#登录功能
import re
import time

from playwright.sync_api import Page

def login(page: Page):
    username = "admin"  # 可以在这里设置默认的用户名
    password = "TWS#admin#1349"  # 设置默认的密码
    page.get_by_placeholder("账号").click()
    page.get_by_placeholder("账号").fill(username)
    page.get_by_placeholder("密码").click()
    page.get_by_placeholder("密码").press("CapsLock")
    page.get_by_placeholder("密码").fill(password)
    page.get_by_placeholder("密码").press("CapsLock")
    page.get_by_placeholder("密码").fill(password)
    time.sleep(0.5)
    page.get_by_role("button", name="登 录").click()
