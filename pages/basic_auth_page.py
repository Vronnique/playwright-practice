from playwright.sync_api import Page

from ui.web_element import WebElement

from utils.url_utils import embed_credentials_in_url


class BasicAuthPage:
    def __init__(self, page: Page) -> None:
        self.page = page
        self.success_message = WebElement(
            page.get_by_text('Congratulations! You must have the proper credentials.'),
            description='Текст успешной авторизации'
        )

    def open_with_auth(self, url: str, username: str, password: str) -> None:
        auth_url = embed_credentials_in_url(url, username, password)
        self.page.goto(auth_url)

    def get_success_message(self) -> str:
        return self.success_message.get_inner_text()