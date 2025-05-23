from selenium import webdriver 
from selenium.webdriver.common.by import By
from pages.download_page import DownloadPage


#ЦЕЛЬ: переход на https://saby.ru и
#в Footer'e поиск и переход на "Скачать локальные версии"


def test_button_download(browser):
    #Переход на https://saby.ru
    page = DownloadPage(browser)
    page.open()

   
    #Поиск элемента "Скачать локальные версии"
    assert page.link_download_is_displayed()
    print('"Скачать локальные версии" есть на странице')
    
    
    #Проверка, что ссылка "Скачать локальные версии" кликабельна
    #Переход по ссылке "Скачать локальные версии"
def test_link_download_clicked(browser):
    page = DownloadPage(browser)
    page.open()
    page.link_download().click()
    assert "download" in browser.current_url.lower(), "Не перешли на страницу загрузки"
    print('Ссылка кликабельна. Выполнен переход на страницу загрузки')

   




    