# 定义首页面对象
# 定义对象库层
import time

from selenium.webdriver.common.by import By

from base.mis.base import BasePage, BaseHandle


class HomePage(BasePage):
    def __init__(self):
        super().__init__()
        # 用户信息
        self.user_info = By.CSS_SELECTOR, ".user_info span"
        # 信息管理
        self.content_manage = By.XPATH, "//*[@class='side_bar']/ul/li[3]/a"
        # 内容审核
        self.content_audit = By.XPATH, "//*[@class='current3']/li[3]/a"

    # 定位用户信息
    def find_user_info(self):
        return self.get_element(self.user_info)

    # 定位信息管理菜单
    def find_content_manage(self):
        return self.get_element(self.content_manage)

    # 定位内容审核菜单
    def find_content_audit(self):
        return self.get_element(self.content_audit)


# 定义操作层
class HomeHandle(BaseHandle):
    def __init__(self):
        self.home_page = HomePage()

    # 获取用户信息
    def get_user_info(self):
        return self.home_page.find_user_info().text

    # 点击信息管理
    def click_content_manage(self):
        self.home_page.find_content_manage().click()

    # 点击内容审核
    def click_content_audit(self):
        self.home_page.find_content_audit().click()


# 定义业务层
class HomeProxy:
    def __init__(self):
        self.home_handle = HomeHandle()

    # 获取用户的信息
    def get_user(self):
        return self.home_handle.get_user_info()

    # 跳转到内容审核页面
    def go_content_audit(self):
        self.home_handle.click_content_manage()  # 点击信息管理
        time.sleep(1)
        self.home_handle.click_content_audit()   # 点击内容审核
