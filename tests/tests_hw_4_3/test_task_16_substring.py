from homework_4_3.task_16_substring import is_substring


def test_is_substring_literal():
    assert is_substring("Hello", "ell")


def test_is_substring_numeral():
    assert is_substring("123456789", "2345678")


def test_is_not_substring():
    assert not is_substring("Python", "ruby")
