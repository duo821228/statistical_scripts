#!/usr/bin/python

# Writer: Andrew
# Description: This file produces statistical result of experimental file. 
#              Calculate the task entry and task sent jitter.
#			   From the user input (filename.txt, period), this provides 
#			   mean, min, max, mode, median, stdev values to the text file.  
#			   input file must be saved in ns scale.
# CAUTION: It is running with python 3.4.X. 
#		   This file uses the python statistics module that is recently added.
#
# Usage: python3.4 ./stat_cal.py ./<your_data> task_period(ns)
#											  
# TODO: 
#      - Parsing the text files(.txt) in the directory, 
#	  	 and determine the its task_period.
#      - merge with trans2hist.py

import sys
import statistics
import os.path

data_array = [] # from the text file, values are saved in ms scale. 
abs_jitter_task_entry = [] 
jitter_task_entry = []

NS2MS = 1000000
NS2US = 1000

input_file = sys.argv[1]
task_period = int(sys.argv[2])
#task_period = [8000000, 4000000, 2000000, 1000000, 500000]

with open (input_file, "r") as f:
	for line in f:
		data_array.append(int(line)/NS2MS)
		abs_jitter_task_entry.append(abs((int(line)-task_period)/NS2US))
		jitter_task_entry.append((int(line)-task_period)/NS2US)
	f.close()

# Calculate values
Avg = statistics.mean(data_array)
Min = min(data_array)
Max = max(data_array)
Mode = statistics.mode(data_array) # Most value in the samples. 
Median = statistics.median(data_array)
Var = statistics.variance(data_array, Avg)
Stdev = statistics.stdev(data_array)

# Calculate Absolute jitter 
AbsJitterAvg = statistics.mean(abs_jitter_task_entry)
AbsJitterMin = min(abs_jitter_task_entry)
AbsJitterMax = max(abs_jitter_task_entry)
AbsJitterMode = statistics.mode(abs_jitter_task_entry)
AbsJitterMedian = statistics.median(abs_jitter_task_entry)
AbsJitterVar = statistics.variance(abs_jitter_task_entry, AbsJitterAvg)
AbsJitterStdev = statistics.stdev(abs_jitter_task_entry)

# Calculate jitter
JitterAvg = statistics.mean(jitter_task_entry)
JitterMin = min(jitter_task_entry)
JitterMax = max(jitter_task_entry)
JitterMode = statistics.mode(jitter_task_entry)
JitterMedian = statistics.median(jitter_task_entry)
JitterVar = statistics.variance(jitter_task_entry, JitterAvg)
JitterStdev = statistics.stdev (jitter_task_entry)


print ("======"+input_file+"'summary"+"======"+"\n")
print ("Avg:",Avg)
print ("Min:",Min," Max:",Max)
print ("Median:",Median,"Modes:", Mode)
print ("Var:",Var)
print ("Stdev:",Stdev)
print ("=========================================="+"\n")
print ("======"+input_file+"'Absolute jitter"+"======"+"\n")
print ("Avg:", AbsJitterAvg)
print ("Min:",AbsJitterMin," Max:",AbsJitterMax)
print ("Median:",AbsJitterMedian,"Modes:", AbsJitterMode)
print ("Var:",AbsJitterVar)
print ("Stdev:",AbsJitterStdev)
print ("=========================================="+"\n")
print ("======"+input_file+"'Jitter"+"======"+"\n")
print ("Avg:", JitterAvg)
print ("Min:",JitterMin," Max:",JitterMax)
print ("Median:",JitterMedian,"Modes:", JitterMode)
print ("Var:",JitterVar)
print ("Stdev:",JitterStdev)
print ("=========================================="+"\n")

output_file = os.path.splitext(input_file)[0]
result_postfix = ".result"
abs_jit_postfix = ".absjit"
jit_postfix = ".jit"

# To draw graph with gnuplot.
output_gnuplot = output_file+result_postfix
output_abs_jit = output_file+abs_jit_postfix
output_jit = output_file+jit_postfix

#print (output_gnuplot)
#print (output_abs_jit)
#print (output_jit)

# Summary stats.
with open(output_gnuplot, "w") as w:
	w.write(str(Avg)+"\t"+str(Min)+"\t"+str(Max)+"\t"+str(Mode)+"\t"+str(Median)+"\t"+str(Var)+"\t"+str(Stdev)+"\n") 
	w.close()

# Absolute task entry jitter stats.
with open(output_abs_jit, "w") as w:
	for arr in abs_jitter_task_entry:
		w.write(str(arr)+"\n") 
	w.close()
 
# Task entry jitter stats.
with open(output_jit, "w") as w:
	for arr in jitter_task_entry:
		w.write(str(arr)+"\n") 
	w.close()
 
