import Lab3

print("Test_Lab3")


def test_bubble_sort_ascending():
    result = []
    input_arr = [64, 34, 25, 12, 22, 11, 90]
    test_arr = [11, 12, 22, 25, 34, 64, 90]

    result = Lab3.bubble_sort(input_arr, Lab3.SORT_ASCENDING)

    assert (result == test_arr)

def test_bubble_sort_descending():
    result = []
    input_arr = [64, 34, 25, 12, 22, 11, 90]
    test_arr = [90, 64, 34, 25, 22, 12, 11]

    result = Lab3.bubble_sort(input_arr, Lab3.SORT_DESCENDING)

    assert (result == test_arr)

def test_bubble_sort_invalid():
    result = []
    input_arr = [64, 34, 25, 12, 22, 11, 90]

    result = Lab3.bubble_sort(input_arr, 3)

    assert (result == [])

def bubble_sort(numbers, order_type):
    # REQ-04: Check if the list is empty
    if len(numbers) == 0:
        return 0

    # REQ-05: Check if all values are integers
    if not all(isinstance(num, int) for num in numbers):
        return 2

    # REQ-03: If 10 or more numbers are entered, return 1
    if len(numbers) >= 10:
        return 1

    # REQ-01 and REQ-02: Sort the numbers in ascending or descending order
    if order_type == "SORT_ASCENDING":
        for i in range(len(numbers)):
            for j in range(0, len(numbers) - i - 1):
                if numbers[j] > numbers[j + 1]:
                    numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
        return numbers

    elif order_type == "SORT_DESCENDING":
        for i in range(len(numbers)):
            for j in range(0, len(numbers) - i - 1):
                if numbers[j] < numbers[j + 1]:
                    numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
        return numbers

    # Default case if order_type is not recognized
    return None
