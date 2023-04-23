from urllib.request import urlopen, Request

from bs4 import BeautifulSoup


class Currency:
    def __init__(self, bid, ask, code, currName):
        self.bid = bid
        self.ask = ask
        self.code = code
        self.currencyName = currName


def getCurrencies():
    currencies = ["eur", "usd", "chf", "gbp", "nok", "dkk", "sek", "czk", "jpy"]
    currenciesList = []

    for curr in currencies:
        page = "https://api.nbp.pl/api/exchangerates/rates/c/{}/".format(curr)
        req = Request(page)
        page = urlopen(req)
        soup = BeautifulSoup(page, 'lxml')

        bid = str(soup.find("p")).split(":")[7].split(",")[0]
        ask = str(soup.find("p")).split(":")[8].split("}")[0]
        code = str(soup.find("p")).split(":")[3].split(",")[0]
        name = str(soup.find("p")).split(":")[2].split(",")[0]

        currenciesList.append(Currency(bid, ask, code, name))

    print("Currencies - SUCCESS")
    return currenciesList
