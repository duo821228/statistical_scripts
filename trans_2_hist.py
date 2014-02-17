#!/usr/bin/python

# Writer: Andrew
# Description: This file produces histogram result of experimental file. 
#              Calculate sample numbers between interval(bin) and its probability..
#			   input file must be saved in ns scale.
#
# CAUTION: It is running with python 2.7.X only. 
#		   numpy module which can produce histogram from array list is not provided in python 3.4.X. 
#
# Usage: python2.7 ./this.py ./yourdata.data
# Result example:
# 	7995125		16.0		0.0
#	7995777		33.0		0.0
#	7996429		81.0		0.001
#	7997081		192.0		0.003
#	7997733		584.0		0.008
#	7998385		1439.0		0.019
#	7999037		12750.0		0.17
#	7999689		47475.0		0.633
#	8000341		9650.0		0.129
#	8000993		1803.0		0.024
#	8001646		551.0		0.007
#	8002298		174.0		0.002
#	8002950		116.0		0.002
#	8003602		71.0		0.001
#	8004254		18.0		0.0
#
#											  
# TODO: Must be merged with stat_cal.py 

import sys
import os.path
import numpy as np

data_array = []
output_array = []
bin_size = 60

file_name = sys.argv[1]

with open (file_name, "r") as f:
	for line in f:
		data_array.append(int(line))
	f.close()

hist, bins = np.histogram(data_array, bins=bin_size)

print (hist)
print (bins)
hist = map (float, hist)

output_file = os.path.splitext(file_name)[0]
output_file += ".hist"
#print (output_file)
with open(output_file, "w") as w:
	for idx in range(bin_size):
		# timestamp (ns scale)	 number_of_timestamp	probability in bins
		w.write(str(int(bins[idx]))+"\t\t"+str(hist[idx])+"\t\t"+str(round(hist[idx]/len(data_array), 3))+"\n");
	w.close()
   
