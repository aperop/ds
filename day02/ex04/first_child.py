import sys
from random import randint


class Research:

    def __init__(self, path: str) -> None:
        self.path = path

    def file_reader(self, has_header=True):
        with open(self.path, mode="r") as f_in:
            lines = f_in.readlines()
            arr = []
            head = 1 if has_header else 0
            if has_header and (lines[0].rstrip() != 'head,tail' or len(lines) < 2):
                raise Exception('File must contains a header with two strings delimited by a comma')
            for line in lines[head:]:
                if line.rstrip() not in {'0,1', '1,0'}:
                    raise Exception('The data must contains only 0 or 1')
                arr.append(list(map(int, line.split(','))))
            return arr

    class Calculations:

        def __init__(self, arr) -> None:
            self.arr = arr

        def counts(self):
            return [sum(i) for i in zip(*self.arr)]

        @staticmethod
        def fractions(arr):
            return [i / sum(arr) * 100 for i in arr]

    class Analytics(Calculations):

        @staticmethod
        def predict_random(num: int):
            return [[[1, 0], [0, 1]][randint(0, 1)] for _ in range(num)]

        def predict_last(self):
            return self.arr[-1]


if __name__ == '__main__':
    if len(sys.argv) == 2:
        r = Research(sys.argv[1])
        print(fr := r.file_reader())
        print(*(count := r.Calculations(fr).counts()))
        print(*r.Calculations(fr).fractions(count))
        print(r.Analytics(fr).predict_random(3))
        print(r.Analytics(fr).predict_last())
