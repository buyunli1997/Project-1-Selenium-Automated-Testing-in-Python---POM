# define testing class
import logging

import allure
import pytest
from config import BaseDir
from page.mp.home_page import HomeProxy
from page.mp.login_page import LoginProxy
from page.mp.publish_page import PublishProxy
from utils import UtilsDriver, is_exist, get_case_data

case_data = get_case_data(BaseDir + "/data/mp/test_login_data.json")


@pytest.mark.run(order=1)
class TestPublishArticle:
    # define fixture's setup method(class level)
    def setup_class(self):
        self.login_proxy = LoginProxy()
        self.home_proxy = HomeProxy()
        self.publish_proxy = PublishProxy()

    # define fixture's teardown method (class level）
    def teardown_class(self):
        UtilsDriver.quit_mp_driver()

    # login test case
    @pytest.mark.parametrize("username, code, expect", case_data)
    @allure.severity(allure.severity_level.CRITICAL)
    def test_login(self, username, code, expect):
        logging.info("用例的数据如下：用户名：{}， 验证码：{}， 预期结果：{}".format(username,
                                                              code, expect))
        print(username, code)
        self.login_proxy.login(username, code)   # to login
        allure.attach(UtilsDriver.get_mp_driver().get_screenshot_as_png(), "登录截图", allure.attachment_type.PNG)
        username = self.home_proxy.get_username_msg()  # to get username after login
        assert expect == username   # assert username is correct

    # define testing methods
    @allure.severity(allure.severity_level.CRITICAL)
    def test_publish_article(self):
        self.home_proxy.go_publish_page()   # to make the window go to the publishing page
        self.publish_proxy.publish_article("发布文章_0828_15", "发布文章_0710_14发布文章_0710_14", "数据库")
        assert is_exist(UtilsDriver.get_mp_driver(), "新增文章成功")
