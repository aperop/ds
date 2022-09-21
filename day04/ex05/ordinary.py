# /opt/goinfre/dhawkgir/ml-25m/ratings.csv

import sys
import resource as res


def read_on_list(path):
    with open(path, 'r') as file:
        return file.readlines()


if __name__ == "__main__":
    if len(sys.argv) == 2:
        lst = read_on_list(sys.argv[1])
        for i in lst:
            pass
        usage = res.getrusage(res.RUSAGE_SELF) 
        print(f"Peak Memory Usage = {usage.ru_maxrss / (1024**3):0.3f} GB")
        print(f"User Mode Time + System Mode Time = {usage.ru_utime + usage.ru_stime:0.2f}s")
