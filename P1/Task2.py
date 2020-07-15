"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""
# CReate a dictionary  of the {number, total time}
phone_time = {}
for call in calls:
    if call[0] in phone_time:
        phone_time[call[0]] += int(call[3])
    else:
        phone_time[call[0]] = int(call[3])

    if call[1] in phone_time:
        phone_time[call[1]] += int(call[3])
    else:
        phone_time[call[1]] = int(call[3])

# get the number that with the max time
max_number = None
max_time = 0
for number in phone_time.keys():
    if phone_time[number] > max_time:
        max_number = number
        max_time = phone_time[number]

print("{} spent the longest time, {} seconds, on the phone during September 2016.".format(
    max_number, max_time))
