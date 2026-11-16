import time

from playwright.sync_api import Page

from ui.multi_web_element import MultiWebElement


class ScrollPage:
    def __init__(self, page: Page) -> None:
        self.page = page

        self.paragraphs = MultiWebElement(
            page=page,
            locator=page.locator('.jscroll-added'),
            description='Абзацы'
        )

    def scroll_until_paragraphs(self, target: int = 10, timeout_sec: float = 30.0) -> int:
        end = time.monotonic() + timeout_sec
        while time.monotonic() < end:
            count = self.paragraphs.count()
            if count >= target:
                return count
            self.paragraphs.last().scroll_into_view_if_needed()
        return self.paragraphs.count()
