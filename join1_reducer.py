#!/usr/bin/python
# --------------------------------------------------------------------------
# Input of reducer: <Word, TCount> and <Word, Date DCount>
# Output of reducer: <Date Word, DCount Tcount>
# --------------------------------------------------------------------------
import sys
prev_word = ' ' #initialize previous word to blank string
months = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
dates_to_output = [] #empty list to hold dates (Date) for a given word
day_cnts_to_output = [] #empty list of day counts (Dcount) for a given word
line_cnt = 0 #count input lines
for line in sys.stdin:
    line_cnt = line_cnt + 1
    line = line.strip() #strip out carriage return (empty lines)
    key_value = line.split('\t')#split line, into key and value, returns a list
    curr_word = key_value[0] #key is first item in list, indexed by 0: <Word>
    value_in = key_value[1] #value is 2nd item: <TCount> or <Date DCount>
    #check whether have a new current word and not the first line
    if (curr_word != prev_word) and (line_cnt > 1):
        #write out the join result for previous word
        for i in range(len(dates_to_output)):
            print('{0} {1} {2} {3}'.format(dates_to_output[i],prev_word,day_cnts_to_output[i],curr_word_total_cnt))
        #after write out, rest the lists for current word
        dates_to_output = []
        day_cnts_to_output = []
    #store "date, daycount, and total count" of current word in the lists
    if value_in[0:3] in months:#if value is <Date DCount>
        date_day = value_in.split()
        dates_to_output.append(date_day[0]) #add date to the list
        day_cnts_to_output.append(date_day[1]) #add dayCount to the list
    else:#if value is <TCount>
        curr_word_total_cnt = value_in#record the totalCount
    #setup new previous word for the next set of input lines
    prev_word = curr_word
#--------------------------------------------------------------------------
#After iterating through all lines, write out the join result for last word
for i in range(len(dates_to_output)):
    print('{0} {1} {2} {3}'.format(dates_to_output[i],prev_word,
        day_cnts_to_output[i],curr_word_total_cnt))
