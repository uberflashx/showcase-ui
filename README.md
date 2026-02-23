# E-commerce UI automation framework (Playwright + Pytest)

## Технологический стек
- **Python 3.13.5**
- **Playwright 1.55**
- **Pytest**
- **Git/GitHub**
- **Allure**

## Структура проекта
```
.
├── .github/
│   └── workflows/    # GitHub Actions workflows
│       └── ...
├── components/   # Описанные через Page Component компоненты
│   ├── authentication/
│   │   └── ...
│   └── ...
├── fixtures/   # Фикстуры, вынесенные в плагины
│   └── ...
├── pages/    # Описанные через POM страницы проекта
│   └── ...
├── prompts/    # Промпты для AI-ревью
│   └── ...
├── tests/    # Тестовые сценарии
│   └── ...
├── tools/    # Дополнительные тулы для работы с Allure-отчетами
│   ├── allure/
│   │   └── ...
│   └── playwright/
│       └── ...
├── .ai-review.yaml
├── .env
├── .gitignore
├── config.py   # Конфигураци проекта через Pydantic Settings
├── conftest.py   # Указание пути к pytest plugins
├── pytest.ini    # Правила нейминга для тестов и кастомные маркировки
├── README.md   # Этот файл
└── requirements.txt    # Зависимости проекта
```

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

## Allure-отчеты
В проект добавлен Allure-репортинг с кастомными шагами, тайтлами, разбивкой по Epic/Feature/Story, а также добавлена возможность прикладывания Playwright Traces к отчетам.


## Установка и запуск
### Установка зависимостей
`pip3 install -r requirements.txt`

### Установка браузеров
`playwright install`

### Запуск тестов с сохранением данных для Allure-отчета
`python -m pytest -s -v -k "test_cart" --alluredir=./allure-results` # Запуск по имени теста

`python -m pytest -s -v -m "regression" --alluredir=./allure-results` # Запуск по имени кастомной маркировки

### Параллельный запуск тестов с иcпользованием pytest-xdist
`python -m pytest -s -v -m "regression" -numprocesses auto` # Вместо значения auto можно указать вручную количество потоков

### Открытие отчета в браузере
`allure serve ./allure-results`


## CI/CD
Автоматизированный запуск тестов настроен через **GitHub Actions** с триггерами по событиям push и pull request в ветку **main**. Allure-отчеты автоматически публикуются на **GitHub Pages** с сохранением истории запусков.