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
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""
# loop over calls
#   if caller is fixed line with area code 080 for Banglure
#     then add the codes to a new list
# extract from this list a sorted distinct list
# from this list count the Baglure area code and get the percentage of this cout of the total number of the list

bangalore_calls_codes = {}
total_calls = 0
for call in calls:
    if call[0].startswith("(080)"):
        total_calls += 1
        area_code = ""
        if call[1].startswith("140"):
            area_code = "140"
        elif call[1].startswith("("):
            area_code = call[1].split(")")[0][1:]
        else:
            area_code = call[1].split(" ")[0][:4]
        if area_code in bangalore_calls_codes:
            bangalore_calls_codes[area_code] += 1
        else:
            bangalore_calls_codes[area_code] = 1

print("The numbers called by people in Bangalore have codes: ")
for code in sorted(bangalore_calls_codes.keys()):
    print(code)

bangalore_calls_percentage = 100 * bangalore_calls_codes["080"] / total_calls
print("{} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.".format(
    "%.2f" % bangalore_calls_percentage))
