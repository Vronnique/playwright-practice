from playwright.sync_api import Page

from pages.frames_page import FramesPage
from ui.page_actions import PageActions


def test_frames(page: Page):
    actions = PageActions(page)

    actions.goto('/nested_frames')

    frames_page = FramesPage(page)

    actual_left_text = frames_page.get_left_frame_text()
    expected_left_text = 'LEFT'
    # Проверка 1: текст левого фрейма соответствует ожидаемому
    assert actual_left_text == expected_left_text, (
        f'Текст левого фрейма не совпал. '
        f'Ожидали: "{expected_left_text}", получили: "{actual_left_text}"'
    )

    actual_right_text = frames_page.get_right_frame_text()
    expected_right_text = 'RIGHT'
    # Проверка 2: текст правого фрейма соответствует ожидаемому
    assert actual_right_text == expected_right_text, (
        f'Текст правого фрейма не совпал. '
        f'Ожидали: "{expected_right_text}", получили: "{actual_right_text}"'
    )

    actual_bottom_text = frames_page.get_bottom_frame_text()
    expected_bottom_text = 'BOTTOM'
    # Проверка 3: текст нижнего фрейма соответствует ожидаемому
    assert actual_bottom_text == expected_bottom_text, (
        f'Текст нижнего фрейма не совпал. '
        f'Ожидали: "{expected_bottom_text}", получили: "{actual_bottom_text}"'
    )

    actual_middle_text = frames_page.get_middle_frame_text()
    expected_middle_text = 'MIDDLE'
    # Проверка 4: текст центрального фрейма соответствует ожидаемому
    assert actual_middle_text == expected_middle_text, (
        f'Текст центрального фрейма не совпал. '
        f'Ожидали: "{expected_middle_text}", получили: "{actual_middle_text}"'
    )
