from base_page import BasePage
from selenium.webdriver.common.by import By


class RegionsPage(BasePage):
    """
    Page Object для тестирования региональных настроек на сайте Saby.ru.

    Предоставляет методы:
    - для открытия сайта
    - для взаимодействия с кнопками "Контакты"
    - для проверки текущего региона
    - для выбора региона из выпадающего списка
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
    my_region = (By.CSS_SELECTOR, '.sbis_ru-Region-Chooser.ml-16.ml-xm-0 > .sbis_ru-Region-Chooser__text.sbis_ru-link')
    partner_items_locator = (By.CSS_SELECTOR, '[data-qa="item"]')
    kamchatkaKrai = (By.CSS_SELECTOR, '[title="Камчатский край"]')
    partner_items_locatorKK = (By.CSS_SELECTOR, '[title="Saby - Камчатка"]')
    
    
    def click_button_contacts(self):
        """
        Кликает по кнопке "Контакты" в хедере сайта.

        Raises:
            TimeoutException: Если элемент не стал кликабельным за timeout.
        """
        btn = self.find_clickable(*self.button_contacts)
        btn.click()

    def click_button_contacts_more(self):
        """
        Кликает по кнопке "ещё" в меню "Контакты".

        Raises:
            TimeoutException: Если элемент не стал кликабельным за timeout.
        """
        btn = self.find_clickable(*self.button_contacts_more)
        btn.click()
    
    def get_current_url(self):
        """
        Возвращает текущий URL браузера.

        Returns:
            str: Текущий URL страницы.
        """
        return self.current_url()
    
    def get_current_region_text(self):
        """
        Получает название текущего региона из выпадающего списка.

        Returns:
            str: Название текущего региона.
        """
        element = self.find_visible(*self.my_region)
        return self.get_text(element)

    def get_partner_names(self):
        """
        Возвращает список названий партнёров в текущем регионе.

        Returns:
            list[str]: Список строк — названия партнёров.
        Raises:
            TimeoutException: Если элементы партнёров не стали видимыми за timeout.
        """
        elements = self.find_all_visible(*self.partner_items_locator)
        return [el.text.strip() for el in elements if el.text.strip()]
       
    
    def select_region(self, region_name):
        """
        Выбирает указанный регион из выпадающего списка через JS-клик.

        Args:
            region_name (str): Название региона (например, "Камчатский край").

        Raises:
            TimeoutException: Если элемент региона не стал кликабельным за timeout.
        """
        # Открыть выпадающий список регионов
        region_dropdown = self.find_visible(*self.my_region)
        region_dropdown.click()

        # Подождём появление нужного региона
        region_item = self.find_visible(*self.kamchatkaKrai)
        
        # Кликнем через JS
        self.browser.execute_script("arguments[0].click();", region_item)
        print(f"Регион '{region_name}' выбран через JS")
        import time
        time.sleep(3)
        print("Текущий URL после выбора региона:", self.current_url())
        print("Заголовок страницы:", self.browser.title)
        
            
    def get_partner_names_kamchatka(self):
        """
        Возвращает список названий партнёров в Камчатском крае.

        Returns:
            list[str]: Список строк — названия партнёров Камчатского края.
        Raises:
            TimeoutException: Если элементы партнёров не стали видимыми за timeout.
        """
        elements = self.find_all_visible(*self.partner_items_locatorKK)
        
        return [el.text.strip() for el in elements if el.text.strip()]
    
    
        

    
    