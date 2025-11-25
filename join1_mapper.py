
#!/usr/bin/python
#
# Input of mapper: <Word, TCount> and <Date Word, DCount> files
# Output of mapper: Word is the key, (TCount) or (Date DCount) is value
#

import sys
for line in sys.stdin:
    line = line.strip() #strip out carriage return (empty lines)
    key_value = line.split(',') #split line, into key and value, returns a list
        #<Word, TCount> or <Date Word, DCount>
    key_in = key_value[0].split(' ') #key is first item in list:
    #(Word) or (Date, Word)
    value_in = key_value[1] #value is 2nd item: (Tcount) or (DCount)

    if len(key_in) == 1:#key is only <Word>, just pass it through
        print('%s\t%s' % (key_in[0], value_in) )#print a string, tab, and string
    elif len(key_in) == 2:#if key has <Date, Word>
        date = key_in[0]#get "Date" from key field
        word = key_in[1]#get "Word" from key field
        value_out = date + ' ' + value_in #concatenate "Date, blank, and DCount"
        print('%s\t%s' % (word, value_out) ) #print a string, tab, and string

# Note that Hadoop expects a tab to separate key value
# but this program assumes the input file has a ',' separating key value