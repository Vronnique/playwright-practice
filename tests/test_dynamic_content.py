from collections import Counter

from playwright.sync_api import Page

from pages.dinamyc_content_page import DinamycContentPage
from ui.page_actions import PageActions

MAX_ATTEMPTS = 20


def test_dynamic_content(page: Page):
    dc_page = DinamycContentPage(page)
    actions = PageActions(page)

    actions.goto('/dynamic_content')

    found = False
    for _ in range(MAX_ATTEMPTS):
        srcs = dc_page.get_images_src()
        counts = Counter(srcs)
        if max(counts.values()) >= 2:
            found = True
            break
        page.reload()

    # Проверка: найдены два одинаковых изображения среди трёх
    assert found, (
        f'За {MAX_ATTEMPTS} попыток изображения не совпали'
    )
