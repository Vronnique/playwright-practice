from playwright.sync_api import Page

from ui.multi_web_element import MultiWebElement


class HoversPage(Page):
    def __init__(self, page: Page):
        self.page = page

        self.users = MultiWebElement(
            page,
            page.locator('.figure'),
            description='Все карточки пользователей'
        )

        self.users_names = MultiWebElement(
            page,
            page.locator('.figure .figcaption h5'),
            description='Имена пользователей'
        )

    def hover_user(self, index: int) -> None:
        self.users.nth(index).hover()

    def get_name_text(self, index: int) -> str:
        return self.users_names.nth(index).get_inner_text()
