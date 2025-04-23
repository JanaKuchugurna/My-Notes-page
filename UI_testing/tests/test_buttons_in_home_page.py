from UI_testing.pages.buttons_in_home_page import ButtonsPage
import uuid


def test_add_note_button(filled_login_input, buttons_page: ButtonsPage):
    unique_title = f"Test Note {uuid.uuid4()}"
    buttons_page.page.wait_for_selector('[data-testid="note-card"]')
    count_before = buttons_page.get_notes_count()
    buttons_page.add_note_button.click()
    buttons_page.note_title_input.fill(unique_title)
    buttons_page.note_description_input.fill("This is a test note.")
    buttons_page.create_button.click()
    buttons_page.page.wait_for_selector(f'[data-testid="note-card-title"] >> text={unique_title}', timeout=5000)
    count_after = buttons_page.get_notes_count()

    assert count_after == count_before + 1, "Note count did not increase after adding a note"
    assert "Test Note Title" in buttons_page.get_last_note_title()


def test_search_button_opens_input(filled_login_input, buttons_page: ButtonsPage):
    buttons_page.search_button.click()
    buttons_page.page.wait_for_selector('[placeholder="Search notes..."]', state="visible", timeout=3000)
    assert buttons_page.search_input.is_visible(), "Search input did not appear after clicking Search button"


def test_search_functionality(filled_login_input, buttons_page: ButtonsPage):
    search_term = "123456"
    buttons_page.search(search_term)
    result = buttons_page.search_result_locator(search_term)
    result.wait_for(state="visible", timeout=5000)
    assert result.is_visible(), "Search Results header is not visible"
    text = result.text_content()
    assert search_term in text, f"Expected '{search_term}' in result text, but got '{text}'"


def test_profile_button(filled_login_input, buttons_page: ButtonsPage):
    buttons_page.profile_button.click()
    buttons_page.page.wait_for_url("**/notes/app/profile", timeout=5000)
    current_url = buttons_page.page.url
    assert "/notes/app/profile" in current_url, f"Expected to be on profile page, but got {current_url}"


def test_update_button_in_profile(filled_login_input, buttons_page: ButtonsPage):
    buttons_page.profile_button.click()
    buttons_page.page.wait_for_url("**/notes/app/profile", timeout=5000)
    buttons_page.full_name_input.fill("Yana")
    buttons_page.update_profile_button.click()
    assert buttons_page.full_name_input.input_value() == "Yana"


def test_delete_button_in_profile(filled_login_input_for_delete_profile, buttons_page: ButtonsPage):
    buttons_page.page.wait_for_load_state("networkidle")
    assert "/notes/app" in buttons_page.page.url, "Did not navigate to the page after login."
    buttons_page.page.wait_for_selector('[data-testid="profile"]', timeout=10000)
    buttons_page.profile_button.click()
    buttons_page.page.wait_for_url("**/notes/app/profile", timeout=10000)
    buttons_page.page.wait_for_selector('[data-testid="delete-account"]', timeout=5000)
    buttons_page.delete_account_button.click()
    buttons_page.page.wait_for_selector('[data-testid="note-delete-confirm"]', timeout=5000)
    buttons_page.delete_button.click()
    buttons_page.page.wait_for_selector('[data-testid="alert-message"]', timeout=5000)
    message = buttons_page.page.locator('[data-testid="alert-message"]').inner_text()

    assert "Your account has been deleted" in message, "The deletion message did not appear."


def test_logout_button(filled_login_input, buttons_page: ButtonsPage):
    buttons_page.logout_button.click()
    buttons_page.page.wait_for_selector('a[href="/notes/app/login"]', timeout=5000)
    assert buttons_page.login_button.is_visible()
    assert buttons_page.logout_button.is_hidden()


def test_progress_info_all_category(filled_login_input, buttons_page: ButtonsPage):
    buttons_page.all_button.click()
    buttons_page.page.wait_for_selector('[data-testid="progress-info"]')
    completed, total = buttons_page.get_progress_counts()
    real_count = buttons_page.get_notes_count()
    assert total == real_count, (
        f"We waite total={real_count}, and see total={total}"
    )
    assert 0 <= completed <= total


def test_progress_info_home_category(filled_login_input, buttons_page: ButtonsPage):
    buttons_page.home_button.click()
    buttons_page.page.wait_for_selector('[data-testid="progress-info"]')
    completed, total = buttons_page.get_progress_counts()
    real_home = buttons_page.get_notes_count()
    print(f"[DEBUG] Progress says: {completed}/{total}, real notes count: {real_home}")
    assert total == real_home, f"Expected {total} notes in Home, but found {real_home}"
    assert completed <= total, f"Completed ({completed}) must not exceed total ({total})"


def test_progress_info_work_category(filled_login_input, buttons_page: ButtonsPage):
    buttons_page.work_button.click()
    buttons_page.page.wait_for_selector('[data-testid="progress-info"]')
    completed, total = buttons_page.get_progress_counts()
    real_work = buttons_page.get_notes_count()
    print(f"[DEBUG] Progress says: {completed}/{total}, real notes count: {real_work}")
    assert total == real_work, f"Expected {total} notes in Work, but found {real_work}"
    assert completed <= total, f"Completed ({completed}) must not exceed total ({total})"


def test_progress_info_personal_category(filled_login_input, buttons_page: ButtonsPage):
    buttons_page.personal_button.click()
    buttons_page.page.wait_for_selector('[data-testid="progress-info"]')
    completed, total = buttons_page.get_progress_counts()
    real_personal = buttons_page.get_notes_count()
    print(f"[DEBUG] Progress says: {completed}/{total}, real notes count: {real_personal}")
    assert total == real_personal, f"Expected {total} notes in Personal, but found {real_personal}"
    assert completed <= total, f"Completed ({completed}) must not exceed total ({total})"
