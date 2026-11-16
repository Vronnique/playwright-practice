from __future__ import annotations

import json

from playwright.sync_api import Browser, BrowserContext, Page


class PageFactory:
    DEFAULT_IGNORE_HTTPS_ERRORS = True
    DEFAULT_TIMEOUT_MS = 10_000
    DEFAULT_NAVIGATION_TIMEOUT_MS = 15_000

    def __init__(self, browser: Browser, config: dict) -> None:
        self.browser = browser
        self.config = config

    @classmethod
    def from_json(cls, browser: Browser, file_path: str) -> PageFactory:
        with open(file_path, encoding="utf-8") as config_file:
            config = json.load(config_file)
        return cls(browser, config)

    def create_page(self) -> Page:
        context = self._create_context()
        page = context.new_page()
        page.set_default_timeout(self.config.get("default_timeout_ms", self.DEFAULT_TIMEOUT_MS))
        page.set_default_navigation_timeout(
            self.config.get(
                "navigation_timeout_ms",
                self.DEFAULT_NAVIGATION_TIMEOUT_MS,
            )
        )
        return page

    def _create_context(self) -> BrowserContext:
        return self.browser.new_context(
            base_url=self.config["base_url"],
            ignore_https_errors=self.config.get(
                "ignore_https_errors",
                self.DEFAULT_IGNORE_HTTPS_ERRORS,
            ),
        )
