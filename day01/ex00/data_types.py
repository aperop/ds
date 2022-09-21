def data_types():
    my_int = 42
    my_str = '42'
    my_float = 42.
    my_bool = True
    my_list = [42]
    my_dict = {42: 42}
    my_tuple = 42,
    my_set = {1}
    types = [type(my_int),
             type(my_str),
             type(my_float),
             type(my_bool),
             type(my_list),
             type(my_dict),
             type(my_tuple),
             type(my_set)
             ]

    print("[", ", ".join(str(i).split("'")[1] for i in types), "]", sep="")


if __name__ == '__main__':
    data_types()
