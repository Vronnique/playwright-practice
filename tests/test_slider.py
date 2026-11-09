import random
from playwright.sync_api import Page

from pages.slider_page import SliderPage
from ui.page_actions import PageActions

BASE_URL = 'https://the-internet.herokuapp.com/horizontal_slider'


def test_slider(page: Page):
    slider_page = SliderPage(page)
    actions = PageActions(page)

    actions.goto(BASE_URL)

    # задаём рандомное значение слайдера
    steps = random.randint(1, 9)
    slider_page.set_value_by_keyboard(steps)

    # получаем значение отображаемое в индикаторе
    actual_indicator_value = slider_page.get_indicator_text()
    expected_indicator_value = steps * 0.5

    # Проверка: отображаемое значение индикатора соответствует заданному
    assert float(actual_indicator_value) == expected_indicator_value, (
        f'Ожидали значение индикатора: {expected_indicator_value}, '
        f'Получили: {actual_indicator_value}'
    )
