from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium import webdriver


class ContactsButtonPage(BasePage):
    button_contacts = (By.CLASS_NAME, 'sbis_ru-Header__menu-link')
    button_contacts_more = (By.CLASS_NAME, 'sbisru-Header-ContactsMenu__arrow-icon')
    
    def __init__(self, browser):
        super().__init__(browser)

    def open(self):
        self.browser.get('https://saby.ru')

    def button1(self):
        return self.find(*self.button_contacts)
    
    def button1_is_displayed(self):
        return self.button1().is_displayed()
    
    def button2(self):
        return self.find(*self.button_contacts_more)