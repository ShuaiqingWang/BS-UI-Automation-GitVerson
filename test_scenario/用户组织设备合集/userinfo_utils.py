#user_utils.py
import random
import string

def generate_random_user_name(prefix="测试用户"):
    # 生成4个随机字母
    random_letters = ''.join(random.choices(string.ascii_letters, k=4))
    # 生成4个随机数字
    random_digits = ''.join(random.choices(string.digits, k=4))
    # 合并字符串
    return f"{prefix}{random_letters}{random_digits}"

def generate_random_user_email(prefix="ceshi"):
    # 生成随机的5个字符
    random_letters = ''.join(random.choices(string.ascii_letters, k=5))
    # 生成随机的3个数字
    random_digits = ''.join(random.choices(string.digits, k=3))
    # 组合所有部分并添加邮件域
    return f"{prefix}{random_letters}{random_digits}@qq.com"

def generate_random_phone_number():
    # Generate 8 additional random digits
    random_digits = ''.join(random.choices('0123456789', k=8))
    # Combine with the prefix '138'
    return f"138{random_digits}"