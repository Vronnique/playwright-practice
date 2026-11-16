import random

from playwright.sync_api import Page

from pages.slider_page import SliderPage
from ui.page_actions import PageActions


def test_slider(page: Page):
    slider_page = SliderPage(page)
    actions = PageActions(page)

    actions.goto('/horizontal_slider')

    # получаем граничные значения слайдера
    step_val = slider_page.get_step()
    min_val = slider_page.get_min_value()
    max_val = slider_page.get_max_value()

    total_steps = int((max_val - min_val) / step_val)  # всего шагов можно сделать

    # задаём рандомное значение слайдера
    random_steps = random.randrange(1, total_steps)
    slider_page.set_value_by_keyboard(random_steps)

    # получаем значение отображаемое в индикаторе
    actual_indicator_value = slider_page.get_indicator_text()
    expected_indicator_value = min_val + random_steps * step_val

    # Проверка: отображаемое значение индикатора соответствует заданному
    assert float(actual_indicator_value) == expected_indicator_value, (
        f'Ожидали значение индикатора: {expected_indicator_value}, '
        f'Получили: {actual_indicator_value}'
    )
