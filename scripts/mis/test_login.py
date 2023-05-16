# define testing class
import pytest

from page.mis.home_page import HomeProxy
from page.mis.login_page import LoginProxy
from utils import UtilsDriver


@pytest.mark.run(order=1001)
class TestLogin:
    # define fixture's setup method(class level)
    def setup_class(self):
        self.login_proxy = LoginProxy()
        self.home_proxy = HomeProxy()

    # define fixture's teardown method (class level）
    def teardown_class(self):
        UtilsDriver.quit_mis_driver()

    # define testing methods
    def test_login(self):
        """
        testing data： username：testid   password:testpwd123
        :return:
        """
        self.login_proxy.login("testid", "testpwd123")
        result = self.home_proxy.get_user()
        assert "管理员" in result
