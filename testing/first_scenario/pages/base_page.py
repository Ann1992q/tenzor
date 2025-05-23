from selenium.webdriver.remote.webdriver import WebDriver

# Базовый класс для всех страниц. 
# Служит шаблоном, от которого наследуются конкретные page-объекты.
class BasePage:
    def __init__(self, browser: WebDriver):
        # Сохраняем переданный экземпляр браузера (webdriver) в атрибут класса
        self.browser = browser

    # Упрощённый метод для поиска элемента на странице
    # Передаёт все аргументы в стандартный метод find_element Selenium
    def find(self, *args):
        return self.browser.find_element(*args)