from pathlib import Path

from playwright.sync_api import Page

from pages.file_uploader_page import FileUploaderPage
from ui.page_actions import PageActions

FILE_PATH = Path(__file__).parent.parent / 'file_for_test.txt'
EXPECTED_TEXT = 'File Uploaded!'
EXPECTED_FILE_NAME = FILE_PATH.name


def test_uploader(page: Page):
    uploader_page = FileUploaderPage(page)
    actions = PageActions(page)

    actions.goto('/upload')

    uploader_page.set_input_file(FILE_PATH)
    uploader_page.click_upload_button()

    actual_text = uploader_page.get_updated_page_text()
    # Проверка 1: текст отображаемый на обновленной странице соответствует ожидаемому
    assert actual_text == EXPECTED_TEXT, (
        f'Ожидали на обновленной странице текст: {EXPECTED_TEXT}. '
        f'Получили: {actual_text}'
    )

    actual_file_name = uploader_page.get_file_name()
    # Проверка 2: отображается имя загруженного файла
    assert actual_file_name == EXPECTED_FILE_NAME, (
        f'Ожидали имя файла: {EXPECTED_FILE_NAME}. '
        f'Получили: {actual_file_name}'
    )
