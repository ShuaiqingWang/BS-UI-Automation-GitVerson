# main_testing_script.py
import os
import time
from 元界UI自动化总测试.判定逻辑.test_runner import run_tests
from 元界UI自动化总测试.判定逻辑.test_logger import log_result, send_report, save_results_to_file

from test_scenario.新增用户类型配置场景 import run as 新增用户类型配置场景
from test_scenario.新增应用组场景 import run as 新增应用组场景
from test_scenario.新增应用场景 import run as 新增应用场景
from test_scenario.新增设备组场以及旗下设备景 import run as 新增设备组场以及旗下设备景
from test_scenario.新增组织以及旗下用户场景 import run as 新增组织以及旗下用户场景


#########
from test_scenario.组织架构.安全策略.组织安全策略场景_允许_全局 import run as 组织安全策略场景_允许_全局
from test_scenario.组织架构.安全策略.组织安全策略场景_不允许_全局 import run as 组织安全策略场景_不允许_全局
from test_scenario.组织架构.安全策略.组织安全策略场景_不控制_全局 import run as 组织安全策略场景_不控制_全局

from test_scenario.组织架构.客户端策略.组织客户端场景_全显示 import run as 组织客户端场景_全显示
from test_scenario.组织架构.客户端策略.组织客户端场景_不显示 import run as 组织客户端场景_不显示

from test_scenario.组织架构.水印策略.组织水印策略场景_允许明水印_指定 import run as 组织水印策略场景_允许明水印_指定
from test_scenario.组织架构.水印策略.组织水印策略场景_全禁止 import run as 组织水印策略场景_全禁止
from test_scenario.组织架构.水印策略.组织水印策略场景_允许明水印_自定义水印 import run as 组织水印策略场景_允许明水印_自定义水印
#全禁止

from test_scenario.组织架构.用户行为.组织用户行为策略_不控制_全局 import run as 组织用户行为策略_不控制_全局
from test_scenario.组织架构.用户行为.组织用户行为策略_不控制_指定默认 import run as 组织用户行为策略_不控制_指定默认
from test_scenario.组织架构.用户行为.组织用户行为策略_不控制_指定全局 import run as 组织用户行为策略_不控制_指定全局

from test_scenario.组织架构.脱敏策略.组织脱敏策略场景_保留6位_启用_指定 import run as 组织脱敏策略场景_保留6位_启用_指定
from test_scenario.组织架构.脱敏策略.组织脱敏策略场景_保留6位_不启用 import run as 组织脱敏策略场景_保留6位_不启用

from test_scenario.组织架构.访问策略.组织访问策略场景_全启用_指定 import run as 组织访问策略场景_全启用_指定
from test_scenario.组织架构.访问策略.组织访问策略场景_全启用_全局 import run as 组织访问策略场景_全启用_全局
from test_scenario.组织架构.访问策略.组织访问策略场景_全不启用 import run as 组织访问策略场景_全不启用
##########################################################################################################
from test_scenario.设备组.安全策略.设备安全策略场景_允许_全局 import run as 设备安全策略场景_允许_全局
from test_scenario.设备组.安全策略.设备安全策略场景_不允许_全局 import run as 设备安全策略场景_不允许_全局
from test_scenario.设备组.安全策略.设备安全策略场景_不控制_全局 import run as 设备安全策略场景_不控制_全局

from test_scenario.设备组.客户端策略.设备客户端场景_全显示 import run as 设备客户端场景_全显示
from test_scenario.设备组.客户端策略.设备客户端场景_不显示 import run as 设备客户端场景_不显示

from test_scenario.设备组.水印策略.设备水印策略场景_允许明水印_指定 import run as 设备水印策略场景_允许明水印_指定
from test_scenario.设备组.水印策略.设备水印策略场景_全禁止 import run as 设备水印策略场景_全禁止
from test_scenario.设备组.水印策略.设备水印策略场景_允许明水印_自定义水印 import run as 设备水印策略场景_允许明水印_自定义水印
#全禁止

from test_scenario.设备组.用户行为.设备用户行为策略_不控制_全局 import run as 设备用户行为策略_不控制_全局
from test_scenario.设备组.用户行为.设备用户行为策略_不控制_指定默认 import run as 设备用户行为策略_不控制_指定默认
from test_scenario.设备组.用户行为.设备用户行为策略_不控制_指定全局 import run as 设备用户行为策略_不控制_指定全局

from test_scenario.设备组.脱敏策略.设备脱敏策略场景_保留6位_启用_指定 import run as 设备脱敏策略场景_保留6位_启用_指定
from test_scenario.设备组.脱敏策略.设备脱敏策略场景_保留6位_不启用 import run as 设备脱敏策略场景_保留6位_不启用

