from reports.payout import PayoutReport


def test_generate_payout_report_output_format():
    employees = [
        {"name": "Alice", "department": "Dev", "hours_worked": 100, "hourly_rate": 50},
        {"name": "Bob", "department": "Dev", "hours_worked": 120, "hourly_rate": 40},
    ]
    report = PayoutReport()
    output = report.generate(employees)
    assert "Alice" in output
    assert "Bob" in output
    assert "Dev" in output
    assert "$5000" in output
    assert "$4800" in output
