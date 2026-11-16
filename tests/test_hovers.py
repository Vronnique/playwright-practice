from playwright.sync_api import Page

from pages.hovers_page import HoversPage
from ui.page_actions import PageActions

NAME_TEMPLATE = 'name: user{N}'  # где N — порядковый номер карточки пользователя


def test_hover_all_users(page: Page):
    hovers_page = HoversPage(page)
    actions = PageActions(page)

    actions.goto('/hovers')

    for i, _ in enumerate(hovers_page.users):
        hovers_page.hover_user(i)
        actual_name = hovers_page.get_name_text(i)
        expected_name = NAME_TEMPLATE.format(N=i + 1)
        # Проверка: при наведении курсора отображается имя пользователя в формате NAME_TEMPLATE
        assert actual_name == expected_name, (
            f'Карточка пользователя {i + 1}: ожидали имя: {expected_name}, '
            f'Получили: {actual_name}'
        )
