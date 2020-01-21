import time as t


class Article:
    def __init__(self):
        self.headline = ""
        self.date = ""
        self.link = ""
        self.content = ""


class SpiegelBot:
    def __init__(self, driver):
        self.driver = driver
        self.file = ""

    def check(self, categorie):
        self.driver.get("https://www.spiegel.de/" + categorie + "/")
        t.sleep(1)

        # Create file
        self.file = "saves/" + categorie + ".txt"

        save = open(self.file, 'a', encoding="utf-8")
        save.close()

        newestNewsContainer = self.driver.find_element_by_css_selector('section[data-area="article-teaser-list"]')

        newsList = newestNewsContainer.find_elements_by_css_selector('a[class="block"]')

        ArticleList = []



        for articleTeaser in newsList:
            art = Article()
            art.link = articleTeaser.get_attribute("href")
            art.headline = articleTeaser.get_attribute("title")
            ArticleList.append(art)


        for link in ArticleList:
            self.driver.get(link.link)
            t.sleep(1)
