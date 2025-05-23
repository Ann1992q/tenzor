from selenium import webdriver 
import pytest

@pytest.fixture()
def browser():
    chrome_browser = webdriver.Chrome()
    chrome_browser.implicitly_wait(10)
    # Передаём управление браузером в тест
    yield chrome_browser  # передаёт браузер в тест
    chrome_browser.quit() # закрывает браузер после теста


   

