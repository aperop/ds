#!/bin/zsh

echo "@ Pies,Bars
2007,73.32,70.52
2008,81.23,93.00
2009,181.43,135.10
2010,110.21,95.00
2011,93.97,90.45" > data.txt

termgraph data.txt --color {blue,yellow} --custom-tick "░"