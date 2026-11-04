from playwright.sync_api import Page

from ui.web_element import WebElement


class BasicAuthPage:
    def __init__(self, page: Page) -> None:
        self.page = page
        self.success_message = WebElement(
            page.get_by_text('Congratulations! You must have the proper credentials.'),
            description='Текст успешной авторизации'
        )

    def get_success_message(self) -> str:
        return self.success_message.get_inner_text()
