#feishu_report_message.py
import requests

def send_summary_to_feishu(script_name, passed_count, failed_count, total_tests, elapsed_time):
    # Remove '.py' from script_name
    script_name = script_name.replace('.py', '')

    # Determine color for total_tests
    total_tests_color = "blue"


    # Determine color for pass rate
    pass_rate_color = "green" if passed_count == total_tests else "yellow"

    # Determine color for passed and failed tests
    passed_color = "green"
    failed_color = "red" if failed_count > 0 else "green"


    #南京内部
    webhook_url = "https://open.feishu.cn/open-apis/bot/v2/hook/0f64ad2c-f22e-428f-b621-6dde83ebe84f"

    #大群
    #webhook_url = ""


    card_content = {
        "config": {
            "wide_screen_mode": True,
            "enable_forward": True
        },
        "header": {
            "title": {
                "tag": "plain_text",
                "content": f"测试报告 - {script_name}"
            }
        },
        "elements": [
            {
                "tag": "div",
                "text": {
                    "tag": "lark_md",
                    "content": f"**测试完成，总用时:** {elapsed_time:.2f}秒\n**总场景数:** <font color='{total_tests_color}'>{total_tests}</font>\n**通过率:** <font color='{pass_rate_color}'>{passed_count / total_tests * 100:.2f}%</font>\n**成功:** <font color='{passed_color}'>{passed_count}</font> 个场景\n**失败:** <font color='{failed_color}'>{failed_count}</font> 个场景"
                }
            }
        ]
    }
    data = {
        "msg_type": "interactive",
        "card": card_content
    }
    response = requests.post(webhook_url, json=data)
    print("Message sent to Feishu: ", response.text)
