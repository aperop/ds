import timeit
import sys

def emails():
    return ["john@gmail.com",
            "james@gmail.com",
            "alice@yahoo.com",
            "anna@live.com",
            "philipp@gmail.com"
            ] * 5

def loop(emails):
    lst = []
    for i in emails:
        if i.endswith('gmail.com'):
            lst.append(i)
    return lst

def comprehension(emails):
    return [i for i in emails if i.endswith('gmail.com')]

def my_map(emails):
    return map(lambda x: x if x.endswith('gmail.com') else None, emails)

def my_filter(emails):
    return filter(lambda x: x if x.endswith('gmail.com') else None, emails)


def my_func(func, number):
    match func:
        case "loop":
            print(timeit.timeit(lambda: loop(emails()), number=number))
        case "list_comprehension":
            print(timeit.timeit(lambda: comprehension(emails()), number=number))
        case "map":
            print(timeit.timeit(lambda: my_map(emails()), number=number))
        case "filter":
            print(timeit.timeit(lambda: my_filter(emails()), number=number))
        case _:
            raise ValueError("invalid command")

if __name__ == "__main__":
    if len(sys.argv) == 3:
        number = int(sys.argv[2])
        my_func(sys.argv[1], number)