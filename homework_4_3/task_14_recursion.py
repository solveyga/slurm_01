def to_string(dict_to_string):
    for key, value in dict_to_string.items():
        if isinstance(value, (int, float)):
            print(f"{key}: value={value}")
        elif isinstance(value, list):
            print(f"{key}: array={value}")
        else:
            print(f"{key}:")
            to_string(value)
