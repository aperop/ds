python -m cProfile -s tottime financial.py 'MSFT' 'Total Revenue' > profiling-sleep.txt
python -m cProfile -s tottime financial.py 'MSFT' 'Total Revenue' > profiling-tottime.txt
python -m cProfile -s ncalls financial.py 'MSFT' 'Total Revenue' > profiling-ncalls.txt
python -m cProfile -s ncalls financial_enhanced.py 'MSFT' 'Total Revenue' > profiling-http.txt
# for pstats
python -m cProfile -o profiling-tottime.profile financial.py 'MSFT' 'Total Revenue'
echo "
sort cumtime
stats 5
EOF" | python -m pstats profiling-tottime.profile > pstats-cumulative.txt
