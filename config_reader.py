import json
from pathlib import Path


class ConfigReader:
    DEFAULT_CONFIG_PATH = 'config.json'

    _instances = {}

    def __new__(cls, filepath: str = DEFAULT_CONFIG_PATH):
        path = Path(filepath)
        if not path.is_absolute():
            path = Path(__file__).parent / path

        absolute_path = str(path.resolve())

        if absolute_path not in cls._instances:
            instance = super().__new__(cls)
            instance._load_config(absolute_path)
            cls._instances[absolute_path] = instance

        return cls._instances[absolute_path]

    def _load_config(self, absolute_filepath: str) -> None:
        with open(absolute_filepath, encoding='utf-8') as f:
            self._config = json.load(f)

    def get_base_url(self) -> str:
        return self._config['base_url']
