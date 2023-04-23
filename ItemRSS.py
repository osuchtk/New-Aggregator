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
    categoryList = []

    # iterate through keys of dictionary to get to values (links) ang get xml
    for category in links.keys():
        for link in links[category]:
            req = Request(link)
            page = urlopen(req)
            soup = BeautifulSoup(page, 'xml')
            categoryList.append(category)
            soupList.append(soup)

    return categoryList, soupList


# making class objects with attributes
def makeItem(soups, categories):
    itemsList = []
    for soup, categoryIterator in zip(soups, categories):
        allItems = list(soup.find_all("item"))

        for item in allItems:
            title = item.find("title").text
            description = item.find("description").text
            link = item.find("link").text
            pubDate = item.find("pubDate").text
            try:
                image = item.find("enclosure").attrs['url']
            except AttributeError:
                try:
                    image = item.find("enclosure").attrs['src']
                except AttributeError:
                    image = None
            try:
                guid = item.find("guid").text
            except AttributeError:
                guid = None

            category = categoryIterator

            itemsList.append(Items(title, description, link, pubDate, image, category, guid))

    print("News - SUCCESS")
    return itemsList
