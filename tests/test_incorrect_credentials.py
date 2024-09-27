from ..pages.LoginPage import LoginPage


def test_incorrect_credentials(page):
    login_page = LoginPage(page)

    login_page.navigate()

    login_page.put_username(username='standard_user')
    login_page.put_password(password='wrong_password')

    login_page.click_button()

    login_page.assert_invalid_error()

def test_incorrect_credentials2(page):
    login_page = LoginPage(page)

    login_page.navigate()

    login_page.put_username(username='locked_out_user')
    login_page.put_password(password='wrong_password')

    login_page.click_button()

    login_page.assert_invalid_error()

def test_incorrect_credentials3(page):
    login_page = LoginPage(page)

    login_page.navigate()

    login_page.put_username(username='problem_user')
    login_page.put_password(password='wrong_password')

    login_page.click_button()

    login_page.assert_invalid_error()

def test_incorrect_credentials4(page):
    login_page = LoginPage(page)

    login_page.navigate()

    login_page.put_username(username='performance_glitch_user')
    login_page.put_password(password='wrong_password')

    login_page.click_button()

    login_page.assert_invalid_error()

def test_incorrect_credentials5(page):
    login_page = LoginPage(page)

    login_page.navigate()

    login_page.put_username(username='error_user')
    login_page.put_password(password='wrong_password')

    login_page.click_button()

    login_page.assert_invalid_error()

def test_incorrect_credentials6(page):
    login_page = LoginPage(page)

    login_page.navigate()

    login_page.put_username(username='visual_user')
    login_page.put_password(password='wrong_password')

    login_page.click_button()

    login_page.assert_invalid_error()