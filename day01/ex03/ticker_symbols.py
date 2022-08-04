import sys


def init_dict():
    COMPANIES = {
        'Apple': 'AAPL',
        'Microsoft': 'MSFT',
        'Netflix': 'NFLX',
        'Tesla': 'TSLA',
        'Nokia': 'NOK'
    }
    STOCKS = {
        'AAPL': 287.73,
        'MSFT': 173.79,
        'NFLX': 416.90,
        'TSLA': 724.88,
        'NOK': 3.37
    }
    return COMPANIES, STOCKS

def get_key(d, value):
    for k, v in d.items():
        if v == value:
            return k
    return 'Unknown ticker symbol'

def search():
    companies, stocks = init_dict()

    if len(sys.argv) == 2:
        if (s := sys.argv[1].upper()) in stocks:
            print(get_key(companies, s), stocks.get(s, ""))
        else:
            print('Unknown ticker symbol')


if __name__ == '__main__':
    search()
