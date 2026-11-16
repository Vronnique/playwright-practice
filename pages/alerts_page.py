from playwright.sync_api import Page

from ui.page_actions import PageActions
from ui.web_element import WebElement


class AlertsPage:
    def __init__(self, page: Page) -> None:
        self.page = page
        self.actions = PageActions(page)

        self.js_alert_button = WebElement(
            page.get_by_role('button', name='Click for JS Alert'),
            description='Кнопка "Click for JS Alert"'
        )

        self.js_confirm_button = WebElement(
            page.get_by_role('button', name='Click for JS Confirm'),
            description='Кнопка "Click for JS Confirm"'
        )

        self.js_prompt_button = WebElement(
            page.get_by_role('button', name='Click for JS Prompt'),
            description='Кнопка "Click for JS Prompt"'
        )

        self.result_message = WebElement(
            page.locator('#result'),
            description='Секция Result'
        )

    def click_js_alert_and_accept(self) -> str:
        return self.actions.run_and_accept_alert(self.js_alert_button.click)

    def click_js_confirm_and_accept(self) -> str:
        return self.actions.run_and_accept_alert(self.js_confirm_button.click)

    def click_js_prompt_and_accept(self, input_text: str) -> str:
        return self.actions.run_and_accept_prompt(
            action=self.js_prompt_button.click,
            prompt_text=input_text
        )

    def get_result_message(self) -> str:
        return self.result_message.get_inner_text()
