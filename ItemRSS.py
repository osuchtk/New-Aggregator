from urllib.request import urlopen, Request

from bs4 import BeautifulSoup


# class getting all items from xml feed file
class Items:

    def __init__(self, rssLink):
        # declaring item attributes
        self.title = []
        self.description = []
        self.link = []
        self.pubDate = []
        self.image = []
        self.category = []

        self.rssLink = rssLink
        self.soup = None

    def makeSoup(self):
        # opening url address with feed
        req = Request(self.rssLink)
        page = urlopen(req)

        self.soup = BeautifulSoup(page, 'xml')

    def addElements(self):
        # adding elements to lists
        allItems = list(self.soup.find_all("item"))

        for item in allItems:
            self.title.append(item.find("title"))
            self.description.append(item.find("description"))
            self.link.append(item.find("link"))
            self.pubDate.append(item.find("pubDate"))
            self.image.append(item.find("enclosure"))
            self.category.append(item.find("category"))
