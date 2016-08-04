#!/usr/bin/python

import sys

def error_message():
    print "-" * 10
    print "reverse_string.py STRING START(int) STOP(int)"
    exit(1)

def reversal(string, start, stop):
    output = ''
    stop_counter = stop
    i = 0
    while i < start - 1:
        output = output + string[i]
        i += 1
    while stop_counter >= start:
        output = output + string[stop_counter - 1]
        stop_counter -= 1
    while stop < len(string):
        output = output + string[stop]
        stop += 1
    return(output)

if len(sys.argv) < 4:
    print "Not enough arguments provided"
    error_message()

elif int(sys.argv[2]) > int(sys.argv[3]):
    print "STOP can't be before START"
    error_message()

elif int(sys.argv[2]) > len(sys.argv[1]) or int(sys.argv[3]) > len(sys.argv[1]):
   print "START or STOP not valid for length of string provided."
   error_message()
   
else:
    print "I guess we'll go on"
    input_string = sys.argv[1]
    reverse_start = int(sys.argv[2])
    reverse_stop = int(sys.argv[3])
    reversed = reversal(input_string, reverse_start, reverse_stop)
    print reversed
    exit(0)
