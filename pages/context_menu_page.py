from playwright.sync_api import Page

from ui.page_actions import PageActions
from ui.web_element import WebElement


class ContextMenuPage:
    def __init__(self, page: Page):
        self.page = page
        self.actions = PageActions(page)

        self.context_menu_area = WebElement(
            page.locator('#hot-spot'),
            description='Выделенная область'
        )

    def right_click_and_accept_alert(self) -> str:
        return self.actions.run_and_accept_alert(self.context_menu_area.right_click)
