import random
import string

def generate_random_application_name(prefix="测试应用"):
    # 生成4个随机字母
    random_letters = ''.join(random.choices(string.ascii_letters, k=4))
    # 生成4个随机数字
    random_digits = ''.join(random.choices(string.digits, k=4))
    # 合并字符串
    return f"{prefix}{random_letters}{random_digits}"


def generate_random_application_url(prefix="https://"):
    # 生成6个随机字母
    random_letters = ''.join(random.choices(string.ascii_letters, k=6))
    # 生成4个随机数字
    random_digits = ''.join(random.choices(string.digits, k=4))
    # 合并字符串
    return f"{prefix}{random_letters}{random_digits}.com"