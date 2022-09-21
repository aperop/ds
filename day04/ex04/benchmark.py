import timeit
import random
from collections import Counter


def generate() -> list:
    return [random.randrange(0, 101) for _ in range(1000000)]


def counter(lst: list) -> dict:
    return {i: lst.count(i) for i in set(lst)}


def counter_top(lst: list) -> dict:
    count_dict = {i: lst.count(i) for i in set(lst)}
    my_list = list(count_dict.items())    
    return dict(sorted(my_list, key=lambda x: -x[1])[:10])


def benchmark(lst: list) -> None:
    print("my function:", timeit.timeit(lambda: counter(lst), number=1))
    print("Counter:", timeit.timeit(lambda: Counter(lst), number=1))
    print("my top:", timeit.timeit(lambda: counter_top(lst), number=1))
    print("Counter's top:", timeit.timeit(lambda: Counter(lst).most_common(10), number=1))


if __name__ == "__main__":
    benchmark(generate())