from test_scenario.设备组.访问策略.设备访问策略场景_全启用_指定 import run as 设备访问策略场景_全启用_指定
from test_scenario.设备组.访问策略.设备访问策略场景_全启用_全局 import run as 设备访问策略场景_全启用_全局
from test_scenario.设备组.访问策略.设备访问策略场景_全不启用 import run as 设备访问策略场景_全不启用



#######


def main():
    script_name = os.path.basename(__file__)
    start_time = time.time()

    results = run_tests([
        #新增
        (新增应用场景, "新增应用场景"),
        (新增应用组场景, "新增应用组场景"),
        (新增组织以及旗下用户场景, "新增组织以及旗下用户场景"),
        (新增设备组场以及旗下设备景, "新增设备组场以及旗下设备景"),
        (新增用户类型配置场景, "新增用户类型配置场景"),
        #--

        # 组织
        (组织用户行为策略_不控制_指定全局, "组织用户行为策略_不控制_指定全局"),
        (组织用户行为策略_不控制_全局, "组织用户行为策略_不控制_全局"),
        (组织用户行为策略_不控制_指定默认, "组织用户行为策略_不控制_指定默认"),
        (组织用户行为策略_不控制_指定全局, "组织用户行为策略_不控制_指定全局"),

        (组织访问策略场景_全不启用, "组织访问策略场景_全不启用"),
        (组织访问策略场景_全启用_全局, "组织访问策略场景_全启用_全局"),
        (组织访问策略场景_全启用_指定, "组织访问策略场景_全启用_指定"),
        (组织访问策略场景_全不启用, "组织访问策略场景_全不启用"),

        (组织安全策略场景_允许_全局, "组织安全策略场景_允许_全局"),
        (组织安全策略场景_不允许_全局, "组织安全策略场景_不允许_全局"),


        (组织脱敏策略场景_保留6位_不启用, "组织脱敏策略场景_保留6位_不启用"),
        (组织脱敏策略场景_保留6位_启用_指定, "组织脱敏策略场景_保留6位_启用_指定"),
        (组织脱敏策略场景_保留6位_不启用, "组织脱敏策略场景_保留6位_不启用"),

        (组织水印策略场景_全禁止, "组织水印策略场景_全禁止"),
        (组织水印策略场景_允许明水印_指定, "组织水印策略场景_允许明水印_指定"),
        (组织水印策略场景_允许明水印_自定义水印, "组织水印策略场景_允许明水印_自定义水印"),
        (组织水印策略场景_全禁止, "组织水印策略场景_全禁止"),


        (组织客户端场景_全显示, "组织客户端场景_全显示"),
        (组织客户端场景_不显示, "组织客户端场景_不显示"),
        # -------------------------------------------------------------------------

        # 设备
        (设备用户行为策略_不控制_指定全局, "设备用户行为策略_不控制_指定全局"),
        (设备用户行为策略_不控制_全局, "设备用户行为策略_不控制_全局"),
        (设备用户行为策略_不控制_指定默认, "设备用户行为策略_不控制_指定默认"),
        (设备用户行为策略_不控制_指定全局, "设备用户行为策略_不控制_指定全局"),

        (设备访问策略场景_全不启用, "设备访问策略场景_全不启用"),
        (设备访问策略场景_全启用_全局, "设备访问策略场景_全启用_全局"),
        (设备访问策略场景_全启用_指定, "设备访问策略场景_全启用_指定"),
        (设备访问策略场景_全不启用, "设备访问策略场景_全不启用"),

        (设备安全策略场景_允许_全局, "设备安全策略场景_允许_全局"),
        (设备安全策略场景_不允许_全局, "设备安全策略场景_不允许_全局"),

        (设备脱敏策略场景_保留6位_不启用, "设备脱敏策略场景_保留6位_不启用"),
        (设备脱敏策略场景_保留6位_启用_指定, "设备脱敏策略场景_保留6位_启用_指定"),
        (设备脱敏策略场景_保留6位_不启用, "设备脱敏策略场景_保留6位_不启用"),

        (设备水印策略场景_全禁止, "设备水印策略场景_全禁止"),
        (设备水印策略场景_允许明水印_指定, "设备水印策略场景_允许明水印_指定"),
        (设备水印策略场景_允许明水印_自定义水印, "设备水印策略场景_允许明水印_自定义水印"),
        (设备水印策略场景_全禁止, "设备水印策略场景_全禁止"),

        (设备客户端场景_全显示, "设备客户端场景_全显示"),
        (设备客户端场景_不显示, "设备客户端场景_不显示")

    ])
    for name, result in results.items():
        log_result(name, result)

    # 发送飞书
    send_report(script_name, results, start_time)

    # 本地log
    save_results_to_file(script_name, results, start_time)


if __name__ == "__main__":
    main()
