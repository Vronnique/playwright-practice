from pathlib import Path
from playwright.sync_api import Page

from ui.web_element import WebElement


class FileUploaderPage:
    def __init__(self, page: Page) -> None:
        self.page = page

        self.file_input = WebElement(
            page.locator('#file-upload'),
            description='Выбор файла'
        )

        self.upload_button = WebElement(
            page.locator('#file-submit'),
            description='Кнопка "Upload"'
        )

        self.updated_page_text = WebElement(
            page.locator('.example h3'),
            description='Текст на обновленной странице'
        )

        self.file_name = WebElement(
            page.locator('#uploaded-files'),
            description='Имя загруженного файла'
        )

    def set_input_file(self, filepath: Path) -> None:
        self.file_input.set_input_files(filepath)

    def click_upload_button(self) -> None:
        self.upload_button.click()

    def get_updated_page_text(self) -> str:
        return self.updated_page_text.get_inner_text().strip()

    def get_file_name(self) -> str:
        return self.file_name.get_inner_text().strip()
