import random
import string

from playwright.sync_api import Page

URL = 'http://2.26.162.45:8080'
ERROR_TEXT = 'Invalid login or password.'

def test_login(page: Page):
    page.goto(URL)
    page.get_by_test_id('nav-login').click()

    username = ''.join(random.choices(string.ascii_letters, k=8))
    password = ''.join(random.choices(string.ascii_letters, k=10))

    page.get_by_test_id('login-username').fill(username)
    page.get_by_test_id('login-password').fill(password)
    page.get_by_role('button').click()

    spinner = page.get_by_test_id('login-submit-spinner')
    error = page.get_by_test_id('login-error-inline')

    spinner.wait_for(state='visible')
    spinner.wait_for(state='hidden')
    error.wait_for(state='visible')

    spinner_hidden = spinner.is_hidden()
    assert spinner_hidden, (f'Ожидалось: появление и исчезновение индикатора загрузки.'
                            f'Фактически: {spinner_hidden}')

    error_visible = error.is_visible()
    assert error_visible, (f"Ожидалось: появление сообщения об ошибке {ERROR_TEXT} после исчезновения индикатора загрузки."
                           f"Фактически: {error_visible}")