#!/usr/bin/python

# Inputs: find_proc_count.py hostname-preamble range_start range_stop process
#                                                                           count
# Example find_proc_count.py webhost 1 1000 httpd 5

import commands
import sys 
import socket

hostname_pre = sys.argv[1]
hostrange_start = int(sys.argv[2])
hostrange_stop = int(sys.argv[3])
process = sys.argv[4]
process_count = int(sys.argv[5])

def check_host_for_process(host_to_check, process_to_check):
    command_to_run = "ssh %s \'pgrep %s | wc -l\'" % (host_to_check,
        process_to_check)
    output_count = int(commands.getoutput(command_to_run))
    return(output_count)

def make_dict_of_hosts(mydict, hostpre, start, stop):
    for i in range(start, stop+1):
        if i < 10:
            padded_hostnumber = "0000%s" % i
        elif i >= 10 and i < 100:
            padded_hostnumber = "000%s" % i
        elif i >= 100 and i < 1000:
            padded_hostnumber = "00%s" % i
        elif i >= 1000 and i < 10000:
            padded_hostnumber = "0%s" % i 
        elif i == 10000:
           padded_hostnumber = "%s" % i
        current_hostname = hostpre + padded_hostnumber
        try: 
            socket.gethostbyname("current_hostname")
            current_process_count = check_host_for_process(current_hostname, process)
            if current_process_count != process_count:
                mydict[current_hostname] = current_process_count
        except socket.gaierror:
            print "%s is not a valid hostname." % current_hostname
    return(mydict)

results_dict = {}
results_dict = make_dict_of_hosts(results_dict, hostname_pre, hostrange_start, hostrange_stop)

#print "Results Dictionary is %s long" % results_dict.__len__()
print results_dict
