import pytest
from src.homework_4_3.task_20_brackets import is_valid


@pytest.mark.parametrize(
    "input_string",
    [
        "()",
        "[]",
        "{}",
        "(text) [123] {___} ({[]})",
        "({[(())]})",
        "(sdfds{[sdf]sdfsd})",
    ],
)
def test_is_valid(input_string):
    assert is_valid(input_string)


@pytest.mark.parametrize("input_string", ["({[]}", "(]", "(", "{", "]"])
def test_is_not_valid(input_string):
    assert not is_valid(input_string)
