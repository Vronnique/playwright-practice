from playwright.sync_api import Page

from ui.multi_web_element import MultiWebElement


class DinamycContentPage:
    def __init__(self, page: Page):
        self.page = page

        self.images = MultiWebElement(
            page=page,
            locator=page.locator('.large-2.columns img'),
            description='Изображения на странице'
        )

    def get_images_src(self) -> list[str]:
        result = []
        for i in range(self.images.count()):
            src = self.images.nth(i).get_attribute('src')
            if src is not None:
                result.append(src)
        return result
