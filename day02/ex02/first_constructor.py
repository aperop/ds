import sys


class Research:

    def __init__(self, path: str) -> None:
        self.path = path

    def file_reader(self):
        with open(self.path, mode="r") as f_in:
            lines = f_in.readlines()
            if lines[0].rstrip() != 'head,tail' or len(lines) < 2:
                raise Exception('File must contains a header with two strings delimited by a comma')
            for line in lines[1:]:
                if line.rstrip() not in {'0,1', '1,0'}:
                    raise Exception('The data must contains only 0 or 1')
            return lines


if __name__ == '__main__':
    if len(sys.argv) == 2:
        print(*Research(sys.argv[1]).file_reader(), sep='')
