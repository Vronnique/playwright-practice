import pytest
from playwright.sync_api import Page

from pages.basic_auth_page import BasicAuthPage

BASE_URL = 'http://the-internet.herokuapp.com/basic_auth'
EXPECTED_TEXT = 'Congratulations! You must have the proper credentials.'


def test_basic_auth(page: Page):
    auth_page = BasicAuthPage(page)

    auth_page.open_with_auth(url=BASE_URL, username='admin', password='admin')
    actual_text = auth_page.get_success_message()

    # Проверка 1: отображаемый текст соответствует ожидаемому
    assert actual_text == EXPECTED_TEXT, (f'Ожидали: "{EXPECTED_TEXT}", получили: "{actual_text}"')
