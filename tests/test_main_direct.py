import sys
import pytest

from main import main


def test_main_runs(monkeypatch):
    monkeypatch.setattr(sys, 'argv', [
        "main.py",
        "data/data1.csv",
        "data/data2.csv",
        "data/data3.csv",
        "--report", "payout"
    ])
    try:
        main()
    except SystemExit:
        pass


def test_main_with_invalid_report(monkeypatch):
    monkeypatch.setattr(sys, 'argv', [
        "main.py",
        "data/data1.csv",
        "--report", "unknown"
    ])
    with pytest.raises(SystemExit) as e:
        main()
    assert e.value.code == 1


def test_main_without_args(monkeypatch):
    monkeypatch.setattr(sys, 'argv', ["main.py"])
    with pytest.raises(SystemExit):
        main()
