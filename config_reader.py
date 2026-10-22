import json
from pathlib import Path


class ConfigReader:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._load_config()
        return cls._instance

    def _load_config(self) -> None:
        config_path = Path(__file__).parent / 'config.json'
        with open(config_path, encoding="utf-8") as f:
            self._config = json.load(f)

    def get_base_url(self) -> str:
        return self._config['base_url']

    def get_search_cases(self) -> list[dict]:
        return self._config['search_cases']
