import sys


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
        @staticmethod
        def counts(arr):
            return [sum(i) for i in zip(*arr)]

        @staticmethod
        def fractions(arr):
            return [i / sum(arr) * 100 for i in arr]


if __name__ == '__main__':
    if len(sys.argv) == 2:
        r = Research(sys.argv[1])
        print(fr := r.file_reader())
        print(*(count := r.Calculations.counts(fr)))
        print(*r.Calculations.fractions(count))
