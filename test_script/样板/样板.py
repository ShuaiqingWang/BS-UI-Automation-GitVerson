import re
import time
from playwright.sync_api import Page


#example 改成任何你想叫的名字
def example1(page: Page):


    page.get_by_placeholder("账号").click()
    page.get_by_placeholder("账号").fill("admin")
    page.get_by_placeholder("密码").click()
    page.get_by_placeholder("密码").fill("")
    page.get_by_placeholder("密码").press("CapsLock")
    page.get_by_placeholder("密码").fill("DSWS")
    page.get_by_placeholder("密码").press("CapsLock")
    page.get_by_placeholder("密码").fill("DSWS#admin#1349")
    page.get_by_role("button", name="登 录").click()