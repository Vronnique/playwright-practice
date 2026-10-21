from playwright.sync_api import Page

class MainPage:
    def __init__(self, page: Page):
        self.page = page
        self.search_input = page.get_by_test_id('search-input')
        self.search_button = page.get_by_test_id('search-button')

    def search(self, query: str) -> None:
        self.search_input.fill(query)
        self.search_button.click()