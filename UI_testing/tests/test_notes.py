from UI_testing.pages.notes import Notes

from playwright.sync_api import expect


def test_no_notes_message(filled_login_input, notes: Notes):
    # notes.page.wait_for_load_state("networkidle")
    notes.all_button.click()
    expect(notes.no_notes_locator).to_be_visible(timeout=10000)
    message = notes.no_notes_locator.inner_text()
    print("📩 Message displayed:", message)
    assert "You don't have any notes in all categories" in message, "❌ Повідомлення про відсутність нотаток не з'явилось"


def test_create_new_note(filled_login_input, notes: Notes, categories="Home", completed=False):
    notes.add_note_button.click()
    notes.note_title_input.fill("Notes1")
    notes.note_description_input.fill("My notes1")
    if categories in ["Home", "Work", "Personal"]:
        notes.my_select_option.select_option(categories)
    else:
        raise ValueError(f"Unknown a{categories}")

    if completed:
        notes.completed_checkbox.check()

    notes.create_button.click()


