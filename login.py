from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC

def wait_for_element(driver, by, value, timeout=60):
    """等待元素加载并返回元素"""
    try:
        return WebDriverWait(driver, timeout).until(EC.presence_of_element_located((by, value)))
    except TimeoutException:
        print(f"元素 {value} 未加载成功")
        return None

def fill_input_field(element, value):
    """填充输入框"""
    if element:
        element.clear()
        element.send_keys(value)

def click_button(driver, xpath):
    """点击按钮"""
    try:
        button = WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, xpath)))
        button.click()
    except TimeoutException:
        print(f"按钮 {xpath} 未加载成功")
        return False
    return True

def handle_alert(driver, timeout=5):
    """处理弹窗"""
    try:
        alert = WebDriverWait(driver, timeout).until(EC.alert_is_present())
        alert_text = alert.text
        print(f"弹窗提示: {alert_text}")
        alert.accept()
    except TimeoutException:
        print("登录界面测试成功：没有弹窗")

def login(account="test", password="123456"):
    """账号密码测试"""
    # 初始化 WebDriver
    driver = webdriver.Edge()

    try:
        # 访问首页
        driver.get("http://20.30.1.198:8017/")

        # 查找并填充账号输入框
        search_box = wait_for_element(driver, By.ID, "account")
        fill_input_field(search_box, account)

        # 查找并填充密码输入框
        password_box = wait_for_element(driver, By.ID, "password")
        fill_input_field(password_box, password)

        # 点击登录按钮
        if not click_button(driver, "//button[@type='submit']"):
            return

        # 处理登录后的弹窗
        handle_alert(driver)

    except Exception as e:
        print(f"发生错误: {e}")
    
    finally:
        driver.quit()

# 错误的账号密码测试
print("错误的账号密码测试：")
login(account="test", password="123456")

# 输入账号不输入密码
print("\n输入账号不输入密码：")
login(account="test", password="")

# 输入密码不输入账号
print("\n输入密码不输入账号：")
login(account="", password="z123456")

# 正确的账号密码测试
print("\n正确的账号密码测试：")
login(account="test", password="z123456")
