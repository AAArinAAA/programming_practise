from playwright.sync_api import Page, expect

class OrderPage1:
    def __init__(self, page: Page):
        self.page = page
        self.checkout_complete = page.locator('h2[data-test="complete-header"]')

    def assert_complete(self):
        expect(self.checkout_complete).to_be_visible()
        expect(self.checkout_complete).to_contain_text('Epic sadface: Username is required')
