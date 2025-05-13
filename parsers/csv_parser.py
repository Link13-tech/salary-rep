from typing import List, Dict

RATE_KEYS = {"hourly_rate", "rate", "salary"}


def parse_employee_data(filepath: str) -> List[Dict]:
    with open(filepath, encoding="utf-8") as f:
        lines = f.read().splitlines()

    if not lines:
        return []

    headers = lines[0].split(",")
    data = [line.split(",") for line in lines[1:]]

    # Поиск нужных индексов
    try:
        name_idx = headers.index("name")
        dept_idx = headers.index("department")
        hours_idx = headers.index("hours_worked")
        rate_idx = next(i for i, h in enumerate(headers) if h in RATE_KEYS)
    except ValueError as e:
        raise ValueError(f"Missing required column in {filepath}: {e}")

    employees = []
    for row in data:
        employee = {
            "name": row[name_idx],
            "department": row[dept_idx],
            "hours_worked": float(row[hours_idx]),
            "hourly_rate": float(row[rate_idx]),
        }
        employees.append(employee)

    return employees
