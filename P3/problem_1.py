def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    if number < 0:
        print('Invalid input')
        return None
    # use binary search approache
    
    start = 0
    end = number
    while start <= end:
        mid = (start + end) // 2
        if (mid + 1) * (mid + 1) > number and mid * mid <= number:
            break
        if mid * mid > number:
            end = mid -1
        else:
            start = mid + 1

    return mid

print ("Pass" if  (None == sqrt(-9)) else "Fail")
print ("Pass" if  (3 == sqrt(9)) else "Fail")
print ("Pass" if  (0 == sqrt(0)) else "Fail")
print ("Pass" if  (4 == sqrt(16)) else "Fail")
print ("Pass" if  (1 == sqrt(1)) else "Fail")
print ("Pass" if  (5 == sqrt(27)) else "Fail")
print ("Pass" if  (2236 == sqrt(5000000)) else "Fail")