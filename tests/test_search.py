import pytest
from playwright.sync_api import Page

from config_reader import ConfigReader
from pages.main_page import MainPage
from pages.search_results_page import SearchResultsPage, SearchFilter

config = ConfigReader()
URL = config.get_base_url()


@pytest.mark.parametrize(
    "name, n, filter_type",
    [
        ('city', 10, SearchFilter.PRICE_ASC),
        ('city', 15, SearchFilter.PRICE_DESC),
        ('habits', 10, SearchFilter.PRICE_ASC),
        ('habits', 15, SearchFilter.PRICE_DESC),
    ],
)
def test_search_with_filter(page: Page, name, n, filter_type) -> None:
    page.goto(URL)

    main_page = MainPage(page)
    main_page.search(name)

    search_results_page = SearchResultsPage(page)
    search_results_page.set_filter(filter_type)

    actual_prices = search_results_page.get_first_n_prices(n)

    # Проверка 1: количество полученных цен соответствует n
    assert len(actual_prices) == n, f'Ожидали {n} первых цен статей, фактически {len(actual_prices)}'

    # Проверка 2: порядок цен соответствует фильтру
    if filter_type == SearchFilter.PRICE_ASC:
        expected = sorted(actual_prices)
        direction = 'Price: low to high'
    elif filter_type == SearchFilter.PRICE_DESC:
        expected = sorted(actual_prices, reverse=True)
        direction = 'Price: high to low'
    else:
        pytest.fail(f'Неизвестный фильтр: {filter_type}')

    assert actual_prices == expected, (
        f'Цены не отсортированы в соответствии с фильтром: {direction}. '
        f'Ожидали: {expected}, фактически: {actual_prices}'
    )
