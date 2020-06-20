from selenium import webdriver

from src.bot import SpiegelBot

PATH_TO_DRIVER = ""

driver = webdriver.Firefox(executable_path=PATH_TO_DRIVER)

categories = ["politik","panorama","sport", "wirtschaft","netzwelt",\
              "auto","kultur","geschichte","leben","karriere"]

bot = SpiegelBot(driver)

for a in categories:
  bot.check(a)



