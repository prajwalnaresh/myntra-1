# to keep all driver initialisation we use this file
# if we want to do parallel execution or run in multiple browsers, then in conftest it will be defficult
# so we use this file to return an object of multiple web drivers (ex Android or IOS objects)
# this will return corresponding driver objects
# here we create object of webdriver
from selenium import webdriver
from Sources.utilities import globals
from Sources.utilities.properties import ReadConfig


class DriversFactory:

    def __init__(self):
        self.driver = None

    def get_web_driver(self, browser_name, url):
        if self.driver is None:
            self.driver = self.create_driver(browser_name, url)
        return self.driver

    def create_driver(self, browser_name, url):
        if browser_name == "chrome" or "ch":
            self.driver = webdriver.Chrome(executable_path=globals.CHROME_DRIVER)
        elif browser_name == "firefox" or "ff":
            self.driver = webdriver.Firefox(executable_path=globals.FIREFOX_DRIVER)
        elif browser_name == "internet explorer" or "ie":
            print("IE driver")
        self.driver.get(url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(ReadConfig.get_implicit_wait())
        return self.driver

