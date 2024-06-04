import random
import string

def generate_random_device_name(prefix="测试设备"):
    # 生成4个随机字母
    random_letters = ''.join(random.choices(string.ascii_letters, k=4))
    # 生成4个随机数字
    random_digits = ''.join(random.choices(string.digits, k=4))
    # 合并字符串
    return f"{prefix}{random_letters}{random_digits}"


def generate_random_device_id(prefix="TEST_DESKTOP_"):
    # 生成4个随机字母
    random_letters = ''.join(random.choices(string.ascii_letters, k=3))
    # 生成4个随机数字
    random_digits = ''.join(random.choices(string.digits, k=3))
    # 合并字符串
    return f"{prefix}{random_letters}{random_digits}"