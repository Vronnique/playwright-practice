from playwright.sync_api import Page

from pages.basic_auth_page import BasicAuthPage
from ui.page_actions import PageActions
from utils.url_utils import embed_credentials_in_url

TEST_URL = 'http://the-internet.herokuapp.com/basic_auth'
EXPECTED_TEXT = 'Congratulations! You must have the proper credentials.'


def test_basic_auth(page: Page):
    auth_page = BasicAuthPage(page)
    actions = PageActions(page)

    auth_url = embed_credentials_in_url(TEST_URL, "admin", "admin")
    actions.goto(auth_url)

    actual_text = auth_page.get_success_message()

    # Проверка 1: отображаемый текст соответствует ожидаемому
    assert actual_text == EXPECTED_TEXT, (
        f'Ожидали: "{EXPECTED_TEXT}", '
        f'получили: "{actual_text}"'
    )
