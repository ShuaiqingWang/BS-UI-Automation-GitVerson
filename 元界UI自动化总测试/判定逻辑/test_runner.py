# test_runner.py
def run_test(test, name, results):
    try:
        test()  # 直接调用测试函数，不需要 page 参数
        results[name] = "Passed"
    except Exception as e:
        results[name] = f"Failed - {str(e)}"
        print(f"Error in {name}: {str(e)}")  # 打印错误详情到控制台

def run_tests(tests):
    results = {}
    for test, name in tests:
        run_test(test, name, results)
    return results
