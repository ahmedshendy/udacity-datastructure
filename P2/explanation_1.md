I have used a dictionary object to utilize its high performance in setting and getting the keys and values

and to keep the history for accessing the cache keys, I have implemented a doubly-linked list to able to know which key is the oldest one with O(1)

the time complexity for set and get operations is O(1)
space complexity: O(n) it is the size of items in the cache