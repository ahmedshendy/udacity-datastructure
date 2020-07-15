def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    if len(input_list) <= 2:
        return input_list
    sorted_input = mergsort(input_list)
    num1 = []
    num2 = []
    for i in range(0, len(sorted_input), 2):
        num1.append(str(sorted_input[i]))
        if i + 1 < len(sorted_input):
            num2.append(str(sorted_input[i + 1]))
    return [int(''.join(num1)), int(''.join(num2))]

def mergsort(input_list):
    input_len = len(input_list)
    if input_len <= 1:
        return input_list
    mid = input_len // 2
    left = input_list[:mid]
    right = input_list[mid:]

    left = mergsort(left)
    right = mergsort(right)

    return merge(left, right)

def merge(left, right):
    merged = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] > right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1
    merged.extend(left[left_index:])
    merged.extend(right[right_index:])

    return merged


print(rearrange_digits([]))
print(rearrange_digits([0]))
print(rearrange_digits([0,1]))
print(rearrange_digits([1,2]))
print(rearrange_digits([1,2,3]))
print(rearrange_digits([1, 2, 3, 4, 5]))
def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")

test_function([[1, 2, 3, 4, 5], [542, 31]])
test_case = [[4, 6, 2, 5, 9, 8], [964, 852]]
test_function(test_case)