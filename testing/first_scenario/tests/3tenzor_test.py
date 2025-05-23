from pages.tenzor_page import TenzorButtonPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# ЦЕЛЬ: Проверить наличие баннера "Тензор" на странице контактов Saby
def test_tenzor(browser):
    page_tenzor = TenzorButtonPage(browser)
    page_tenzor.open()

    # Проверяем отображение кнопки/баннера "Тензор"
    assert page_tenzor.button3_is_displayed(), \
        "Баннер 'Тензор' не найден на странице"
    
    print('Баннер "Тензор" присутствует на странице')

# ЦЕЛЬ: Кликнуть по баннеру "Тензор" и перейти на сайт Tensor в новой вкладке
def test_tenzor_click(browser):
    page_tenzor = TenzorButtonPage(browser)
    # Открываем страницу контактов
    page_tenzor.open()
    
    # Запоминаем текущее окно
    original_window = browser.current_window_handle #текущее окно
    
    # Кликаем по баннеру "Тензор"
    page_tenzor.button3().click()
    print('Выполнен клик по баннеру "Тензор"')
    
    
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

    # Проверяем текущий URL
    current_url = browser.current_url
    print("Current URL after switch:", current_url)

    # Убеждаемся, что мы на нужном сайте
    assert "tensor.ru" in current_url.lower(), \
        f"Ожидался домен 'tensor.ru', получен: '{current_url}'"

    print('Переход на сайт "https://tensor.ru" выполнен успешно')
        
    
   
    
    