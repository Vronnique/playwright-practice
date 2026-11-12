from playwright.sync_api import Page

from pages.scroll_page import ScrollPage
from ui.page_actions import PageActions

BASE_URL = 'https://the-internet.herokuapp.com/infinite_scroll'


def test_scroll(page: Page):
    scroll_page = ScrollPage(page)
    actions = PageActions(page)

    actions.goto(BASE_URL)

    actual_paragraphs_count = scroll_page.scroll_until_paragraphs()
    expected_paragraphs_count = 10
    # Проверка: кол-во абзацев на странице >= ожидаемому
    assert actual_paragraphs_count >= expected_paragraphs_count, (
        f'Ожидали получить кол-во абзацев: {expected_paragraphs_count} или больше. '
        f'Получили: {actual_paragraphs_count}'
    )
