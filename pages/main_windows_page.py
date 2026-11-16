from playwright.sync_api import Page

from ui.web_element import WebElement


class MainWindowsPage:
    def __init__(self, page: Page):
        self.page = page

        self.new_window_link = WebElement(
            page.get_by_role('link', name='Click Here'),
            description='Ссылка "Click Here"'
        )

    def click_new_window_link(self) -> None:
        self.new_window_link.click()
