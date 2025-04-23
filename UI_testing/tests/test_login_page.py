from UI_testing.pages.login_page import LoginPage


def test_valid_login_inputs(login_page: LoginPage):
    login_page.user_email.fill("anna@gmail.com")
    login_page.password.fill("123456")
    login_page.login_button.click()


def test_invalid_login_inputs(login_page: LoginPage):
    login_page.user_email.fill("anna@gmail.com")
    login_page.password.fill("789456")
    login_page.login_button.click()


def test_empty_login_inputs(login_page: LoginPage):
    login_page.user_email.fill("")
    login_page.password.fill("")
    login_page.login_button.click()


def test_only_email_input(login_page: LoginPage):
    login_page.user_email.fill("anna@gmail.com")
    login_page.password.fill("")
    login_page.login_button.click()


def test_only_password_input(login_page: LoginPage):
    login_page.user_email.fill("")
    login_page.password.fill("789456")
    login_page.login_button.click()


def test_incorrect_format_of_email(login_page: LoginPage):
    login_page.user_email.fill(" anna @gmail.com")
    login_page.password.fill("789456")
    login_page.login_button.click()


def test_incorrect_format_of_password(login_page: LoginPage):
    login_page.user_email.fill("anna@gmail.com")
    login_page.password.fill("   ")
    login_page.login_button.click()
