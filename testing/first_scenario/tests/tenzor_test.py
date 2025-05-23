from selenium import webdriver 
from selenium.webdriver.common.by import By
from pages.tenzor_page import TenzorButtonPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

#ЦЕЛЬ: "НАЙТИ БАННЕР ТЕНЗОР И КЛИКНУТЬ ПО НЕМУ"

#Поиск элемента баннер Тензор
def test_tenzor(browser):
    page_tenzor = TenzorButtonPage(browser)
    page_tenzor.open()

    assert page_tenzor.button3_is_displayed()
    print('баннер Тензор есть на странице')

#Клик по баннеру Тензор
def test_tenzor_click(browser):
    page_tenzor = TenzorButtonPage(browser)
    page_tenzor.open()
    
    original_window = browser.current_window_handle #текущее окно
    
    page_tenzor.button3().click()
    
    
    # Ожидание появления новой вкладки
    WebDriverWait(browser, 10).until(
        lambda d: len(d.window_handles) > 1
    )

    # Переключение на новую вкладку
    for window_handle in browser.window_handles:
        if window_handle != original_window:
            browser.switch_to.window(window_handle)
            break

    # Ждём, пока загрузится страница tensor.ru
    WebDriverWait(browser, 10).until(
        EC.url_contains("tensor.ru")
    )

    # Проверяем, что текущий URL содержит "tensor.ru"
    current_url = browser.current_url
    print("Current URL after switch:", current_url)
        
    
   
    
    