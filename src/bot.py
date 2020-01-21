import time as t


class Article:
    def __init__(self):
        self.headline = ""
        self.date = ""
        self.link = ""
        self.content = ""
        self.author = ""

    def print(self):
        print(self.headline)
        print(self.date)
        print(self.author)
        print(self.link)
        print(self.content + "\n\n\n")


class SpiegelBot:
    def __init__(self, driver):
        self.driver = driver
        self.file = ""

    def getSavedContent(self):
        save = open(self.file, 'r', encoding="utf-8")
        ret = save.read()
        save.close()
        return ret

    def saveArticle(self, art):

        if not art.link in self.getSavedContent():
            save = open(self.file, 'a', encoding="utf-8")
            save.write(art.headline + "\n")
            save.write(art.date + "\n")
            save.write(art.author + "\n")
            save.write(art.link + "\n")
            save.write(art.content + "\n\n")

            print("Registered new Article: " + art.headline)

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
            t.sleep(3)
            self.driver.get(link.link)
            authorContainer = self.driver.find_elements_by_css_selector('a[class="text-black font-bold border-b '
                                                                        'border-shade-light hover:border-black"]')

            AuthorString = ""

            for author in authorContainer:
                AuthorString += author.get_attribute("title") + ";"





            link.author = AuthorString

            link.date_c = self.driver.find_element_by_class_name("timeformat")
            link.date = link.date_c.text

            textContainers = self.driver.find_elements_by_class_name("RichText")
            for text in textContainers:
                link.content += text.text

            self.saveArticle(link)


