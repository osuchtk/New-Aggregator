from urllib.request import urlopen, Request

from bs4 import BeautifulSoup


# class declaring item attributes
class Items:
    def __init__(self, title, description, link, pubDate, image, category, guid):
        self.title = title
        self.description = description
        self.link = link
        self.pubDate = pubDate
        self.image = image
        self.category = category
        if guid is not None:
            self.guid = guid
        else:
            self.guid = link


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
            title = item.find("title").text
            description = item.find("description").text
            link = item.find("link").text
            pubDate = item.find("pubDate").text
            try:
                image = item.find("enclosure").attrs["url"]
            except AttributeError:
                try:
                    image = item.find("enclosure").attrs["src"]
                except AttributeError:
                    image = None
            try:
                category = item.find("category").text
            except AttributeError:
                category = None
            try:
                guid = item.find("guid").text
            except AttributeError:
                guid = None

            itemsList.append(Items(title, description, link, pubDate, image, category, guid))

    return itemsList
