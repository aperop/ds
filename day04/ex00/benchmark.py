import timeit


def emails() -> list:
    return ["john@gmail.com",
            "james@gmail.com",
            "alice@yahoo.com",
            "anna@live.com",
            "philipp@gmail.com"
            ] * 5


def loop(emails: list) -> list:
    lst = []
    for i in emails:
        if i.endswith('gmail.com'):
            lst.append(i)
    return lst


def comprehension(emails: list) -> list:
    return [i for i in emails if i.endswith('gmail.com')]


if __name__ == "__main__":
    number = 90_000_000
    bench = dict()
    bench['loop'] = timeit.timeit(lambda: loop(emails()), number=number)
    bench['list comprehension'] = timeit.timeit(lambda: comprehension(emails()), number=number)
    my_list = list(bench.items())    
    my_list.sort(key=lambda x: x[1])
    print("it is better to use a " + my_list[0][0])
    print(*[i[1] for i in my_list], sep=' vs ')

# it is better to use a list comprehension
# 310.128922122065 vs 334.9740557090845