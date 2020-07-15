- I have implemented RouteTrieNode and RouteTrie classes to handle insert and find routes
    - in insert I separate the path by "/", then isert each part as chiled node for its previeus part
    - in find I separate the path by "/", then starting from root check exxisting of each part in the chieldren of the previous node
- Time complexity:
    - add handler O(n) where n is the number of path's parts
    - lookup O(1), because getting value with key from dict is a constatnt time complexity
- Space complexity is O(n * m) where
                n: possible route path parts
                m: number of routes