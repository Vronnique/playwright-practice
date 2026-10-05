import random
import string

from playwright.sync_api import Page, expect

def test_login(page: Page):
    page.goto('http://2.26.162.45:8080')
    page.get_by_role('link', name='login').click()

    username = ''.join(random.choices(string.ascii_letters, k=8))
    password = ''.join(random.choices(string.ascii_letters, k=10))

    page.get_by_test_id('login-username').fill(username)
    page.get_by_test_id('login-password').fill(password)
    page.get_by_role('button').click()


    expect(page.get_by_test_id('login-submit-spinner')).to_be_visible()
    expect(page.get_by_test_id('login-submit-spinner')).to_be_hidden()
    expect(page.get_by_text('Invalid login or password.')).to_be_visible()