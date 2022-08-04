def data_types():
    i = 42
    s = '42'
    f = 42.
    b = True
    m = [42]
    d = {42: 42}
    t = 42,
    set = {i} & {s}
    types = [type(i), type(s), type(f), type(b), type(m), type(d), type(t), type(set)]
    print("[", ", ".join(str(i).split("'")[1] for i in types), "]", sep="")


if __name__ == '__main__':
    data_types()