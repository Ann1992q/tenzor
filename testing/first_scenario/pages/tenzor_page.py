from pages.base_page import BasePage
from selenium.webdriver.common.by import By



class TenzorButtonPage(BasePage):
    
    # Локатор кнопки/ссылки "Тензор" в разделе контактов Saby
    button_tenzor = (By.CSS_SELECTOR, '.sbisru-Contacts__border-left--border-xm > a')
        
    def __init__(self, browser):
        super().__init__(browser)

    def open(self):
        # Открываем страницу контактов Saby
        self.browser.get('https://saby.ru/contacts')

    def button3(self):
        # Находит кнопку "Тензор"
        return self.find(*self.button_tenzor)
    
    def button3_is_displayed(self):
        # Проверяет, отображается ли кнопка "Тензор"
        return self.button3().is_displayed()
    
    