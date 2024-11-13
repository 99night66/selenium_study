# test_login.py

from login import LoginAutomation

class LoginTest:
    def __init__(self):
        """初始化，创建 LoginAutomation 实例"""
        self.login_test = LoginAutomation()
        self.url = "http://20.30.1.198:8017/"
        self.account = "test"
        self.password = "z123456"

    def run_invalid_credentials_test(self):
        """错误的账号密码测试"""
        print("错误的账号密码测试：")
        self.login_test.login(account=self.account, password=self.password[1:])

    def run_missing_password_test(self):
        """输入账号不输入密码测试"""
        print("\n输入账号不输入密码：")
        self.login_test.login(account=self.account, password="")

    def run_missing_account_test(self):
        """输入密码不输入账号测试"""
        print("\n输入密码不输入账号：")
        self.login_test.login(account="", password=self.password)

    def run_valid_credentials_test(self):
        """正确的账号密码测试"""
        print("\n正确的账号密码测试：")
        self.login_test.login(account=self.account, password=self.password)

    def close_browser(self):
        """关闭浏览器"""
        self.login_test.close()

    def run_all_tests(self):
        """执行所有测试"""
        self.run_invalid_credentials_test()
        self.run_missing_password_test()
        self.run_missing_account_test()
        self.run_valid_credentials_test()
        self.close_browser()

if __name__ == "__main__":
    # 创建并运行测试
    login_tester = LoginTest()
    login_tester.run_all_tests()
