def my_range(stop_value: float, start_value=0.0, step_value=1.0):
    if stop_value == start_value:
        my_list = []
    else:
        current_element = start_value
        my_list = [current_element]
        steps_count = int((stop_value - start_value) / step_value) - 1
        for i in range(steps_count):
            current_element += step_value
            my_list.append(current_element)

    return my_list
