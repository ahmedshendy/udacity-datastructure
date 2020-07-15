def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    max_num = None
    min_num = None
    for num in ints:
        if max_num == None or num > max_num:
            max_num = num
        if min_num == None or num < min_num:
            min_num = num
    return(min_num, max_num)

## Example Test Case of Ten Integers
import random

l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)

print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail")
print ("Pass" if ((None, None) == get_min_max([])) else "Fail")
print ("Pass" if ((0, 0) == get_min_max([0])) else "Fail")