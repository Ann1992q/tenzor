from pages.base_page import BasePage
from selenium.webdriver.common.by import By


# Класс для работы с кнопками контактов на главной странице Saby
class ContactsButtonPage(BasePage):
    # Локатор для первой кнопки "Контакты" в меню заголовка
    button_contacts = (By.CLASS_NAME, 'sbis_ru-Header__menu-link')
    
    # Локатор для кнопки "ещё" внутри кнопки контакты
    button_contacts_more = (By.CLASS_NAME, 'sbisru-Header-ContactsMenu__arrow-icon')

    def __init__(self, browser):
        # Передаем экземпляр браузера в конструктор базового класса
        super().__init__(browser)

    def open(self):
        # Открывает главную страницу Saby
        self.browser.get('https://saby.ru')

    def button1(self):
        # Находит первую кнопку "Контакты"
        return self.find(*self.button_contacts)

    def button1_is_displayed(self):
        # Проверяет, отображается ли кнопка "Контакты"
        return self.button1().is_displayed()

    def button2(self):
        # Находит кнопку "ещё" в меню контактов
        return self.find(*self.button_contacts_more)