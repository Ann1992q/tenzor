from selenium import webdriver 
from selenium.webdriver.common.by import By
from pages.contacts_page import ContactsButtonPage
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest

#ЦЕЛЬ: ПЕРЕХОД В РАЗДЕЛ "КОНТАКТЫ";
#ПРОВЕРКА, ЧТО ОПРЕДЕЛИЛСЯ ТВОЙ РЕГИОН И СПИСОК ПАРТНЕРОВ;
#ИЗМЕНЕНИЕ ТЕКУЩЕГО РЕГИОНА НА КАМЧАТСКИЙ КРАЙ, СПИСКА ПАРТНЕРОВ
#URL И TITLE СОДЕРЖИТ ИНФОРМАЦИЮ ВЫБРАННОГО РЕГИОНА



#Переход в раздел "Контакты"
def test_button_contacts(browser):
    page_contacts = ContactsButtonPage(browser)
    page_contacts.open()
    page_contacts.button1().click()
        
    #Поиск кнопки "Контакты-еще"
    assert page_contacts.button2()
    page_contacts.button2().click()
    time.sleep(5)
    print('Переход в раздел "Контакты".')

      
    # Получаем и выводим регион
    myRegion = page_contacts.region()
    
    
    # Получаем список партнеров
    partner_names = page_contacts.get_partner_names()
    print("Найденные партнеры:")
    for name in partner_names:
        print(f"- {name}")

    # Проверка, что список не пустой
    assert len(partner_names) > 0, "Список партнеров пуст или не найден"
    print(f"Найдено партнеров: {len(partner_names)}")


    #Изменение текущего региона на Камчатский край
    #Клик по текущему региону
    current_region = browser.find_element(*page_contacts.my_region)
    current_region.click()
    #Выбор региона Камчатский край
    kamchatka = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable(page_contacts.kamchatkaKrai)
    )
    
    # Сохраняем URL (мой регион)
    initial_url = browser.current_url
    print(f"Исходный URL: {initial_url}")

    initial_region = page_contacts.region()
    
    print("Клик по Камчатскому краю")
    time.sleep(3)
    kamchatka.click()
    
    time.sleep(3)

    new_region = browser.find_element(*page_contacts.my_region).text
    time.sleep(3)
    print(f"Регион после клика: {new_region}")
    time.sleep(3)

    assert new_region == "Камчатский край", f"Ожидался 'Камчатский край', получили '{new_region}'"
    time.sleep(3)
    # Находим актуальный регион и выводим его текст
    current_region_after = browser.find_element(*page_contacts.my_region)
    print(f"Текущий регион после изменения: {current_region_after.text}")

    #Проверка, что список партнеров изменился
    partner_namesKK = page_contacts.get_partner_namesKK()
    print("Найденные партнеры:")
    for name in partner_namesKK:
        print(f"- {name}")

    # Проверка, что список не пустой
    assert len(partner_namesKK) > 0, "Список партнеров пуст или не найден"
    print(f"Найдено партнеров: {len(partner_namesKK)}")

    # Ждём изменения URL
    try:
        WebDriverWait(browser, 10).until(
            lambda driver: driver.current_url != initial_url
        )
        new_url = browser.current_url
        print(f"Новый URL: {new_url}")
    except:
        pytest.fail("URL не изменился после выбора региона Камчатский край")

    # Проверяем, что URL содержит информацию о Камчатском крае
    assert "kamchatskij-kraj" in new_url.lower(), f"URL не содержит информации о Камчатском крае: {new_url}"
    
    # Проверяем, что регион изменился
    new_region_text = WebDriverWait(browser, 10).until(
        lambda driver: driver.find_element(*page_contacts.my_region).text != initial_region
    )
    # Получаем текст региона
    new_region_text = browser.find_element(*page_contacts.my_region).text
    print(f"Регион после изменения: {new_region_text}")
    assert new_region_text == "Камчатский край", f"Ожидался 'Камчатский край', получили '{new_region_text}'"

    #title содержит информацию выбранного региона
    current_title = browser.title
    assert "Камчатский край" in current_title, f"Title не содержит 'Камчатский край': {current_title}"
    print(f"Заголовок содержит информацию о регионе: {current_title}")
    
    
    
   
    

    