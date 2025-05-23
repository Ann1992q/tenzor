from selenium import webdriver 
import pytest

# Определяем фикстуру browser, которая будет использоваться в тестах
@pytest.fixture()
def browser():
    # Создаем экземпляр Chrome-браузера
    chrome_browser = webdriver.Chrome()
    chrome_browser.implicitly_wait(10)
    # Возвращаем объект браузера в тест через yield
    # Тесты будут выполняться после этого шага
    yield chrome_browser
    # После завершения теста закрываем браузер
    chrome_browser.quit() # закрывает браузер после теста


   

