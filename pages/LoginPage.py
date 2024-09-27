from playwright.sync_api import Page, expect

class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.username = page.locator('input[name="user-name"]')
        self.password = page.locator('input[name="password"]')
        self.login_button = 'input[type="submit"]'
        self.error_label = page.locator('h3[data-test="error"]')     

    def navigate(self):
        self.page.goto('https://www.saucedemo.com/')

    def put_username(self, username):
        self.username.fill(username)

    def put_password(self, password):
        self.password.fill(password)

    def click_button(self):
        self.page.click(self.login_button)

    def assert_invalid_error(self):
        expect(self.error_label).to_be_visible()
        expect(self.error_label).to_contain_text('Epic sadface: Username and password'
                                                 ' do not match any user in this service')
    def assert_empty_error(self):
        expect(self.error_label).to_be_visible()
        expect(self.error_label).to_contain_text('Epic sadface: Username is required')