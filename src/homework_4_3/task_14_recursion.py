def to_string(value, indent=0):
    result = []
    if isinstance(value, dict):
        for key, value in value.items():
            row = f'\n{" " * indent}{key}: {to_string(value, indent + 2)}'
            result.append(row)
    elif isinstance(value, list):
        result.append(f"array={value}")
    else:
        result.append(f"value={value}")
    return "".join(result)
