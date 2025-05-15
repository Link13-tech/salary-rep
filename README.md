
# Salary Report Generator

Скрипт для генерации отчётов по зарплатам сотрудников из CSV-файлов.

## 📦 Установка

1. Клонируйте репозиторий:
   ```bash
   git clone https://github.com/Link13-tech/salary-rep.git
   cd salary-rep
   ```

2. Создайте и активируйте виртуальное окружение:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/macOS
   venv\Scripts\activate     # Windows
   ```

3. Установите зависимости (если используете `requirements.txt`):
   ```bash
   pip install -r requirements.txt
   ```

> **⚠️ Зависимости:** только стандартная библиотека. Никаких внешних пакетов, кроме `pytest` для тестов и `pytest-cov` (если нужен отчёт покрытия).

## 🚀 Как использовать

Запуск генерации отчёта:
```bash
python main.py data/data1.csv data/data2.csv data/data3.csv --report payout
```

Можно указывать **абсолютные пути**:
```bash
python main.py C:\Users\You\Desktop\data1.csv --report payout
```

Или смешанные пути:
```bash
python main.py ./data/data1.csv D:/Отчеты/data2.csv --report payout
```

### Аргументы

- `data/*.csv` — путь(и) к CSV-файлам с данными сотрудников.
- `--report` — тип отчёта. Сейчас поддерживается:
  - `payout` — отчёт по зарплатам.

## 🧾 Пример формата отчёта (`payout`)

```
              name             hours   rate  payout
Dev
------------  Alice            100     50    $5000
------------  Bob              120     40    $4800
```

## 📁 Формат CSV

Файлы должны содержать данные с колонками:

- `name` — имя сотрудника
- `department` — отдел
- `hours_worked` — отработанные часы
- `hourly_rate` — ставка в час

Колонки могут отличаться по имени (например, `hours`, `rate`), но будут распознаны.

## ➕ Добавление нового отчёта

Чтобы добавить новый тип отчёта:

1. Создайте новый файл в папке `reports/`, например `salary.py`.
2. В нём определите класс с методом `generate(records: List[Dict]) -> str`.
3. Зарегистрируйте отчёт в `Reports`:

```python
# reports/reports.py

from reports.payout import PayoutReport
from reports.salary import SalaryReport  # <- ваш новый отчёт

class Reports:
    def __init__(self):
        self.available_reports = {
            "payout": PayoutReport(),
            "salary": SalaryReport(),  # <- добавляем
        }
```

## ✅ Тесты

Запуск всех тестов:
```bash
pytest -v
```

Покрытие:
```bash
pytest --cov=.
```

## 📂 Структура проекта

```
salary-rep/
├── data/
│   ├── data1.csv
│   ├── data2.csv
│   └── data3.csv
├── parsers/
│   ├── __init__.py
│   └── csv_parser.py
├── reports/
│   ├── __init__.py
│   ├── payout.py
│   └── reports.py
├── tests/
│   ├── __init__.py
│   ├── test_main_direct.py
│   ├── test_main_subprocess.py
│   ├── test_parser.py
│   └── test_report.py
├── .gitignore
├── main.py
└── README.md
```

## 👤 Автор

Link13-tech
