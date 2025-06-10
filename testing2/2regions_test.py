from selenium import webdriver 
from selenium.webdriver.common.by import By
from pages.regions_page import RegionsPage
from pages.contacts_page import ContactsPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest


#ЦЕЛЬ: Переход в раздел "Контакты"
def test_button_contacts(region_page_contacts):
    region_page_contacts.click_button_contacts()
    print('Кнопка "Контакты" успешно нажата')
   
    # Кликаем по кнопке "ещё"

    region_page_contacts.click_button_contacts_more()
    print('Кнопка "Контакты-еще" кликабельна.')
    current_url = region_page_contacts.get_current_url()
    print(f"Текущий URL: {current_url}")
    print('Успешно выполнен переход в раздел "Контакты"')

#ЦЕЛЬ: Проверить, что определился ваш регион и список партнеров
# Получаем текущий регион
def test_current_region(region_page):
    initial_region = region_page.get_current_region_text()
    print(f"Текущий регион: {initial_region}")

    # Получаем список партнеров
def test_partner_names(region_page):
    partner_names = region_page.get_partner_names()
    print("Найденные партнеры:")
    for name in partner_names:
        print(f"- {name}")
        
#ЦЕЛЬ: Выбор региона "Камчатский край" и проверка списка партнеров
def test_select_kamchatka_region(region_page):   
    region_page.select_region("Камчатский край")

# ЦЕЛЬ: Проверить, что URL и TITLE содержат информацию о выбранном регионе
    WebDriverWait(region_page.browser, 15).until(
        lambda driver: "kamchatskij-kraj" in driver.current_url.lower()
    )

    print("URL содержит информацию о Камчатском крае")
          
    # Проверяем, что заголовок страницы содержит "Камчатский край"
    WebDriverWait(region_page.browser, 10).until(
        lambda driver: "Камчатский край" in driver.title
    )
    new_title = region_page.browser.title
    assert "Камчатский край" in new_title, f"Заголовок не содержит 'Камчатский край': {new_title}"
    print(f"Заголовок содержит информацию о регионе: {new_title}")
