def is_valid(value: str):
    open_round_brackets_count = value.count('(')
    close_round_brackets_count = value.count(')')
    if open_round_brackets_count != close_round_brackets_count:
        return False

    open_square_brackets_count = value.count('[')
    close_square_brackets_count = value.count(']')
    if open_square_brackets_count != close_square_brackets_count:
        return False

    open_curly_brackets_count = value.count('{')
    close_curly_brackets_count = value.count('}')
    if open_curly_brackets_count != close_curly_brackets_count:
        return False

    return True


