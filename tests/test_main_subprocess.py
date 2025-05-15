import subprocess
import os


def test_main_script_runs():
    files = ["data/data1.csv", "data/data2.csv", "data/data3.csv"]
    for f in files:
        assert os.path.exists(f), f"Missing file: {f}"

    result = subprocess.run(
        ["python", "main.py"] + files + ["--report", "payout"],
        capture_output=True,
        text=True
    )
    print(result.stdout)

    assert result.returncode == 0
    assert "Design" in result.stdout
    assert "$" in result.stdout
