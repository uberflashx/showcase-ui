# Showcase UI Automation (Playwright + Pytest)
Учебный проект, цель которого - продемонстрировать навыки автоматизации UI-тестирования на Python с использованием
Playwright и Pytest. В проекте реализованы ключевые техники, применяемые при написании автотестов для web-приложений.
---
## Цели проекта
- Продемонстрировать практические навыки автоматизации UI-тестов.
- Отразить применение паттернов и подходов, изученных при прохождении курса по Playwright и Pytest.
- Создать базовый, но структурированный репозиторий для showcase-портфолио QA Automation Engineer.
---
## Технологический стек
- **Python 3.13.5**
- **Playwright 1.55**
- **Pytest**
- **Pytest-rerunfailures**
- **Git/GitHub**
- **Allure**
---
## Структура проекта
* `showcase-ui/`
  * `fixtures/` # Фикстуры, вынесенные в плагины
    * `browsers.py`
  * `tests/` # Тестовые сценарии
    * `test_authorization.py`
    * `...`
  * `browser-state.json` # Файл для хранения storage state
  * `conftest.py` # Указание пути к pytest plugins
  * `pytest.ini` # Правила нейминга для тестов и кастомные маркировки
  * `requirements.txt` # Зависимости проекта
  * `README.md` # Этот файл
---
## Конфигурация
Проект использует Pydantic Settings для управления конфигурациями.
Все чувствительные данные и специфичные для окружений значения хранятся в .env файле.

Пример:
```
APP_URL="https://test.shop.com"
HEADLESS=false
BROWSERS=["chromium"]

TEST_USER.EMAIL="test@example.com"
TEST_USER.USERNAME="JohnD"
TEST_USER.PASSWORD="pass123"
```
---
## Allure-отчеты
В проект добавлен Allure-репортинг с кастомными шагами, тайтлами, разбивкой по Epic/Feature/Story, а также добавлена возможность прикладывания Playwright Traces к отчетам.

---
## Установка и запуск
### Установка зависимостей
`pip3 install -r requirements.txt`
### Установка браузеров
`playwright install`
### Запуск тестов с сохранением данных для Allure-отчета
`python -m pytest -s -v -k "test_cart" --alluredir=./allure-results` # Запуск по имени теста

`python -m pytest -s -v -m smoke --alluredir=./allure-results` # Запуск по имени кастомной маркировки
### Открытие отчета в браузере
`allure serve ./allure-results`