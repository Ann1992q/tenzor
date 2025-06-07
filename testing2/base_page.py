from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By



class BasePage:
    def __init__(self, browser):
        self.browser: WebDriver = browser

    def find(self, by: By, value: str):
        return self.browser.find_element(by, value)
    

