#!/usr/bin/python
# --------------------------------------------------------------------------
# Input of reducer: <Show, View> and <Show, ABC>
# Output of reducer: <Show, Total View>
# --------------------------------------------------------------------------
import sys
ABC_dict = {} # empty dictionary to hold "Show: Total View"
kvs = [] # empty list to hold "<Show, View/ABC>"
for line in sys.stdin:
    line = line.strip() # strip out carriage return (empty lines)
    key_value = line.split('\t') # split line, into key and value,
        # returns a list of <Show, ABC/View>
    if key_value[1] == 'ABC': # <Show, ABC>
        if (key_value[0] in ABC_dict) == False:
        # Initialize the total views for each new show
            ABC_dict.update({key_value[0]: 0})
    else: # <Show, View>
        kvs.append(key_value) # add "<Show, View>" to the list
# Add the views for each show in the dictionary
for key_value in kvs:
    if key_value[0] in ABC_dict:
        ABC_dict[key_value[0]] += int(key_value[1])
# Write out the LAST join result
for (key, value) in ABC_dict.items():
    print('%s %s' % (key, value))
