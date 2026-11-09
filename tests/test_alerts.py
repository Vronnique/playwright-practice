from faker import Faker
from playwright.sync_api import Page

from pages.alerts_page import AlertsPage
from ui.page_actions import PageActions

BASE_URL = 'https://the-internet.herokuapp.com/javascript_alerts'


def test_js_alert(page: Page):
    alerts_page = AlertsPage(page)
    actions = PageActions(page)

    actions.goto(BASE_URL)

    actual_dialog_text = alerts_page.click_js_alert_and_accept()
    expected_dialog_text = 'I am a JS Alert'

    # Проверка 1: текст алерта соответствует ожидаемому
    assert actual_dialog_text == expected_dialog_text, (
        f'Ожидали текст алерта: "{expected_dialog_text}", '
        f'получили: "{actual_dialog_text}"'
    )

    actual_result_message = alerts_page.get_result_message()
    expected_result_message = 'You successfully clicked an alert'

    # Проверка 2: текст в секции Result соответствует ожидаемому
    assert actual_result_message == expected_result_message, (
        f'Ожидали текст в Result: "{expected_result_message}", '
        f'получили: "{actual_result_message}"'
    )


def test_js_confirm(page: Page):
    alerts_page = AlertsPage(page)
    actions = PageActions(page)

    actions.goto(BASE_URL)

    actual_dialog_text = alerts_page.click_js_confirm_and_accept()
    expected_dialog_text = 'I am a JS Confirm'

    # Проверка 1: текст алерта соответствует ожидаемому
    assert actual_dialog_text == expected_dialog_text, (
        f'Ожидали текст алерта: "{expected_dialog_text}", '
        f'получили: "{actual_dialog_text}"'
    )

    actual_result_message = alerts_page.get_result_message()
    expected_result_message = 'You clicked: Ok'

    # Проверка 2: текст в секции Result соответствует ожидаемому
    assert actual_result_message == expected_result_message, (
        f'Ожидали текст в Result: "{expected_result_message}", '
        f'получили: "{actual_result_message}"'
    )


def test_js_prompt(page: Page):
    alerts_page = AlertsPage(page)
    actions = PageActions(page)
    fake = Faker()
    random_text = fake.word()

    actions.goto(BASE_URL)

    actual_dialog_text = alerts_page.click_js_prompt_and_accept(random_text)
    expected_dialog_text = 'I am a JS prompt'

    # Проверка 1: текст алерта соответствует ожидаемому
    assert actual_dialog_text == expected_dialog_text, (
        f'Ожидали текст алерта: "{expected_dialog_text}", '
        f'получили: "{actual_dialog_text}"'
    )

    actual_result_message = alerts_page.get_result_message()
    expected_result_message = f'You entered: {random_text}'

    # # Проверка 2: текст в секции Result соответствует ожидаемому
    assert actual_result_message == expected_result_message, (
        f'Ожидали текст в Result: "{expected_result_message}", '
        f'получили: "{actual_result_message}"'
    )
