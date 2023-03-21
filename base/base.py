import time
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.wait import WebDriverWait

class Base:
    def __init__(self, driver):
        self.driver = driver

    def by_id(self, id):
        return self.driver.find_element(AppiumBy.ID, id)

    def by_xpath(self, xpath):
        return self.driver.find_element(AppiumBy.XPATH, xpath)

    def id_base_click(self, loc):
        self.by_id(loc).click()

    def send_keys(self, loc, text):
        ele = self.by_id(loc)
        ele.clear()
        ele.send_keys(text)
