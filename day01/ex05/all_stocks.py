import sys


def init_dict():
    companies = {
        'Apple': 'AAPL',
        'Microsoft': 'MSFT',
        'Netflix': 'NFLX',
        'Tesla': 'TSLA',
        'Nokia': 'NOK'
    }
    stocks = {
        'AAPL': 287.73,
        'MSFT': 173.79,
        'NFLX': 416.90,
        'TSLA': 724.88,
        'NOK': 3.37
    }
    return companies, stocks


def get_item(d, item):
    for k, v in d.items():
        if v == item:
            return k
        elif k == item:
            return v
    return None


def search():
    companies, stocks = init_dict()

    if len(sys.argv) == 2:
        for item in (l := sys.argv[1].split(',')):
            item = item.strip()
            if item == '':
                print()
                return
        for item in l:
            item = item.strip()
            if (s := item.upper()) in companies.values():
                print(s, 'is a ticker symbol for', get_item(companies, s))
            elif (s := item.capitalize()) in companies.keys():
                print(s, 'stock price is', get_item(stocks, get_item(companies, s)))
            else:
                print(item, 'is an unknown company or an unknown ticker symbol')


if __name__ == '__main__':
    search()
