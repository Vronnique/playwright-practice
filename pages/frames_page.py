from playwright.sync_api import Frame, Page

from ui.web_element import WebElement


class FramesPage:
    def __init__(self, page: Page) -> None:
        self.page = page

        self.left_frame_text = WebElement(
            self._get_frame('frame-left').locator('body'),
            description='Текст левого frame'
        )

        self.right_frame_text = WebElement(
            self._get_frame('frame-right').locator('body'),
            description='Текст правого frame'
        )

        self.bottom_frame_text = WebElement(
            self._get_frame('frame-bottom').locator('body'),
            description='Текст нижнего frame'
        )

        self.middle_frame_text = WebElement(
            self._get_frame('frame-middle').locator('#content'),
            description='Текст центрального frame'
        )

    def get_left_frame_text(self) -> str:
        return self.left_frame_text.get_inner_text().strip()

    def get_middle_frame_text(self) -> str:
        return self.middle_frame_text.get_inner_text().strip()

    def get_right_frame_text(self) -> str:
        return self.right_frame_text.get_inner_text().strip()

    def get_bottom_frame_text(self) -> str:
        return self.bottom_frame_text.get_inner_text().strip()

    def _get_frame(self, name: str) -> Frame:
        frame = self.page.frame(name=name)
        if frame is None:
            raise RuntimeError(f"Frame '{name}' не найден")
        return frame
