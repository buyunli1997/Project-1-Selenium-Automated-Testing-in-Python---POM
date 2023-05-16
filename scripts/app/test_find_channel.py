# define test class
import pytest

from page.app.index_page import IndexProxy
from utils import UtilsDriver


@pytest.mark.run(order=2000)
class TestFindChannel:
    # define fixture's setup (class level)
    def setup_class(self):
        self.indxe_proxy = IndexProxy()

    # define fixture's tear_down method
    def teardown_class(self):
        UtilsDriver.quit_app_driver()

    # define testing methods
    # def test_find_channel(self):
    #     self.indxe_proxy.find_channel("数据库")
