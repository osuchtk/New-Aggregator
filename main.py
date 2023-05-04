from ItemRSS import makeSoups, makeItem
from currency import getCurrencies
from mariadbcontroller import connectToDatabase, addNews, addActualWeather, addForecastWeather, addCurrencies
from weather import getWeather

# declaring categories
categories = ["Wszystkie",
              "Polska",
              "Świat",
              "Kultura",
              "Sport",
              "Biznes",
              "Rozrywka"]

# declaring websites to get news from
categoryALL = ["https://wydarzenia.interia.pl/feed",
               "https://www.polsatnews.pl/rss/wszystkie.xml",
               "https://tvn24.pl/najnowsze.xml",
               "https://www.rmf24.pl/feed",
               "https://www.bankier.pl/rss/wiadomosci.xml",
               "https://www.tokfm.pl/pub/rss/tokfmpl_glowne.xml"]
categoryPoland = ["https://wydarzenia.interia.pl/polska/feed",
                  "https://www.polsatnews.pl/rss/polska.xml",
                  "https://tvn24.pl/wiadomosci-z-kraju,3.xml",
                  "https://www.rmf24.pl/fakty/polska/feed",
                  "https://www.tokfm.pl/pub/rss/tokfmpl_polska.xml"]
categoryWorld = ["https://wydarzenia.interia.pl/swiat/feed",
                 "https://www.polsatnews.pl/rss/swiat.xml",
                 "https://tvn24.pl/wiadomosci-ze-swiata,2.xml",
                 "https://www.rmf24.pl/fakty/swiat/feed",
                 "https://www.tokfm.pl/pub/rss/tokfmpl_swiat.xml"]
categoryCulture = ["https://wydarzenia.interia.pl/kultura/feed",
                   "https://www.polsatnews.pl/rss/kultura.xml",
                   "https://tvn24.pl/kultura-styl,8.xml",
                   "https://www.rmf24.pl/kultura/feed",
                   "https://www.tokfm.pl/pub/rss/tokfmpl_kultura.xml"]
categorySport = ["https://sport.interia.pl/feed",
                 "https://www.polsatnews.pl/rss/sport.xml",
                 "https://eurosport.tvn24.pl/sport,81,m.xml",
                 "https://www.rmf24.pl/sport/feed",
                 "https://www.tokfm.pl/pub/rss/tokfmpl_sport.xml"]
categoryBusiness = ["https://biznes.interia.pl/feed",
                    "https://www.polsatnews.pl/rss/biznes.xml",
                    "https://tvn24.pl/biznes-gospodarka,6.xml",
                    "https://www.bankier.pl/rss/finanse.xml",
                    "https://www.bankier.pl/rss/firma.xml",
                    "https://www.bankier.pl/rss/espi.xml",
                    "https://www.rmf24.pl/ekonomia/feed",
                    "https://www.tokfm.pl/pub/rss/tokfmpl_biznes.xml"]
categoryEntertainment = ["https://gry.interia.pl/feed",
                         "https://film.interia.pl/feed",
                         "https://muzyka.interia.pl/feed",
                         "https://www.tokfm.pl/pub/rss/tokfmpl_rozrywka.xml"]

# concatenating links to one list
links = categoryALL + categoryPoland + categoryWorld + categoryCulture + categorySport + categoryBusiness + \
        categoryEntertainment

# creating dictionary from categories and websites
categoriesDict = {'All': categoryALL,
                  'Poland': categoryPoland,
                  'World': categoryWorld,
                  'Culture': categoryCulture,
                  'Sport': categorySport,
                  'Business': categoryBusiness,
                  'Entertainment': categoryEntertainment}

# getting news, weather and currencies
categories, soups = makeSoups(categoriesDict)
items = makeItem(soups, categories)

weatherActual, weatherForecast = getWeather()

currencies = getCurrencies()

# connecting to database to save data
conn, cur = connectToDatabase()
for item in items:
    addNews(item, cur, conn)

for item in weatherActual:
    addActualWeather(item, cur, conn)

for item in weatherForecast:
    addForecastWeather(item, cur, conn)

for item in currencies:
    addCurrencies(item, cur, conn)

# closing connection
conn.close()
