#!/bin/sh

echo "\"name\"","\"count\"" > hh_uniq_positions.csv

(tail -n +2 ../ex03/hh_positions.csv |     \
awk 'BEGIN { FS = OFS = "," }
    {
        if (index($3, "Junior"))
            Junior++
        if (index($3, "Middle"))
            Middle++
        if (index($3, "Senior"))
            Senior++
    }
    END { print "\"Junior\"", Junior    \
                "\n\"Middle\"", Middle  \
                "\n\"Senior\"", Senior }'
) |     \
sort -t',' -n -k2 -r >> hh_uniq_positions.csv