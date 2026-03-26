# Денб 2: Python основы для Data Engineer

## Опсиание
Первый ETL-пайплайн с использованием pandas, логированием и конфигурацией.

## Стек
- Python 3.10+
- pandas
- python-dotenv
- logging

## Запуск

```powershell
# 1. Активировать venv
powershell -ExecutionPolicy Bypass -File venv\Scripts\activate.ps1

# 2. Установить зависимости
pip install -r requirements.txt

# 3. Запустить пайплайн
cd src
pyrhon main.py