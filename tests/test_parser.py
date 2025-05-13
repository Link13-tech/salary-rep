import tempfile
from parsers.csv_parser import parse_employee_data


def test_parse_employee_data_handles_different_rate_fields():
    csv_variants = [
        ("hourly_rate", "50"),
        ("rate", "60"),
        ("salary", "70")
    ]

    for rate_key, rate_value in csv_variants:
        content = (
            f"id,email,name,department,hours_worked,{rate_key}\n"
            f"1,test@example.com,Test User,QA,100,{rate_value}\n"
        )
        with tempfile.NamedTemporaryFile(mode="w+", suffix=".csv", delete=False) as f:
            f.write(content)
            f.seek(0)
            result = parse_employee_data(f.name)
            assert len(result) == 1
            assert result[0]["name"] == "Test User"
            assert result[0]["hourly_rate"] == float(rate_value)
            assert result[0]["hours_worked"] == 100.0
