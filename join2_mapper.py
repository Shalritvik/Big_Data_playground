#!/usr/bin/python
# Input of mapper: <Show, View> and <Show, Channel> files
# Output of mapper: Show is the key, View/ABC is value
# --------------------------------------------------------------------------
import sys
for line in sys.stdin:
    line = line.strip()# strip out carriage return (empty lines)
    key_value = line.split(',')# split line, into key and value, returns a list
    if len(key_value)>1:
        key_in = key_value[0]
        value_in = key_value[1]
#Decide whether value is view (number) or channel (string)
        testNum = [int(s) for s in value_in.split() if s.isdigit()]
        if len(testNum) > 0:
            print('%s\t%s' % (key_in, value_in))
        else:
            if value_in == 'ABC': #remove all shows not on ABC
                print('%s\t%s' % (key_in, value_in))
# Note that Hadoop expects a tab to separate key value
# but this program assumes the input file has a ',' separating key value
