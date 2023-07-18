from src.homework_4_3.task_1_def_my_range import my_range


def test_not_empty_list():
    assert my_range(5.0) == [0.0, 1.0, 2.0, 3.0, 4.0]


def test_start_eqv_stop():
    assert my_range(0.0) == []


def test_custom_boundaries():
    assert my_range(2, -1, 0.5) == [-1, -0.5, 0.0, 0.5, 1.0, 1.5]
