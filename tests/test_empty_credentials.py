from ..pages.LoginPage import LoginPage


def test_empty_credentials(page):
    
    login_page = LoginPage(page)

    login_page.navigate()

    login_page.put_username(username='')
    login_page.put_password(password='')

    login_page.click_button()

    login_page.assert_empty_error()
