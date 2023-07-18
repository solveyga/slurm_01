from src.homework_4_3.task_18_to_snake_case import to_snake_case
import pytest


@pytest.mark.parametrize(
    "input_string, expected",
    [
        ("V for Vendetta", "v_for_vendetta"),
        ("Some text", "some_text"),
        ("Horizon zero dawn", "horizon_zero_dawn"),
    ],
)
def test_three_words(input_string, expected):
    assert to_snake_case(input_string) == expected
