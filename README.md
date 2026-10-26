# Playwright Practice

Практика написания автотестов на Python с использованием pytest и Playwright.

## Стек

- Python
- pytest
- Playwright

## Установка

pip install -r requirements.txt
playwright install

## Запуск

pytest
pytest --headed

## Структура проекта

- `pages/` — Page Object-классы страниц
- `tests/` — тесты
- `config.json` — конфигурация (URL стенда, тестовые данные)
- `config_reader.py` — класс для чтения конфига (Singleton)
- `conftest.py` — корень проекта для корректных импортов