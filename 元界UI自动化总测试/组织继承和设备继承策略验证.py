# main_testing_script.py
import os
import time
from 元界UI自动化总测试.判定逻辑.test_runner import run_tests
from 元界UI自动化总测试.判定逻辑.test_logger import log_result, send_report, save_results_to_file

##############################
# 放置场景
from extend_logic_test.logic_scenario.组织.组织继承场景 import run as 组织继承场景
from extend_logic_test.logic_scenario.设备.设备组继承场景 import run as 设备组继承场景


###############################


def main():
    script_name = os.path.basename(__file__)
    start_time = time.time()

    results = run_tests([
        #####放置场景
        (组织继承场景, "组织继承场景"),
        (设备组继承场景, "设备组继承场景")
        #############
    ])
    for name, result in results.items():
        log_result(name, result)

    send_report(script_name, results, start_time)

    # 本地log
    save_results_to_file(script_name, results, start_time)


if __name__ == "__main__":
    main()
