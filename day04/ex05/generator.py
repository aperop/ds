# /opt/goinfre/dhawkgir/ml-25m/ratings.csv

import sys
import resource as res


def generator(path: str):
    with open(path, 'r') as file:
        for line in file:
            yield line


if __name__ == "__main__":
    if len(sys.argv) == 2:
        gen = generator(sys.argv[1])
        for i in gen:
            pass
        usage = res.getrusage(res.RUSAGE_SELF) 
        print(f"Peak Memory Usage = {usage.ru_maxrss / (1024**3):0.3f} GB")
        print(f"User Mode Time + System Mode Time = {usage.ru_utime + usage.ru_stime:0.2f}s")
