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
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."

"""
# add the distincet numbers to a new dict
distincit_dict = {}
for text in texts:
    distincit_dict[text[0]] = 1
    distincit_dict[text[1]] = 1
for call in calls:
    distincit_dict[call[0]] = 1
    distincit_dict[call[1]] = 1

print("There are {} different telephone numbers in the records.".format(
    len(distincit_dict)))
