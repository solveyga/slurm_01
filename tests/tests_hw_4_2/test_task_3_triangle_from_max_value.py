def test_triangle_from_max_value():
    def triangle_from_max_value(users_number):
        max_value = 1
        result = ""
        for i in range(1, users_number + 1):
            max_value = max_value + i

        for i in range(users_number):
            for j in range(i + 1):
                max_value = max_value - 1
                result += str(max_value) + " "
            result += "\n"
        return result

    assert triangle_from_max_value(4) == "10 \n9 8 \n7 6 5 \n4 3 2 1 \n"
