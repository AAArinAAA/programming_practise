import pytest

import pages.main_page


@pytest.mark.smoke
class TestLogin:
    def test_user_login(self, browser):
        m = pages.main_page.Main(browser)
        m.user_login()