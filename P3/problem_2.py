def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    index = -1
    start = 0
    end = len(input_list) - 1
    while start <= end:
        mid = (start + end) // 2
        mid_value = input_list[mid]
        start_value = input_list[start]
        if number == mid_value:
            index = mid
            break
        
        if (number < mid_value and start_value < mid_value and number >= start_value ) \
            or (number > mid_value and start_value > mid_value):
            end = mid - 1
        else:
            start = mid + 1

    return index

def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1

def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")

test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])

test_function([[6, 7, 8, 9, 10, 1], 6])
test_function([[6, 7, 8, 9, 10, 1], 1])
test_function([[6, 7, 8, 9, 10, 1], 10])
test_function([[6, 7, 8, 9, 10, 1], 9])
test_function([[9], 9])
test_function([[], 9])