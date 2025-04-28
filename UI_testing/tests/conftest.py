import pytest
from playwright.sync_api import sync_playwright

from UI_testing.pages.buttons_in_home_page import ButtonsPage
from UI_testing.pages.login_page import LoginPage
from UI_testing.pages.notes import Notes
from UI_testing.pages.register_page import RegisterPage


@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        yield browser
        browser.close()


@pytest.fixture(scope="function")
def page(browser):
    page = browser.new_page()
    yield page
    page.close()


@pytest.fixture
def login_page(page):
    login_page = LoginPage(page)
    login_page.open()
    return login_page


@pytest.fixture
def register_page(page):
    register_page = RegisterPage(page)
    register_page.open()
    return register_page


@pytest.fixture
def buttons_page(page):
    buttons_page = ButtonsPage(page)
    return buttons_page


@pytest.fixture
def notes(page):
    notes = Notes(page)
    return notes


@pytest.fixture
def filled_login_input(login_page: LoginPage):
    login_page.user_email.fill("alenka@gmail.com")
    login_page.password.fill("963852")
    login_page.login_button.click()
    return login_page


@pytest.fixture
def filled_login_input_for_delete_profile(login_page: LoginPage):
    login_page.user_email.fill("katka@gmail.com")
    login_page.password.fill("987654")
    login_page.login_button.click()
    login_page.page.wait_for_load_state("load")
    return login_page
