from UI_testing.pages.register_page import RegisterPage


def test_empty_register_fields(register_page: RegisterPage):
    register_page.email_address.fill("")
    register_page.password.fill("")
    register_page.confirm_password.fill("")
    register_page.name.fill("")
    register_page.register_button.click()

def test_only_email_field(register_page: RegisterPage):
    register_page.email_address.fill("anna@gmail.com")
    register_page.password.fill("")
    register_page.confirm_password.fill("")
    register_page.name.fill("")
    register_page.register_button.click()

def test_only_name_field(register_page: RegisterPage):
    register_page.email_address.fill("")
    register_page.password.fill("")
    register_page.confirm_password.fill("")
    register_page.name.fill("Anna")
    register_page.register_button.click()

def test_invalid_email(register_page: RegisterPage):
    register_page.email_address.fill("anna.gmail.com")
    register_page.password.fill("")
    register_page.confirm_password.fill("")
    register_page.name.fill("")
    register_page.register_button.click()

def test_without_confirmation_password(register_page: RegisterPage):
    register_page.email_address.fill("anna@gmail.com")
    register_page.password.fill("456789")
    register_page.confirm_password.fill("")
    register_page.name.fill("Anna")
    register_page.register_button.click()

def test_difference_password_and_confirmation(register_page: RegisterPage):
    register_page.email_address.fill("anna@gmail.com")
    register_page.password.fill("456789")
    register_page.confirm_password.fill("987654")
    register_page.name.fill("Anna")
    register_page.register_button.click()

def test_short_password(register_page: RegisterPage):
    register_page.email_address.fill("anna@gmail.com")
    register_page.password.fill("456")
    register_page.confirm_password.fill("456")
    register_page.name.fill("Anna")
    register_page.register_button.click()

def test_short_name(register_page: RegisterPage):
    register_page.email_address.fill("anna@gmail.com")
    register_page.password.fill("456789")
    register_page.confirm_password.fill("456789")
    register_page.name.fill("Ana")
    register_page.register_button.click()

def test_exist_email_registration(register_page: RegisterPage):
    register_page.email_address.fill("anna@gmail.com")
    register_page.password.fill("456789")
    register_page.confirm_password.fill("456789")
    register_page.name.fill("Anna")
    register_page.register_button.click()

def test_invalid_email(register_page: RegisterPage):
    register_page.email_address.fill("anna.@gmail.com")
    register_page.password.fill("456789")
    register_page.confirm_password.fill("456789")
    register_page.name.fill("Anna")
    register_page.register_button.click()

def test_space_inputs(register_page: RegisterPage):
    register_page.email_address.fill(" ")
    register_page.password.fill(" ")
    register_page.confirm_password.fill(" ")
    register_page.name.fill(" ")
    register_page.register_button.click()
