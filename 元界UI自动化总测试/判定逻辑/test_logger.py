# test_logger.py
import os
import time
from datetime import datetime
from 元界UI自动化总测试.飞书报告格式.feishu_report_message import send_summary_to_feishu

# URL from 服务器端口.py
from server_ports.服务器端口 import get_testing_endpoint

def log_result(name, result):
    print(f"{name}: {result}")

def send_report(script_name, results, start_time):
    passed_count = list(results.values()).count("Passed")
    failed_count = len(results) - passed_count
    elapsed_time = time.time() - start_time
    testing_endpoint = get_testing_endpoint()
    #发给飞书
    send_summary_to_feishu(script_name, passed_count, failed_count, len(results), elapsed_time, testing_endpoint)

def save_results_to_file(script_name, results, elapsed_time):
    current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"{current_time}_{script_name.replace('.py', '')}.txt"
    dir_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    report_path = os.path.join(dir_path, 'report', filename)

    with open(report_path, 'w', encoding='utf-8') as file:
        file.write(f"测试报告 - {script_name.replace('.py', '')}\n")
        file.write(f"测试完成，总用时: {elapsed_time:.2f}秒\n")
        for name, result in results.items():
            file.write(f"{name}: {result}\n")