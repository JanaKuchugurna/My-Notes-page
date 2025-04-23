from playwright.sync_api import Page


class LoginPage:

    def __init__(self, page: Page):
        self.page = page
        self.url = "https://practice.expandtesting.com/notes/app/login"
        self.user_email = page.get_by_label("email")
        self.password = page.get_by_label("password")
        self.login_button = page.get_by_role("button", name="Login")

    def open(self):
        self.page.goto(self.url)
