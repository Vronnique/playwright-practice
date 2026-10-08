import random
import string

from playwright.sync_api import Page

URL = 'http://2.26.162.45:8080'
ERROR_TEXT = 'Invalid login or password.'

def test_login(page: Page):
    # Данные
    username = ''.join(random.choices(string.ascii_letters, k=8))
    password = ''.join(random.choices(string.ascii_letters, k=10))

    # Действия
    page.goto(URL)
    page.get_by_test_id('nav-login').click()
    page.get_by_test_id('login-username').fill(username)
    page.get_by_test_id('login-password').fill(password)
    page.get_by_role('button').click()

    # Локаторы
    spinner = page.get_by_test_id('login-submit-spinner')
    error = page.get_by_test_id('login-error-inline')

    # Явные ожидания
    spinner.wait_for(state='visible')
    spinner.wait_for(state='hidden')
    error.wait_for(state='visible')

    # Проверка спиннера
    assert spinner.is_hidden(), 'Индикатор загрузки не исчез после завершения запроса'

    # Проверка ошибки
    actual_error = error.text_content()
    assert actual_error == ERROR_TEXT, (f"Ожидалась ошибка: {ERROR_TEXT} "
                                        f"Фактически: {actual_error}")
