import sys
import heapq


class Node:
    def __init__(self, character, frequency):
        self.character = character
        self.frequency = frequency
        self.bit_code = None
        self.left_child = None
        self.right_child = None


    def __lt__(self, other):
        return self.frequency < other.frequency

def huffman_encoding(data):
    if data == None or len(data) < 1:
        print("Invalid input")
        return '', None
    # Phase I - Build the Huffman Tree
    #   First, determine the frequency of each character in the message.
    chars_freq = {}
    for char in data:
        chars_freq[char] = chars_freq.get(char, 0) + 1
    # represent each char freq as a node, and push it to a priority queue
    help_queue = []
    for char, freq in chars_freq.items():
        node = Node(char, freq)
        heapq.heappush(help_queue, (freq, node))
    head = None
    while len(help_queue) > 0:
        # Pop-out two nodes with the minimum frequency from the priority queue created in the above step
        char_item1 = heapq.heappop(help_queue)
        if len(help_queue) == 0:
            head = char_item1[1]
            continue
        char_item2 = heapq.heappop(help_queue)
        # Create a new node with a frequency equal to the sum of the two nodes picked in the above step
        node = Node("", char_item1[0] + char_item2[0])
        if char_item2[0] < char_item1[0]:
            node.left_child = char_item2[1]
            node.right_child = char_item1[1]
        else:
            node.left_child = char_item1[1]
            node.right_child = char_item2[1]
        node.left_child.bit_code = '0'
        node.right_child.bit_code = '1'
        heapq.heappush(help_queue, (node.frequency, node))
    # handle the case of tree with only head by adding a dumy head and make the old head as left node
    if head.left_child == None and head.right_child == None:
        node = Node("", head.frequency)
        node.left_child = head
        head = node
        node.left_child.bit_code = '0'

    huffman_code_table = {}

    def get_code(node, code):

        if node == None:
            return
        if node.bit_code != None:
            code = code + node.bit_code
        if len(node.character) > 0:
            huffman_code_table[node.character] = code
            return
        get_code(node.left_child, code)
        get_code(node.right_child, code)
        return
    get_code(head, '')

    encoded_data = ''
    for char in data:
        encoded_data += huffman_code_table[char]
    return encoded_data, head


def huffman_decoding(data, tree_head):
    # Declare a blank decoded string
    decoded_string = ''
    node = tree_head
    for bit in data:
        # Pick a bit from the encoded data, traversing from left to right
        # Start traversing the Huffman tree from the root
        
        if bit == '0':
            # If the current bit of encoded data is 0, move to the left child
            node = node.left_child
        else:
            # else move to the right child of the tree if the current bit is 1
            node = node.right_child
        if node.left_child == None and node.right_child == None:
            # f a leaf node is encountered, append the (alphabetical) character of the leaf node to the decoded string
            decoded_string += node.character
            node = tree_head
        
    return decoded_string


def test_huffman(str_input):
    codes = {}

    a_great_sentence = str_input

    print("The size of the data is: {}\n".format(
        sys.getsizeof(a_great_sentence)))
    print("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree_head = huffman_encoding(a_great_sentence)

    if tree_head:
        print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
        print ("The content of the encoded data is: {}\n".format(encoded_data))

        decoded_data = huffman_decoding(encoded_data, tree_head)

        print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
        print ("The content of the encoded data is: {}\n".format(decoded_data))

test_huffman('')
# Invalid input
test_huffman(None)
# Invalid input

test_huffman('A')
# print the decoded_data
# A
test_huffman('AA')
# print the decoded_data
# AA

test_huffman('AB')
# print the decoded_data
# AB


test_huffman('Greenwich Mean Time (GMT) is the mean solar time at the Royal Observatory in Greenwich, London, reckoned from midnight. At different times in the past, it has been calculated in different ways, including being calculated from noon;[1] as a consequence, it cannot be used to specify a precise time unless a context is given.')
# print the decoded_data
# Greenwich Mean Time (GMT) is the mean solar time at the Royal Observatory in Greenwich, London, reckoned from midnight. At different times in the past, it has been calculated in different ways, including being calculated from noon;[1] as a consequence, it cannot be used to specify a precise time unless a context is given.


test_huffman("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUV")