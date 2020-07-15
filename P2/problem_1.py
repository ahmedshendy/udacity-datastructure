class DoubleNode:
    def __init__(self, key, value):
        self.value = value
        self.key = key
        self.next = None
        self.previous = None

class DoublyLinkedList:
    def __init__(self, capacity):
        self.head = None
        self.tail = None
        self.capacity = capacity
        self.num_of_items = 0
    
    def append_head(self, new_head):
        if self.num_of_items >= self.capacity:
            self.handle_over_capacity()

        self.num_of_items += 1
        if self.head is None:
            self.head = new_head
            self.tail = self.head
            return
        
        if self.tail == self.head: #so this is the second element that will be added to the list
            self.tail.previous = new_head
        new_head.next = self.head
        self.head.previous = new_head
        self.head = new_head
        
        return

    def move_node_to_head(self, node):
        if node == self.head:
            return
        if node == self.tail:
            self.tail = node.previous
            self.tail.next = None
        else:
            node.next.previous = node.previous
            node.previous.next = node.next
        self.head.previous = node
        node.next = self.head
        node.previous = None
        self.head = node
        pass

    def handle_over_capacity(self):
        self.capacity -+ 1
        if self.tail == self.head:
            self.tail = self.head = None
        else:
            self.tail = self.tail.previous
            self.tail.next = None


class LRU_Cache(object):
    
    def __init__(self, capacity):
        # Initialize class variables
        self.capacity = capacity
        self.visiting_history = DoublyLinkedList(capacity)
        self.cach_dict = {}
        self.cash_size = 0
        pass

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent.
        if key not in self.cach_dict:
            return -1
        node = self.cach_dict[key]
        self.visiting_history.move_node_to_head(node)
        return node.value

    def set(self, key, value):
        if self.capacity < 1:
            print("The capacity is 0")
            return
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item. 
        cached_value = self.get(key)
        if cached_value == value:
            return
        elif cached_value != -1 and cached_value != value:
            self.cach_dict[key].value = value
            return
            
        node = DoubleNode(key, value)
        if self.cash_size < self.capacity:
            self.cash_size += 1
        else:
            # evict the tail
            evected_node = self.visiting_history.tail
            self.cach_dict.pop(evected_node.key)
        self.visiting_history.append_head(node)
        self.cach_dict[key] = node

        pass

our_cache = LRU_Cache(5)

our_cache.set(1, 1);
our_cache.set(2, 2);
our_cache.set(3, 3);
our_cache.set(4, 4);


print(our_cache.get(1))       # returns 1
print(our_cache.get(2))       # returns 2
print(our_cache.get(9))      # returns -1 because 9 is not present in the cache

our_cache.set(5, 5) 
our_cache.set(6, 6)

print(our_cache.get(3))      # returns -1 because the cache reached it's capacity and 3 was the least recently used entry

our_cache = LRU_Cache(0)

our_cache.set(1, 1);
# The capacity is 0

our_cache = LRU_Cache(1)
print(our_cache.get('A'))
# returns -1
our_cache.set('A', 10)
our_cache.set('B', 20)
print(our_cache.get('B'))
# returns 20


our_cache = LRU_Cache(5)
our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(3, 3)
our_cache.set(4, 4)
print(our_cache.get(1))  # returns 1
print(our_cache.get(2))  # returns 2
print(our_cache.get(9))  # returns -1
our_cache.set(5, 5)
our_cache.set(6, 6)
print(our_cache.get(3))  # returns -1 because key 3 was thrown out
our_cache.set(7, 7)
print(our_cache.get(4))  # 4 is thrown out