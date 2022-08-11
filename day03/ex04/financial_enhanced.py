import sys
import httpx
from bs4 import BeautifulSoup as bs


def parse():
    if (request := httpx.get(
                    f'https://finance.yahoo.com/quote/{sys.argv[1]}/financials',
                    headers={'User-Agent': 'Custom'})
                    ).status_code !=200:
        raise Exception('page not found')
    soup = bs(request.text, 'html.parser')
    fields = soup.find_all('div', attrs={'data-test': 'fin-row'})
    for i in fields:
        if i.find("div", attrs={'title' : sys.argv[2]}):
            cols = i.find_all('div', {'data-test' : 'fin-col'})
            return tuple([sys.argv[2], *[i.text for i in cols]])
    raise Exception("field does not exist")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        raise Exception("invalid argv")
    fin_info = parse()
    if fin_info is None:
        raise Exception("invalid info")
    print(fin_info)