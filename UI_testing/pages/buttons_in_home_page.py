import re

from playwright.sync_api import Page

class ButtonsPage:

    def __init__(self, page: Page):
        self.page = page
        self.url = "https://practice.expandtesting.com/notes/app/"
        self.add_note_button = page.get_by_role("button", name="+ Add Note")
        self.notes = page.locator('[data-testid="note-card"]')
        self.note_titles = page.locator('[data-testid="note-card-title"]')
        self.note_title_input = page.get_by_label("Title:")
        self.note_description_input = page.get_by_label("Description:")
        self.create_button = page.get_by_role("button", name="Create")
        self.search_button = page.get_by_role("button", name="Search")
        self.search_input = page.get_by_placeholder("Search notes...")
        self.profile_button = page.locator('[data-testid="profile"]')
        self.full_name_input = page.get_by_test_id("user-name")
        self.update_profile_button = page.get_by_role("button", name="Update profile")
        self.logout_button = page.get_by_role("button", name="Logout")
        self.login_button = page.locator('a[href="/notes/app/login"]')
        self.all_button = page.get_by_role("button", name="All")
        self.home_button = page.get_by_role("button", name="Home")
        self.work_button = page.get_by_role("button", name="Work")
        self.personal_button = page.get_by_role("button", name="Personal")
        self.progress_info = page.locator('[data-testid="progress-info"]')
        self.notes = page.locator('[data-testid="note-card"]')
        self.delete_account_button = page.get_by_test_id("delete-account")
        self.delete_button = self.page.get_by_test_id("note-delete-confirm")


    def open(self):
        self.page.goto(self.url)

    def get_notes_count(self):
        return self.notes.count()

    def get_last_note_title(self):
        return self.notes.nth(-1).text_content()

    def search(self, term: str):
        self.search_button.click()
        self.search_input.fill(term)
        self.search_input.press("Enter")

    def search_result_locator(self, term: str):
        return self.page.locator(f'p:has-text("Search Results for \\"{term}\\"")')

    def get_progress_counts(self) -> tuple[int, int]:
        """Повертає пару (completed, total) витягнуту з тексту виду "You have 3/9 notes..."."""
        text = self.progress_info.text_content().strip()
        match = re.search(r"You have (\d+)/(\d+)", text)
        if not match:
            raise AssertionError(f"Не вдалося витягти числа з '{text}'")
        return int(match.group(1)), int(match.group(2))


