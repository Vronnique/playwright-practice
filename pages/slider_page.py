from playwright.sync_api import Page

from ui.page_actions import PageActions
from ui.web_element import WebElement


class SliderPage:
    def __init__(self, page: Page):
        self.page = page
        self.actions = PageActions(page)

        self.slider = WebElement(
            page.locator('input[type="range"]'),
            description='Слайдер'
        )

        self.indicator = WebElement(
            page.locator('#range'),
            description='Значение слайдера'
        )

    def set_value_by_keyboard(self, steps: int) -> None:
        self.slider.focus()
        for _ in range(steps):
            self.slider.press('ArrowRight')

    def get_indicator_text(self) -> str:
        return self.indicator.get_inner_text()
