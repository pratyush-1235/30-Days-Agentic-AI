"""Unit tests for Day 1 tools.py"""
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "code"))
from tools import calculator  # noqa: E402


def test_calculator_basic_addition():
    assert calculator("2 + 2") == "4"


def test_calculator_multiplication():
    assert calculator("6 * 7") == "42"


def test_calculator_division_by_zero():
    assert calculator("1 / 0") == "Error: division by zero"


def test_calculator_rejects_code_injection():
    result = calculator("__import__('os').system('ls')")
    assert result.startswith("Error")


def test_calculator_rejects_letters():
    result = calculator("2 + a")
    assert result.startswith("Error")


def test_calculator_handles_parentheses():
    assert calculator("(2 + 3) * 4") == "20"
