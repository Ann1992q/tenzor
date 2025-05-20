from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC



class TenzorButtonPage(BasePage):
    
    button_tenzor = (By.CSS_SELECTOR, '.sbisru-Contacts__border-left--border-xm > a')
        
    def __init__(self, browser):
        super().__init__(browser)

    def open(self):
        self.browser.get('https://saby.ru/contacts')

    def button3(self):
        return self.find(*self.button_tenzor)
    
    def button3_is_displayed(self):
        return self.button3().is_displayed()
    
    