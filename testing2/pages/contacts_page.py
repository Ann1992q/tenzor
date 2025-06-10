from base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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

    def __init__(self, browser):
        """
        Инициализирует экземпляр ContactsPage.

        :param browser: WebDriver-сессия, передаваемая из pytest-фикстуры
        :type browser: selenium.webdriver.remote.webdriver.WebDriver
        """
        super().__init__(browser)

    def open(self, url):
        """
        Открывает указанную веб-страницу в браузере.

        :param url: URL адрес целевой страницы
        :type url: str
        """
        self.browser.get(url)

    def btn_contacts(self):
        """
        Находит элемент кнопки 'Контакты' на странице.

        :return: Найденный WebElement кнопки "Контакты"
        :rtype: selenium.webdriver.remote.webelement.WebElement
        """
        return self.find(*self.contacts)

    def btn_contacts_is_displayed(self):
        """
        Проверяет, отображается ли кнопка "Контакты" на странице.

        :return: True, если кнопка видна пользователю, иначе False
        :rtype: bool
        """
        return self.btn_contacts().is_displayed()
    
    def btn_contacts_click(self):
        """
        Выполняет клик по кнопке "Контакты", чтобы открыть выпадающее меню.
        """
        self.btn_contacts().click()

    def btn_contacts_more(self):
        """
        Ожидает появления кнопки "ещё" в меню "Контакты" и возвращает её как WebElement.

        :return: Элемент кнопки "ещё"
        :rtype: selenium.webdriver.remote.webelement.WebElement
        :raises selenium.common.exceptions.TimeoutException: 
            Если элемент не найден за заданное время ожидания
        """
        return WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located(self.contacts_more),
            "Не найдена кнопка 'ещё'"
        )

    def btn_contacts_more_click(self):
        """
        Кликает по кнопке "ещё" внутри меню "Контакты".
        """
        self.btn_contacts_more().click()

   