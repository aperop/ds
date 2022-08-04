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

def search():
    companies, stocks = init_dict()

    if len(sys.argv) == 2:
        if (s := sys.argv[1].capitalize()) in companies.keys():
            print(stocks.get(companies.get(s), 'Unknown company'))
        else:
            print('Unknown company')


if __name__ == '__main__':
    search()
