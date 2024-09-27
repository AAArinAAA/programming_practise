from ..pages.LoginPage import LoginPage
from ..pages.ProductPage import ProductPage


def test_ordering(page):
    login_page = LoginPage(page)
    product_page = ProductPage(page)

    login_page.navigate()

    login_page.put_username(username='standard_user')
    login_page.put_password(password='secret_sauce')

    login_page.click_button()


