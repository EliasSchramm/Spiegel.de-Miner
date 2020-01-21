from selenium import webdriver

from src.bot import SpiegelBot

PATH_TO_DRIVER = "/home/phantomjs"

webdriver.PhantomJS(service_args=['--load-images=no'])

driver = webdriver.PhantomJS(PATH_TO_DRIVER)

webdriver.PhantomJS(service_args=['--load-images=no'])

categories = ["politik","panorama","sport", "wirtschaft","netzwelt","wissenschaft"\
              "auto","kultur","geschichte","leben","karriere"]

bot = SpiegelBot(driver)

while True:
    for a in categories:
        bot.check(a)

