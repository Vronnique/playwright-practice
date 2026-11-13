from pathlib import Path

import pytest
from playwright.sync_api import Browser, Page

from framework.page_factory import PageFactory
from logger import setup_logger


@pytest.fixture(scope="session", autouse=True)
def init_logger():
    setup_logger()

@pytest.fixture
def page(browser: Browser) -> Page:
    config_path = Path(__file__).parent.parent / "framework" / "browser_config.json"
    factory = PageFactory.from_json(browser, str(config_path))
    return factory.create_page()