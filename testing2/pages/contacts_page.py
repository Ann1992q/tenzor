from base_page import BasePage
from selenium.webdriver.common.by import By



class ContactsPage(BasePage):
    """
    Page Object для работы с кнопкой 'Контакты' на главной странице Saby.ru.
    
    Предоставляет методы для поиска, проверки отображения и клика по кнопке 'Контакты',
    а также взаимодействия с выпадающим меню (например, кнопкой 'ещё').

    Attributes:
        contacts (tuple): Локатор кнопки "Контакты" в хедере сайта.
        contacts_more (tuple): Локатор стрелки раскрытия меню "ещё".
    """
    
    contacts = (By.CLASS_NAME, 'sbis_ru-Header__menu-link')
    contacts_more = (By.CLASS_NAME, 'sbisru-Header-ContactsMenu__arrow-icon')

    def btn_contacts(self):
        """Находит видимую кнопку 'Контакты'."""
        return self.find_visible(*self.contacts)

    def btn_contacts_is_displayed(self):
        """Проверяет, отображается ли кнопка 'Контакты'."""
        self.btn_contacts()
        return True
        
    def btn_contacts_click(self):
        """Кликает по кнопке 'Контакты'."""
        btn = self.find_clickable(*self.contacts)
        btn.click()

    def btn_contacts_more(self):
        """Находит видимый элемент меню 'ещё'."""
        return self.find_visible(*self.contacts_more)

    def btn_contacts_more_click(self):
        """Кликает по стрелке меню 'ещё'."""
        btn = self.find_clickable(*self.contacts_more)
        btn.click()

   