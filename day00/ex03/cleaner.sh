#!/bin/sh

(head -n 1 ../ex02/hh_sorted.csv;      \
tail -n +2 ../ex02/hh_sorted.csv |     \
awk 'BEGIN { FS = OFS = "," }
    {
        str = ""

        if (index(tolower($3), "junior"))
            str = str"Junior/"
        if (index(tolower($3), "middle"))
            str = str"Middle/"
        if (index(tolower($3), "senior"))
            str = str"Senior"
        if (str == "")
            str = "-"

        gsub(/[\/ ]*$/, "", str)
        $3 = "\""str"\""
        print
    }'
) > hh_positions.csv