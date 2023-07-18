def test_triangle():
    def triangle(users_number):
        printed_number = 0
        result = ""

        for i in range(users_number):
            for j in range(i + 1):
                printed_number += 1
                result += str(printed_number) + " "
            result += "\n"
        return result

    assert triangle(4) == "1 \n2 3 \n4 5 6 \n7 8 9 10 \n"
