# define testing class
import time

import pytest

from page.mis.audit_page import AuditProxy
from page.mis.home_page import HomeProxy
from utils import UtilsDriver


@pytest.mark.run(order=1002)
class TestAuditArticle:
    # define fixture's setup method(class level)
    def setup_class(self):
        self.home_proxy = HomeProxy()
        self.audit_proxy = AuditProxy()

    # define fixture's teardown method (class level）
    def teardown_class(self):
        UtilsDriver.quit_mis_driver()

    # define testing methods
    def test_audit_article(self):
        time.sleep(1)
        self.home_proxy.go_content_audit()
        self.audit_proxy.audit_article("发布文章_0828_15", "待审核", "2022-12-13 22:00:00")
        result = self.audit_proxy.audit_article_pass("发布文章_0828_15")
        assert result