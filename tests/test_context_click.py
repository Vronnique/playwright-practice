from playwright.sync_api import Page

from pages.context_menu_page import ContextMenuPage
from ui.page_actions import PageActions

BASE_URL = 'https://the-internet.herokuapp.com/context_menu'
EXPECTED_DIALOG_TEXT = 'You selected a context menu'


def test_right_click(page: Page):
    context_menu_page = ContextMenuPage(page)
    actions = PageActions(page)

    actions.goto(BASE_URL)

    actual_dialog_text = context_menu_page.right_click_and_accept_alert()

    # Проверка: текст алерта соответствует ожидаемому
    assert actual_dialog_text == EXPECTED_DIALOG_TEXT, (
        f'Ожидали текст алерта: "{EXPECTED_DIALOG_TEXT}", '
        f'получили: "{actual_dialog_text}"'
    )
