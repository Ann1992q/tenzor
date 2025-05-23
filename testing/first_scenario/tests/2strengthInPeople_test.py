from selenium import webdriver 
from pages.strengthInPeoplr_page import StrengthButtonPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# ЦЕЛЬ: Проверить наличие блока "Сила в людях"
def test_block(browser):
    page_strengthInPeople = StrengthButtonPage(browser)
    # Открываем главную страницу Tensor
    page_strengthInPeople.open()
    # Проверяем отображение блока "Сила в людях"
    assert page_strengthInPeople.block_strength_is_displayed()
    print('Блок "Сила в людях" присутствует на странице')


# ЦЕЛЬ: Проверить наличие ссылки "Подробнее" и переход по ней
def test_link(browser):
    page_strengthInPeople = StrengthButtonPage(browser)
    page_strengthInPeople.open()
    # Проверяем отображение ссылки "Подробнее"
    assert page_strengthInPeople.more_details_is_displayed(), \
        "Ссылка 'Подробнее' не найдена на странице"
    
    print('Ссылка "Подробнее" присутствует на странице')

      
    # Кликаем по ссылке "Подробнее"
    page_strengthInPeople.more_details().click()

       
    # Явное ожидание загрузки целевой страницы
    WebDriverWait(browser, 10).until(
        EC.url_to_be("https://tensor.ru/about")
    )

    # Проверяем текущий URL
    current_url = browser.current_url
    print("Current URL after transition:", current_url)

    assert current_url == "https://tensor.ru/about", \
        f"Ожидался URL 'https://tensor.ru/about', получен: '{current_url}'"

    print('Переход на страницу "https://tensor.ru/about" выполнен успешно')
        
       