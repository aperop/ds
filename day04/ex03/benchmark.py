import timeit
import sys
from functools import reduce


def loop(number):
    sum = 0
    for i in range(number + 1):
        sum += i*i
    return sum


def my_func(func, number, calc_number):
    match func:
        case "loop":
            print(timeit.timeit(lambda: loop(calc_number), number=number))
        case "reduce":
            print(timeit.timeit(lambda: reduce(lambda sum, i: sum + i*i, range(calc_number + 1)), number=number))
        case _:
            raise ValueError("invalid command")


if __name__ == "__main__":
    if len(sys.argv) == 4:
        number = int(sys.argv[2])
        calc_number = int(sys.argv[3])
        my_func(sys.argv[1], number, calc_number)
