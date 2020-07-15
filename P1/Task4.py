"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

# make dict for text senders, receivers, and call receivers
# loop over the call senders if not in this dict, then add it to the telemarketers list

numbers_dict = {}
for text in texts:
    numbers_dict[text[0]] = 1
    numbers_dict[text[1]] = 1
for call in calls:
    numbers_dict[call[1]] = 1

telemarketers = {}

for call in calls:
    if call[0] not in numbers_dict:
        telemarketers[call[0]] = 1


print("These numbers could be telemarketers: ")
for number in sorted(telemarketers.keys()):
    print(number)
