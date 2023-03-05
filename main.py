from ItemRSS import Items

# link = "https://wydarzenia.interia.pl/feed"
# link = "https://tvn24.pl/najnowsze.xml"
links = ["https://wydarzenia.interia.pl/feed",
         "https://tvn24.pl/najnowsze.xml",
         "https://www.polsatnews.pl/rss/wszystkie.xml"]

items = []
for link in links:
    items.append(Items(link))

for item in items:
    item.makeSoup()
    item.addElements()

print(1)
