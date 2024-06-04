# main_testing_script.py
import os
import time
from 元界UI自动化总测试.判定逻辑.test_runner import run_tests
from 元界UI自动化总测试.判定逻辑.test_logger import log_result, send_report, save_results_to_file

##############################
#放置场景
from test_scenario.新增用户类型配置场景 import run as 新增用户类型配置场景
###############################


def main():
    script_name = os.path.basename(__file__)
    start_time = time.time()

    results = run_tests([

        #####放置场景
        (新增用户类型配置场景, "新增用户类型配置场景"),

       #############

    ])
    for name, result in results.items():
        log_result(name, result)

    #飞书机器人报告
    send_report(script_name, results, start_time)

    # 本地log
    save_results_to_file(script_name, results, start_time)


if __name__ == "__main__":
    main()
