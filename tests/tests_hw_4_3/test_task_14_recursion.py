from src.homework_4_3.task_14_recursion import to_string


def test_array():
    assert (
        to_string(
            {
                "key": [1, 2, 3],
                "key2": {
                    "key1": 56,
                    "key2": [1, 2, 3, 4, 5],
                    "key3": {"key1": 56, "key2": []},
                },
            }
        )
        == "\nkey: array=[1, 2, 3]\nkey2: \n  key1: value=56"
        + "\n  key2: array=[1, 2, 3, 4, 5]"
        + "\n  key3: \n    key1: value=56\n    key2: array=[]"
    )
