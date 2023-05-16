import pytest
from utils import UtilsDriver

@pytest.mark.run(order=1000)
class TestBegin:
    def test_begin(self):
        # UtilsDriver._quit_mis_driver = False
        UtilsDriver.set_quit_driver(False)