- I have implemented TrieNode and Trie classes to handle insert words, find prefix, get  suffixes
    - in insert I create a child node for each character for the upper node
    - in find for each char in the prefix starting from root check exxisting of char in chieldren of the previous node
    - to get suffixes travel recursiverly inside the children and children of each chiled till find the leaf nodes, then append this suffix to the output list
- Time complexity:
    - Insert word O(n) where n is the number of the word's characters
    - find prefix O(n) where n is the number of the prefixes's characters
    - get node suffixes O(n * m) where
                                n: possible character count
                                m: average suffix length

- Space complexity is O(n * m) where
                n: possible character count
                m: average word length