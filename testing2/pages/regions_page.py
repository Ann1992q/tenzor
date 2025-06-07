from base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class RegionsPage(BasePage):
    """
    Page Object для тестирования региональных настроек на сайте Saby.ru.

    Предоставляет методы:
    - для открытия сайта
    - для взаимодействия с кнопками "Контакты"
    - для проверки текущего региона
    - для получения списка партнёров по регионам

    Attributes:
        button_contacts (tuple): Локатор кнопки "Контакты".
        button_contacts_more (tuple): Локатор кнопки раскрытия меню "ещё".
        my_region (tuple): Локатор текста текущего региона.
        partner_items_locator (tuple): Локатор списка партнёров в текущем регионе.
        kamchatkaKrai (tuple): Локатор региона "Камчатский край".
        partner_items_locatorKK (tuple): Локатор списка партнёров Камчатского края.
    """
    button_contacts = (By.CLASS_NAME, 'sbis_ru-Header__menu-link')
    button_contacts_more = (By.CLASS_NAME, 'sbisru-Header-ContactsMenu__arrow-icon')
    my_region = (By.CSS_SELECTOR, '.sbis_ru-Region-Chooser.ml-16.ml-xm-0>span')
    partner_items_locator = (By.CSS_SELECTOR, '[data-qa="item"]')
    kamchatkaKrai = (By.CSS_SELECTOR, '[title="Камчатский край"]')
    partner_items_locatorKK = (By.CSS_SELECTOR, '[title="Saby - Камчатка"]')
    
    
    def __init__(self, browser):
        """
        Инициализирует страницу.

        :param browser: WebDriver-сессия
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

    def click_button_contacts(self):
        """
        Кликает по кнопке "Контакты".
        """
        element = WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable(self.button_contacts)
        )
        element.click()

    def click_button_contacts_more(self):
        """
        Кликает по кнопке "ещё" в меню "Контакты".
        """
        element = WebDriverWait(self.browser, 10).until(
            EC.element_to_be_clickable(self.button_contacts_more)
        )
        element.click()
    
    def get_current_url(self):
        return self.browser.current_url
    
    def get_current_region_text(self):
        """Получает текст текущего региона, каждый раз заново находя элемент."""
        element = WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located(self.my_region)
        )
        return element.text.strip()

    def get_partner_names(self):
        """
        Возвращает список названий партнёров в текущем регионе.

        :return: Список строк — названия партнёров
        :rtype: list[str]
        """
        elements = WebDriverWait(self.browser, 20).until(
            EC.presence_of_all_elements_located(self.partner_items_locator)
        )
        return [el.text.strip() for el in elements if el.text.strip()]
       
    
    def select_kamchatka_region(self):
        # 1. Открыть выпадающий список регионов
        region_dropdown = WebDriverWait(self.browser, 15).until(
            EC.element_to_be_clickable(self.my_region)
        )
        region_dropdown.click()

        # 2. Ждём появления пункта Камчатский край
        kamchatka_element = WebDriverWait(self.browser, 15).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, '[title="Камчатский край"]'))
        )

        # 3. Клик через JS
        self.browser.execute_script("arguments[0].scrollIntoView({block: 'center'});", kamchatka_element)
        self.browser.execute_script("arguments[0].click();", kamchatka_element)
        
        print("Регион 'Камчатский край' успешно выбран")
        
            
    def get_partner_names_kamchatka(self):
        """
        Возвращает список названий партнёров в Камчатском крае.

        :return: Список строк — названия партнёров
        :rtype: list[str]
        """
        elements = WebDriverWait(self.browser, 20).until(
            EC.presence_of_all_elements_located(self.partner_items_locatorKK)
        )
        
        return [el.text.strip() for el in elements if el.text.strip()]
        

    
    