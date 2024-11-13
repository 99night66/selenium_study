from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC

class LoginAutomation:
    def __init__(self, driver=None):
        """初始化，设置 WebDriver"""
        self.driver = driver or webdriver.Edge()

    def wait_for_element(self, by, value, timeout=60):
        """等待元素加载并返回元素"""
        try:
            return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((by, value)))
        except TimeoutException:
            print(f"元素 {value} 未加载成功")
            return None

    def fill_input_field(self, element, value):
        """填充输入框"""
        if element:
            element.clear()
            element.send_keys(value)

    def click_button(self, xpath):
        """点击按钮"""
        try:
            button = WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, xpath)))
            button.click()
        except TimeoutException:
            print(f"按钮 {xpath} 未加载成功")
            return False
        return True

    def handle_alert(self, timeout=5):
        """处理弹窗"""
        try:
            alert = WebDriverWait(self.driver, timeout).until(EC.alert_is_present())
            alert_text = alert.text
            print(f"弹窗提示: {alert_text}")
            alert.accept()
        except TimeoutException:
            print("登录界面测试成功：没有弹窗")

    def login(self, url="http://20.30.1.198:8017/", account="test", password="123456"):
        """执行登录测试"""
        try:
            # 访问首页
            self.driver.get(url)

            # 查找并填充账号输入框
            search_box = self.wait_for_element(By.ID, "account")
            self.fill_input_field(search_box, account)

            # 查找并填充密码输入框
            password_box = self.wait_for_element(By.ID, "password")
            self.fill_input_field(password_box, password)

            # 点击登录按钮
            if not self.click_button("//button[@type='submit']"):
                return

            # 处理登录后的弹窗
            self.handle_alert()

        except Exception as e:
            print(f"发生错误: {e}")

    def close(self):
        """关闭 WebDriver"""
        self.driver.quit()
