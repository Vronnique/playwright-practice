from playwright.sync_api import Page

from pages.downloader_page import DownloaderPage
from ui.page_actions import PageActions

INDEX = 2


def test_downloader(page: Page):
    downloader_page = DownloaderPage(page)
    actions = PageActions(page)

    actions.goto('/download')

    expected_file_name = downloader_page.get_file_name(INDEX)

    downloaded_file = downloader_page.download_file(INDEX)
    actual_file_name = downloaded_file.suggested_filename

    # Проверка: имя скачанного файла совпадает с ожидаемым
    assert actual_file_name == expected_file_name, (
        f'Ожидали получить имя: {expected_file_name}, '
        f'Получили: {actual_file_name}'
    )
