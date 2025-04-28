import pytest
from playwright.async_api import expect

from UI_testing.pages.register_page import RegisterPage
from UI_testing.tests.testdata import register_test_data


@pytest.mark.parametrize(
    "email,password,confirm,name,expected_errors",
    register_test_data
)
def test_registration_validation(register_page, email, password, confirm, name, expected_errors):
    # Fill in the form
    register_page.email_address.fill(email)
    register_page.password.fill(password)
    register_page.confirm_password.fill(confirm)
    register_page.name.fill(name)
    register_page.register_button.click()

    # For each expected error message, assert that it appears on screen
    for err in expected_errors:
        locator = register_page.page.get_by_text(err)
        expect(locator).to_be_visible()
# def test_empty_register_fields(register_page: RegisterPage):
#     register_page.email_address.fill("")
#     register_page.password.fill("")
#     register_page.confirm_password.fill("")
#     register_page.name.fill("")
#     register_page.register_button.click()
#
# def test_only_email_field(register_page: RegisterPage):
#     register_page.email_address.fill("karolina@gmail.com")
#     register_page.password.fill("")
#     register_page.confirm_password.fill("")
#     register_page.name.fill("")
#     register_page.register_button.click()
#
# def test_only_name_field(register_page: RegisterPage):
#     register_page.email_address.fill("")
#     register_page.password.fill("")
#     register_page.confirm_password.fill("")
#     register_page.name.fill("Karolina")
#     register_page.register_button.click()
#
# def test_invalid_email(register_page: RegisterPage):
#     register_page.email_address.fill("karolina.gmail.com")
#     register_page.password.fill("")
#     register_page.confirm_password.fill("")
#     register_page.name.fill("")
#     register_page.register_button.click()
#
# def test_without_confirmation_password(register_page: RegisterPage):
#     register_page.email_address.fill("karolina@gmail.com")
#     register_page.password.fill("4567890")
#     register_page.confirm_password.fill("")
#     register_page.name.fill("Karolina")
#     register_page.register_button.click()
#
# def test_difference_password_and_confirmation(register_page: RegisterPage):
#     register_page.email_address.fill("karolina@gmail.com")
#     register_page.password.fill("4567890")
#     register_page.confirm_password.fill("987654")
#     register_page.name.fill("Karolina")
#     register_page.register_button.click()
#
# def test_short_password(register_page: RegisterPage):
#     register_page.email_address.fill("karolina@gmail.com")
#     register_page.password.fill("456")
#     register_page.confirm_password.fill("456")
#     register_page.name.fill("Karolina")
#     register_page.register_button.click()
#
# def test_short_name(register_page: RegisterPage):
#     register_page.email_address.fill("karolina@gmail.com")
#     register_page.password.fill("4567890")
#     register_page.confirm_password.fill("4567890")
#     register_page.name.fill("Keri")
#     register_page.register_button.click()
#
# def test_exist_email_registration(register_page: RegisterPage):
#     register_page.email_address.fill("karolina@gmail.com")
#     register_page.password.fill("4567890")
#     register_page.confirm_password.fill("4567890")
#     register_page.name.fill("Karolina")
#     register_page.register_button.click()
#
# def test_invalid_email(register_page: RegisterPage):
#     register_page.email_address.fill("karolina.@gmail.com")
#     register_page.password.fill("4567890")
#     register_page.confirm_password.fill("4567890")
#     register_page.name.fill("Karolina")
#     register_page.register_button.click()
#
# def test_space_inputs(register_page: RegisterPage):
#     register_page.email_address.fill("      ")
#     register_page.password.fill("      ")
#     register_page.confirm_password.fill("      ")
#     register_page.name.fill("      ")
#     register_page.register_button.click()
