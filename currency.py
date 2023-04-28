import urllib.error
from datetime import datetime, timedelta
from urllib.request import urlopen, Request

import pandas as pd
from bs4 import BeautifulSoup


class Currency:
    def __init__(self, bid, ask, code, currName, date, recordID):
        self.bid = bid
        self.ask = ask
        self.code = code
        self.currencyName = currName
        self.date = date
        self.recordID = recordID


def getCurrencies():
    currencies = ["eur", "usd", "chf", "gbp", "nok", "dkk", "sek", "czk", "jpy"]
    currenciesList = []

    dateRange = pd.date_range(datetime.today().date() - timedelta(days=30), datetime.today(), unit="ns")
    # dateRange[6].to_pydatetime().date()

    for curr in currencies:
        for date in dateRange:
            try:
                date = date.to_pydatetime().date()
                page = "https://api.nbp.pl/api/exchangerates/rates/c/{}/{}/".format(curr, date)
                req = Request(page)
                page = urlopen(req)
                soup = BeautifulSoup(page, 'lxml')

                bid = str(soup.find("p")).split(":")[7].split(",")[0]
                ask = str(soup.find("p")).split(":")[8].split("}")[0]
                code = str(soup.find("p")).split(":")[3].split(",")[0]
                name = str(soup.find("p")).split(":")[2].split(",")[0]
                # dateVal = str(soup.find("p")).split(":")[6].split(",")[0].split('"')[1]

                id = str(date) + " " + code

                currenciesList.append(Currency(bid, ask, code, name, date, id))

            except urllib.error.HTTPError:
                pass

    print("Currencies - SUCCESS")
    return currenciesList

# tepm = getCurrencies()
