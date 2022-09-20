#!../ex00/dhawkgir/bin/python3
import sys
import requests
from bs4 import BeautifulSoup as bs
import pytest


def parse(ticker, info) -> tuple:
    if (request := requests.get(f'https://finance.yahoo.com/quote/{ticker}/financials',
                                headers={'User-Agent': 'Custom'})).status_code != 200:
        raise Exception('page not found')
    soup = bs(request.text, 'html.parser')
    fields = soup.find_all('div', attrs={'data-test': 'fin-row'})
    for i in fields:
        if i.find("div", attrs={'title': info}):
            cols = i.find_all('div', {'data-test': 'fin-col'})
            return tuple([info, *[i.text for i in cols]])
    raise Exception("field does not exist")


def test_return_type():
    assert isinstance(parse("AAPL", "Total Revenue"), tuple)


def test_total_revenue():
    assert parse("AAPL", "Total Revenue")[0] == "Total Revenue"


def test_exception():
    with pytest.raises(Exception):
        parse()
        parse(1)
        parse(1, 2)
        parse(1, 2, 3)
        parse("QWQWQ", "Total Revene")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        raise Exception("invalid argv")
    fin_info = parse(sys.argv[1], sys.argv[2])
    if fin_info is None:
        raise Exception("invalid info")
    print(fin_info)
