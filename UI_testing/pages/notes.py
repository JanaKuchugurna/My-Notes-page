from playwright.sync_api import Page


class Notes:
    def __init__(self, page: Page):
        self.page = page
        self.url = "https://practice.expandtesting.com/notes/app"
        self.no_notes_locator = page.get_by_text("You don't have any notes in all categories")
        self.all_button = page.get_by_role("button", name="All")
        self.add_note_button = page.get_by_role("button", name="+ Add Note")
        self.note_title_input = page.get_by_label("Title:")
        self.note_description_input = page.get_by_label("Description:")
        self.create_button = page.get_by_role("button", name="Create")
        self.completed_checkbox = page.get_by_role('checkbox', name='Completed')
        self.my_select_option = page.get_by_test_id("note-category")

    def open(self):
        self.page.goto(self.url)
