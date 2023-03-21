import unittest
import ddt
from base.get_driver import GetDriver
from page.page_login import PageLogin

data = [('85978293725', '111aaa'),
        ('85978293725', '222aaa')]


@ddt.ddt
class TestLogin(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = GetDriver.get_driver()
        self.login = PageLogin(self.driver)
        self.driver.implicitly_wait(5)

    @ddt.unpack
    @ddt.data(['85978293725', '111aaa'], ['85978293725', '222aaa'])
    def test_login(self, username, password):
        self.login.page_login(username, password)
        # eq

    def tearDown(self) -> None:
        GetDriver.quit_driver()


if __name__ == '__main__':
    unittest.main()
