#!/bin/bash
# This is a wrapper script to calculate statistics of experimental result.
# TODO: 

for i in *.txt
do
#	echo $i
	python3.4 ./stat_cal.py $i
done
