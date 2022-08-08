import sys


def check():
    if sys.argv[2].isascii() and sys.argv[3].isdecimal():
        return
    else:
        raise ValueError('text must contein only ascii symbols and latest arg must be number')


def encode():
    check()
    text = list(sys.argv[2])
    alpha = list(map(chr, range(ord('a'), ord('z')+1)))
    # ALPHA = list(map(chr, range(ord('A'), ord('Z')+1)))
    text = [chr((alpha.index(i) + int(sys.argv[3])) % len(alpha)) if i in alpha else i for i in text]
    print (text)
    # print([((ord(i) + int(sys.argv[3])) % len(ALPHA)) if ord(i) in ALPHA else i for i in text])


def decode():
    check()
    line = sys.argv[2]


def init():
    match sys.argv[1]:
        case "encode":
            encode()
        case "decode":
            decode()
        case _:
            raise ValueError(f'command \"{sys.argv[1]}\" is not defined')


if __name__ == '__main__':
    if len(sys.argv) == 4:
        init()
    else:
        raise TypeError(f"caesar takes 3 arguments but {len(sys.argv) - 1} was given")