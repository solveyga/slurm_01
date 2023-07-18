import pytest
from src.homework_4_3.task_16_substring import is_substring


@pytest.mark.parametrize(
    "string, substring",
    [("Hello", "ell"), ("123456789", "2345678"), ("fgjh)123", "h)1")],
)
def test_is_substring(string, substring):
    assert is_substring(string, substring)


def test_is_not_substring():
    assert not is_substring("Python", "ruby")
