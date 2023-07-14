from homework_4_3.task_18_to_snake_case import to_snake_case


def test_three_words():
    assert to_snake_case('V for Vendetta') == 'v_for_vendetta'
