from selenium import webdriver

from src.bot import SpiegelBot

PATH_TO_DRIVER = "C:/Windows/chromedriver.exe"

driver = webdriver.Chrome(PATH_TO_DRIVER)

categories = ["politik","panorama","sport", "wirtschaft","netzwelt","wissenschaft"\
              "auto","kultur","geschichte","leben","karriere"]

bot = SpiegelBot(driver)

bot.check(categories[0])

