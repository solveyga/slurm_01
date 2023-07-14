def to_snake_case(value: str) -> str:
    return  '_'.join(value.lower().split())