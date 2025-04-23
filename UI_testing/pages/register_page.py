from playwright.sync_api import Page

class RegisterPage:
    def __init__(self, page: Page):
        self.page = page
        self.url = "https://practice.expandtesting.com/notes/app/register"
        self.email_address = page.get_by_label("Email address")
        self.password = page.get_by_label("Password")
        self.confirm_password = page.get_by_label("Confirm Password")
        self.name = page.get_by_label("Name")
        self.register_button = page.get_by_role("button", name="Register")

    def open(self):
        self.page.goto(self.url)