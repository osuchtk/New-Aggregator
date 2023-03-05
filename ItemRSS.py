from urllib.request import urlopen, Request

from bs4 import BeautifulSoup


# class declaring item attributes
class Items:
    def __init__(self, title, description, link, pubDate, image, category):
        self.title = title
        self.description = description
        self.link = link
        self.pubDate = pubDate
        self.image = image
        self.category = category


# creating list with xml files with feeds
def makeSoups(links):
    soupList = []
    for link in links:
        req = Request(link)
        page = urlopen(req)

        soup = BeautifulSoup(page, 'xml')
        soupList.append(soup)

    return soupList


# making class objects with attributes
def makeItem(soups):
    itemsList = []
    for soup in soups:
        allItems = list(soup.find_all("item"))

        for item in allItems:
            title = item.find("title")
            description = item.find("description")
            link = item.find("link")
            pubDate = item.find("pubDate")
            image = item.find("enclosure")
            category = item.find("category")

            itemsList.append(Items(title, description, link, pubDate, image, category))

    return itemsList
