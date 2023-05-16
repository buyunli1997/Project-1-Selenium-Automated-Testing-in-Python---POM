# 定义登录页面对象
from selenium.webdriver.common.by import By

from base.mis.base import BasePage, BaseHandle


# 定义对象库层
from utils import UtilsDriver


class LoginPage(BasePage):
    def __init__(self):
        super().__init__()
        # 用户名输入框
        self.username = By.NAME, "username"
        # 密码输入框
        self.password = By.NAME, "password"
        # 登录按钮
        self.login_btn = By.ID, "inp1"

    # 定位用户名输入框
    def find_username(self):
        return self.get_element(self.username)

    # 定位密码输入框
    def find_password(self):
        return self.get_element(self.password)

    # 定位登录按钮
    def find_login_btn(self):
        return self.get_element(self.login_btn)


# 定义操作层
class LoginHandle(BaseHandle):
    def __init__(self):
        self.login_page = LoginPage()

    # 输入用户名
    def input_username(self, username):
        self.input_text(self.login_page.find_username(), username)

    # 输入密码
    def input_password(self, password):
        self.input_text(self.login_page.find_password(), password)

    # 点击登录
    def click_login_btn(self):
        # 定义JS
        js = "document.getElementById('inp1').removeAttribute('disabled')"
        # 通过execute_script方法执行JS
        self.login_page.driver.execute_script(js)
        # UtilsDriver.get_mis_driver().execute_script(js)
        # 点击登录按钮
        self.login_page.find_login_btn().click()


# 定义业务层
class LoginProxy:
    def __init__(self):
        self.login_handle = LoginHandle()

    # 登录业务操作
    def login(self, username, password):
        self.login_handle.input_username(username)  # 输入用户名
        self.login_handle.input_password(password)  # 输入密码
        self.login_handle.click_login_btn()         # 点击登录按钮
