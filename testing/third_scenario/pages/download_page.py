from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium import webdriver



class DownloadPage(BasePage):
       
    lk_download = (By.LINK_TEXT, 'Скачать локальные версии')


    def __init__(self, browser):
        super().__init__(browser)

    def open(self):
        self.browser.get('https://saby.ru')

    def link_download(self):
        return self.find(*self.lk_download)
    
    def link_download_is_displayed(self):
        return self.link_download().is_displayed()
    
    
    