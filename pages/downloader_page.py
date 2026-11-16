from playwright.sync_api import Download, Page

from ui.multi_web_element import MultiWebElement


class DownloaderPage:
    def __init__(self, page: Page) -> None:
        self.page = page

        self.all_files = MultiWebElement(
            page=page,
            locator=page.locator('.example a'),
            description='Имена всех файлов'
        )

    def get_file_name(self, index: int) -> str:
        return self.all_files.nth(index).get_inner_text().strip()

    def download_file(self, index: int) -> Download:
        with self.page.expect_download() as download_info:
            self.all_files.nth(index).click()
        return download_info.value
