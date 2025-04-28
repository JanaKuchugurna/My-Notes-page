import pytest
from UI_testing.tests.testdata import login_test_data
from playwright.sync_api import expect


@pytest.mark.parametrize("email, password, should_login", login_test_data)
def test_login(login_page, email, password, should_login):
    login_page.user_email.fill(email)
    login_page.password.fill(password)
    login_page.login_button.click()

    if should_login:
        # Successful login → expect to land on the notes page
        expect(login_page.page).to_have_url("https://practice.expandtesting.com/notes/app")
        return

    # Failed login → expect to stay on the login page
    expect(login_page.page).to_have_url("https://practice.expandtesting.com/notes/app/login")

    # Empty email field
    if email == "":
        expect(login_page.page.get_by_text("Email address is required")).to_be_visible()
        return

    # Empty password field
    if password == "":
        expect(login_page.page.get_by_text("Password is required")).to_be_visible()
        return

    # Password consisting only of spaces → toast shows length error
    if password.strip() == "":
        toast = login_page.page.locator('[data-testid="alert-message"]')
        expect(toast).to_be_visible()
        expect(toast).to_contain_text("Password must be between 6 and 30 characters")
        return

    # Invalid email format (leading/trailing spaces or missing "@")
    if email.strip() != email or "@" not in email:
        expect(login_page.page.get_by_text("Email address is invalid")).to_be_visible()
        return

    # Toast-based errors
    toast = login_page.page.locator('[data-testid="alert-message"]')
    login_page.page.wait_for_selector('[data-testid="alert-message"]', timeout=5000)

    # Incorrect credentials
    expect(toast).to_be_visible()
    expect(toast).to_contain_text("Incorrect email address or password")
