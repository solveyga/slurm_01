test_dist = {'key': [1, 2, 3], 'key2': {'key1': 56, 'key2': [1, 2, 3, 4, 5], 'key3': {'key1': 56, 'key2': []}}}


def to_string(dict_to_string):
    for key, value in dict_to_string.items():
        if isinstance(value, (int, float)):
            print(f'{key}: value={value}')
        elif isinstance(value, list):
            print(f'{key}: array={value}')
        else:
            print(f'{key}:')
            to_string(value)


to_string(test_dist)

