import re

import pytest
from playwright.sync_api import Page

from config_reader import ConfigReader
from pages.main_page import MainPage
from pages.search_results_page import SearchResultsPage

config = ConfigReader()
URL = config.get_base_url()
SEARCH_CASES = config.get_search_cases()


def parse_prices(texts: list[str]) -> list[int]:
    return [int(re.sub(r"[^\d.]", "", t)) for t in texts]


@pytest.mark.parametrize(
    "case",
    SEARCH_CASES,
    ids=lambda c: f"{c['name']}-{c['n']}-{c['filter_type']}",
)
def test_search_with_filter(page: Page, case: dict) -> None:
    name = case['name']
    n = case['n']
    filter_type = case['filter_type']

    page.goto(URL)

    main_page = MainPage(page)
    main_page.search(name)

    search_results_page = SearchResultsPage(page)
    search_results_page.set_filter(filter_type)

    actual_texts = search_results_page.get_first_n_prices(n)
    actual_prices = parse_prices(actual_texts)

    # Проверка 1: количество полученных цен соответствует n
    assert len(actual_prices) == n, f"Ожидали {n} первых цен статей, фактически {len(actual_prices)}"

    # Проверка 2: порядок цен соответствует фильтру
    if filter_type == "price_asc":
        expected = sorted(actual_prices)
        direction = "Price: low to high"
    elif filter_type == "price_desc":
        expected = sorted(actual_prices, reverse=True)
        direction = "Price: high to low"
    else:
        pytest.skip(f"Неизвестный filter_type: {filter_type}")

    assert actual_prices == expected, (
        f"Цены не отсортированы в соответствии с фильтром: {direction}. "
        f"Ожидали: {expected}, фактически: {actual_prices}"
    )
