import requests

def send_summary_to_feishu(script_name, passed_count, failed_count, total_tests, elapsed_time, testing_endpoint):
    script_name = script_name.replace('.py', '')
    total_tests_color = "blue"
    pass_rate_color = "green" if passed_count == total_tests else "yellow"
    passed_color = "green"
    failed_color = "red" if failed_count > 0 else "green"
    success_message = "本次UI自动化测试场景全部通过。请测试同学查看" if passed_count == total_tests else ""
    failure_message = "@测试同学，请查看后台报错以及本地报告，鉴定当前问题为前端BUG或UI自动化脚本自身问题" if failed_count > 0 else ""
    action_module_count = total_tests * 4  # 每个场景调用约4个动作模块

#大群
    webhook_url = "https://open.feishu.cn/open-apis/bot/v2/hook/1d4d5bb5-945c-4746-8f5f-8ad54f57d7c7"

#南京
    # webhook_url = "https://open.feishu.cn/open-apis/bot/v2/hook/0f64ad2c-f22e-428f-b621-6dde83ebe84f"

    card_content = {
        "config": {"wide_screen_mode": True, "enable_forward": True},
        "header": {"title": {"tag": "plain_text", "content": f"测试报告 - {script_name}"}},
        "elements": [{
            "tag": "div",
            "text": {
                "tag": "lark_md",
                "content": (
                    f"**测试完成——总用时:** {elapsed_time:.2f}秒\n"
                    f"**测试端口:** {testing_endpoint}\n"
                    f"**总场景数:** <font color='{total_tests_color}'>{total_tests}</font>\n"
                    f"**约调用动作模块数:** {action_module_count}\n"
                    f"**通过率:** <font color='{pass_rate_color}'>{passed_count / total_tests * 100:.2f}%</font>\n"
                    f"**成功:** <font color='{passed_color}'>{passed_count}</font> 个场景\n"
                    f"**失败:** <font color='{failed_color}'>{failed_count}</font> 个场景\n"
                    f"{success_message}\n"
                    f"{failure_message}"
                )
            }
        }]
    }

    data = {"msg_type": "interactive", "card": card_content}
    response = requests.post(webhook_url, json=data)
    print("Message sent to Feishu: ", response.text)
