from selenium import webdriver 
from selenium.webdriver.common.by import By
from pages.contacts_page import ContactsButtonPage
import time

#ЦЕЛЬ: ПЕРЕХОД В РАЗДЕЛ "КОНТАКТЫ"

#Проверка, что кнопка Контакты есть на странице
def test_button_contacts_exist(browser):
    page_contacts = ContactsButtonPage(browser)
    page_contacts.open()
    assert page_contacts.button1_is_displayed()
    print('кнопка Контакты есть на странице')

#Проверка, что кнопка Контакты кликабельна
def test_button_contacts_clicked(browser):
    page_contacts = ContactsButtonPage(browser)
    page_contacts.open()
    page_contacts.button1().click()
    print('кнопка Контакты кликабельна')
    
    #Поиск кнопки "Контакты-еще"
    assert page_contacts.button2()
    print('Кнопка Контакты-еще найдена')

       
    #Проверка, что кнопка Контакты-еще кликабельна
    page_contacts.button2().click()
    time.sleep(5)
    print('кнопка Контакты-еще кликабельна.')
    print('Переход в раздел "Контакты".')
    