# Импорты
from selenium import webdriver 
from selenium.webdriver.common.by import By
from pages.contacts_page import ContactsButtonPage
import time

# ЦЕЛЬ ТЕСТА: Проверить наличие кнопки "Контакты" на главной странице
def test_button_contacts_exist(browser):
    # Инициализируем page object
    page_contacts = ContactsButtonPage(browser)
    # Открываем главную страницу
    page_contacts.open()
    assert page_contacts.button1_is_displayed()
    print('кнопка Контакты есть на странице')

# ЦЕЛЬ ТЕСТА: Проверить кликабельность кнопки "Контакты"
# и появление дополнительных опций

def test_button_contacts_clicked(browser):
    page_contacts = ContactsButtonPage(browser)
    page_contacts.open()
    page_contacts.button1().click()
    print('кнопка Контакты успешно нажата')
    
    #Поиск кнопки "Контакты-еще"
    assert page_contacts.button2()
    print('Кнопка Контакты-еще найдена')

       
    #Кликаем по кнопке "ещё"
    page_contacts.button2().click()
    time.sleep(5)
    print('кнопка Контакты-еще кликабельна.')
    print('Успешно выполнен переход в раздел "Контакты"')
    