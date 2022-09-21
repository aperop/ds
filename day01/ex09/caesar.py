import sys


def check():
    if sys.argv[2].isascii() and sys.argv[3].isdecimal():
        return
    else:
        raise ValueError('text must contein only ascii symbols and latest arg must be number')


def code(text, flag):
    check()
    alpha = list(map(chr, range(ord('a'), ord('z') + 1)))
    alpha_upper = list(map(chr, range(ord('A'), ord('Z') + 1)))
    cipher = "".join(chr((alpha.index(i) + flag * int(sys.argv[3]))
                         % len(alpha) + 97) if i in alpha else i for i in text)
    cipher = "".join(chr((alpha_upper.index(i) + flag * int(sys.argv[3]))
                         % len(alpha_upper) + 65) if i in alpha_upper else i for i in cipher)
    return cipher


def init():
    match sys.argv[1]:
        case "encode":
            print(code(sys.argv[2], 1))
        case "decode":
            print(code(sys.argv[2], -1))
        case _:
            raise ValueError(f'command \"{sys.argv[1]}\" is not defined')


if __name__ == '__main__':
    if len(sys.argv) == 4:
        init()
    else:
        raise TypeError(f"caesar takes 3 arguments but {len(sys.argv) - 1} was given")
