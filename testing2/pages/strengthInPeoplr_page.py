from base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class StrengthPage(BasePage):

    """
    Page Object для работы с блоком "Сила в людях" на главной странице Tensor.ru.
    
    Предоставляет методы для проверки отображения блока,
    клика по ссылке "Подробнее" и ожидания перехода на нужную страницу.

    Attributes:
        strength (tuple): Локатор заголовка блока "Сила в людях".
        more_details (tuple): Локатор ссылки "Подробнее" под блоком.
    """
    
    
    strength = (By.CSS_SELECTOR, '.tensor_ru-Index__block4-content > p:first-of-type')
    
    more_details = (By.CSS_SELECTOR, '.tensor_ru-Index__block4-content .tensor_ru-link') 
    
    def __init__(self, browser):
        """
        Инициализирует экземпляр StrengthPage.

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

    def block_strength(self):
        """
        Ожидает появления блока 'Сила в людях', прокручивает к нему и возвращает
        как WebElement.

        :return: Найденный и видимый элемент блока "Сила в людях"
        :rtype: selenium.webdriver.remote.webelement.WebElement
        :raises selenium.common.exceptions.TimeoutException:
            Если элемент не найден или не стал видимым за заданное время
        """
        
        element = WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located(self.strength)
        )
        self.browser.execute_script("arguments[0].scrollIntoView();", element)
        
        return element
    
    
    def block_strength_is_displayed(self):
        """
        Проверяет, отображается ли блок 'Сила в людях' на странице.

        :return: True, если блок виден пользователю, иначе False
        :rtype: bool
        """
        return self.block_strength().is_displayed()
    
 
    def link_more_details(self):
        """
        Ожидает появления ссылки 'Подробнее' и возвращает её как WebElement.

        :return: Элемент ссылки "Подробнее"
        :rtype: selenium.webdriver.remote.webelement.WebElement
        :raises selenium.common.exceptions.TimeoutException:
            Если ссылка не стала видимой за заданное время
        """
        return WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located(self.more_details)
        )

    def link_more_details_is_displayed(self):
        """
        Проверяет, отображается ли ссылка 'Подробнее' на странице.

        :return: True, если ссылка видна пользователю, иначе False
        :rtype: bool
        """
        return self.link_more_details().is_displayed()
       
    def click_more_details_and_wait_for_about_page(self):
        """
        Кликает по ссылке 'Подробнее' и ожидает перехода на страницу
        "https://tensor.ru/about". 
        
        :raises selenium.common.exceptions.TimeoutException:
            Если переход на указанный URL не произошёл за заданное время
        """
        self.link_more_details().click()
        WebDriverWait(self.browser, 10).until(
            EC.url_to_be("https://tensor.ru/about")
        )