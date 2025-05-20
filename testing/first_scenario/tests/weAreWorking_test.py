from selenium import webdriver 
from pages.weAreWorking_page import WorkingButtonPage
import time


#ЦЕЛЬ: "ПОИСК РАЗДЕЛА "РАБОТАЕМ";
# ПРОВЕРКА, ЧТО У ВСЕХ ФОТОГРАФИЙ ХРОНОЛОГИИ ОДИНАКОВЫЕ ВЫСОТА И ШИРИНА"


#Поиск элемента "раздел 'Работаем'"
def test_working(browser):
    weAreWorking_page = WorkingButtonPage(browser)
    weAreWorking_page.open()

    assert weAreWorking_page.working()
    print('раздел "Работаем" есть на странице')

    # Проверяем размеры всех фото
    weAreWorking_page.check_all_photos_same_size()

