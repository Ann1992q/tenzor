from pages.contacts_page import ContactsPage
from pages.strengthInPeoplr_page import StrengthPage
from pages.tenzor_page import TenzorPage
from pages.weAreWorking_page import WorkingPage
from selenium.webdriver.common.by import By

# ЦЕЛЬ ТЕСТА: Проверить наличие кнопки "Контакты" на главной странице
def test_btn_contacts_exist(contacts_page):
    assert contacts_page.btn_contacts_is_displayed() ,"Кнопка 'Контакты' не отображается"
    print('кнопка Контакты есть на странице')

# ЦЕЛЬ ТЕСТА: Проверить кликабельность кнопки "Контакты"
# и появление дополнительных опций

def test_btn_contacts_clicked(contacts_page):
    contacts_page.btn_contacts_click()
    print('кнопка Контакты успешно нажата')
    
    # Проверяем наличие кнопки "ещё"
    assert contacts_page.btn_contacts_more().is_displayed(), "Кнопка 'ещё' не найдена"
        
    #Кликаем по кнопке "ещё"
    contacts_page.btn_contacts_more_click()
    print('Успешно выполнен переход в раздел "Контакты"')

# ЦЕЛЬ: Проверить наличие блока "Сила в людях"
def test_block_strength(strengthInPeoplr_page):
    assert strengthInPeoplr_page.block_strength_is_displayed()
    print('Блок "Сила в людях" присутствует на странице')

# Проверяем текст блока
    expected_text = "Сила в людях"
    actual_text = strengthInPeoplr_page.get_text(strengthInPeoplr_page.block_strength())
    assert actual_text == expected_text, \
        f"Ожидался текст '{expected_text}', получено: '{actual_text}'"

# ЦЕЛЬ: Проверить наличие ссылки "Подробнее" и переход по ней
def test_more_details(strengthInPeoplr_page):
    assert strengthInPeoplr_page.link_more_details_is_displayed(), "Ссылка 'Подробнее' не найдена"
    print('Ссылка "Подробнее" найдена')
    
    # Кликаем и ждём нужной страницы
    strengthInPeoplr_page.click_more_details_and_wait_for_about_page()

    assert strengthInPeoplr_page.current_url() == "https://tensor.ru/about",  \
        "URL не совпадает с ожидаемым"

# ЦЕЛЬ: Проверить наличие баннера "Тензор" на странице контактов Saby
def test_tenzor(tenzor_page):
    assert tenzor_page.btn_tenzor_is_displayed(), \
        "Баннер 'Тензор' не найден на странице"
    
    print('Баннер "Тензор" присутствует на странице')

# ЦЕЛЬ: Кликнуть по баннеру "Тензор" и перейти на сайт Tensor в новой вкладке
def test_tenzor_click(tenzor_page):
    result_url = tenzor_page.btn_tenzor_click()
    
    assert "tensor.ru" in result_url, \
        f"Ожидался домен 'tensor.ru', получено: '{result_url}'"

    print(f"Переход выполнен успешно. Текущий URL: {result_url}")

# ЦЕЛЬ: Проверить наличие раздела "Работаем"
# и убедиться, что все фотографии в этом разделе имеют одинаковый размер
def test_weAreWorking(working_page):
    
    # Проверяем наличие заголовка
    working_page.weAreWorking_title()
    print('Раздел "Работаем" присутствует на странице')

    working_page.check_all_photos_same_size()
    print('Все фотографии в разделе "Работаем" имеют одинаковый размер')
