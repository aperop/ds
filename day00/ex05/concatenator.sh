#!/bin/sh

awk 'NR == 1 || FNR > 1' *.csv > restore.csv