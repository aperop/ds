#!/bin/sh

awk ' BEGIN { FS = "," }
    {
        if (NR == 1)
            header = $0
        else
        {
            file = substr($2, 2, 10)".csv"

            if (!(file in files))
            {
                files[file]
                print header > file
            }
            print >> file
        }
    }
    '  ../ex03/hh_positions.csv