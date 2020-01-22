from selenium import webdriver

from src.bot import SpiegelBot

PATH_TO_DRIVER = "C:/Windows/phantomjs.exe"

driver = webdriver.PhantomJS(PATH_TO_DRIVER, service_args=["--load-images=no"])


categories = ["politik","panorama","sport", "wirtschaft","netzwelt",\
              "auto","kultur","geschichte","leben","karriere"]

bot = SpiegelBot(driver)

for a in categories:
  bot.check(a)



