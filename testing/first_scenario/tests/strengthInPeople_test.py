from selenium import webdriver 
from pages.strengthInPeoplr_page import StrengthButtonPage
import time


#ЦЕЛЬ: "ПРОВЕРКА НАЛИЧИЯ БЛОКА "СИЛА В ЛЮДЯХ"
#И ПЕРЕХОД В БЛОК "ПОДРОБНЕЕ"-ПЕРЕХОД НА НОВУЮ СТРАНИЦУ (https://tensor.ru/about)"

#Поиск элемента блок "Сила в людях"
def test_block(browser):
    page_strengthInPeople = StrengthButtonPage(browser)
    page_strengthInPeople.open()

    assert page_strengthInPeople.block_strength_is_displayed()
    print('блок "Сила в людях" есть на странице')

#Поиск ссылки "Подробнее"
def test_link(browser):
    page_strengthInPeople = StrengthButtonPage(browser)
    page_strengthInPeople.open()
    assert page_strengthInPeople.more_details_is_displayed()
    print('ссылка "Подробнее" есть на странице')

      
    #Переход на новую страницу по ссылке "Подробнее"
    page_strengthInPeople.more_details().click()

    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    
    # Ждём, пока загрузится страница https://tensor.ru/about
    WebDriverWait(browser, 10).until(
        EC.url_to_be("https://tensor.ru/about")
    )

    # Проверяем, что текущий URL содержит "https://tensor.ru/about"
    current_url = browser.current_url
    print("Current URL after switch:", current_url)
        
       