from playwright.sync_api import Page

from pages.main_windows_page import MainWindowsPage
from pages.new_window_page import NewWindowPage
from ui.page_actions import PageActions

BASE_URL = 'https://the-internet.herokuapp.com/windows'
EXPECTED_TEXT = 'New Window'


def test_windows(page: Page):
    main_page = MainWindowsPage(page)
    actions = PageActions(page)

    actions.goto(BASE_URL)

    with actions.expect_new_page() as new_page_info1:
        main_page.click_new_window_link()
    tab2 = new_page_info1.value

    new_page_2 = NewWindowPage(tab2)
    actual_text_2 = new_page_2.get_new_window_text()

    # Проверка 1: отображаемый текст на 2-й вкладке соответствует ожидаемому
    assert actual_text_2 == EXPECTED_TEXT, (
        f'Текст на вкладке 2 не совпал с ожидаемым. '
        f'Ожидали: {EXPECTED_TEXT}, '
        f'Получили: {actual_text_2}'
    )

    actions.bring_to_front()

    with actions.expect_new_page() as new_page_info2:
        main_page.click_new_window_link()
    tab3 = new_page_info2.value

    new_page_3 = NewWindowPage(tab3)
    actual_text_3 = new_page_3.get_new_window_text()

    # Проверка 2: отображаемый текст на 3-й вкладке соответствует ожидаемому
    assert actual_text_3 == EXPECTED_TEXT, (
        f'Текст на вкладке 3 не совпал с ожидаемым. '
        f'Ожидали: {EXPECTED_TEXT}, '
        f'Получили: {actual_text_3}'
    )

    actions.bring_to_front()

    tab2.close()
    tab3.close()

    tabs_count = len(page.context.pages)
    # Проверка 3: кол-во открытых вкладок равно 1
    assert tabs_count == 1, (
        f'Ожидали 1 открытую вкладку, получили: {tabs_count}'
    )
