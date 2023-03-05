from ItemRSS import makeSoups, makeItem

links = ["https://wydarzenia.interia.pl/feed",
         "https://tvn24.pl/najnowsze.xml",
         "https://www.polsatnews.pl/rss/wszystkie.xml"]

soups = makeSoups(links)
items = makeItem(soups)

print(1)
