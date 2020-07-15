- use binary search approache with a complex condition
    - in binary search with the normal sorted list, we go to left of mid if the target number is less than it, but in this case we have rotated sorted list, so in some times despite that the target numbre is less than the mid, but we  need to go right
    simple to decide to go left of mid we to satisfy this conditions
        (number < mid_value and start_value < mid_value and number >= start_value ) \
            or (number > mid_value and start_value > mid_value)
    other wise we will go right
- Time complexity is O(log n)
- Space complexity, it consume a space for start, mid, and end so the space complexity is fixed
    O(1)