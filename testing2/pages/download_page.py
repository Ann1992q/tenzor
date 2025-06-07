from base_page import BasePage
from selenium.webdriver.common.by import By


class DownloadPage(BasePage):

    # Локатор ссылки "Скачать локальные версии"  
    lk_download = (By.LINK_TEXT, 'Скачать локальные версии')


    def __init__(self, browser):
        super().__init__(browser)

    def open(self):
        self.browser.get('https://saby.ru')

    def link_download(self):
        return self.find(*self.lk_download)
    
    def link_download_is_displayed(self):
        #Проверяет, отображается ли ссылка 'Скачать локальные версии'.
        return self.link_download().is_displayed()
    
    
    