from playwright.sync_api import Page

from ui.web_element import WebElement


class NewWindowPage:
    def __init__(self, page: Page) -> None:
        self.page = page

        self.text = WebElement(
            page.locator('.example h3'),
            description='Текст на новой странице'
        )

    def get_new_window_text(self) -> str:
        return self.text.get_inner_text()
