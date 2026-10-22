import re
from enum import StrEnum

from playwright.sync_api import Page


class SearchFilter(StrEnum):
    PRICE_ASC = 'price_asc'
    PRICE_DESC = 'price_desc'


class SearchResultsPage:
    def __init__(self, page: Page):
        self.page = page
        self.filter_selection = page.get_by_test_id('filter-sort')
        self.apply_button = page.get_by_test_id('apply-filters-button')
        self.prices = page.get_by_test_id(re.compile(r'search-result-price-\d+'))
        self.loader = page.get_by_test_id('results-loader-svg')

    def set_filter(self, filter_type: str):
        self.filter_selection.select_option(filter_type)
        self.apply_button.click()
        self.loader.wait_for(state='visible')
        self.loader.wait_for(state='hidden')

    def get_first_n_prices(self, n: int) -> list[int]:
        elements = self.prices.all()[:n]
        return [int(el.get_attribute('data-price') or '0') for el in elements]
