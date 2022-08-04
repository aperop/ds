def init():
    list_of_tuples = [
        ('Russia', '25'),
        ('France', '132'),
        ('Germany', '132'),
        ('Spain', '178'),
        ('Italy', '162'),
        ('Portugal', '17'),
        ('Finland', '3'),
        ('Hungary', '2'),
        ('The Netherlands', '28'),
        ('The USA', '610'),
        ('The United Kingdom', '95'),
        ('China', '83'),
        ('Iran', '76'),
        ('Turkey', '65'),
        ('Belgium', '34'),
        ('Canada', '28'),
        ('Switzerland', '26'),
        ('Brazil', '25'),
        ('Austria', '14'),
        ('Israel', '12')
    ]
    return list_of_tuples


def sort_dict():
    list_of_tuples = init()


    result = dict(list_of_tuples)
    my_list = list(result.items())
    my_list.sort(key=lambda x: x[0])
    my_list.sort(key=lambda x: (-1) * int(x[1]))
    for country, _ in my_list:
        print(country)


if __name__ == '__main__':
    sort_dict()