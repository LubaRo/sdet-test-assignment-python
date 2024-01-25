# Системные требования
- python3.10
- pip3
- venv (опционально)

# Как запустить

В данном проекте явно указываем путь по `chromewebdriver`, не полагаясь на `PATH`.

1. `cp .env.example .env`
1. В файле .env для `PATH_TO_CROMEDRIVER` указываем реальный путь до `chromewebdriver`
1. Опционально: поднимаем виртуальную среду `python3.10 -m venv venv & source venv/bin/activate`
1. Устанавливаем пакеты `pip install -r requirements.txt`
1. Прогоняем тесты с помощью `make test` или командой `pytest tests`
