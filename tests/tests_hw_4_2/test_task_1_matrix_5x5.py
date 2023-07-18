def test_5x5_matrix():
    def matrix():
        result = ""
        for i in range(1, 26):
            if i % 5 == 0:
                result = result + str(i) + "\n"
            else:
                result = result + str(i) + " "
        print(result)
        return result

    assert (
        matrix()
        == "1 2 3 4 5\n6 7 8 9 10\n11 12 13 14 15"
        + "\n16 17 18 19 20\n21 22 23 24 25\n"
    )
