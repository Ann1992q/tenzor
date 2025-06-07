from base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TenzorPage(BasePage):
    """
    Page Object для работы с баннером 'Тензор' на странице контактов Saby.ru.

    Предоставляет методы для проверки отображения баннера,
    клика по нему и ожидания открытия новой вкладки с сайтом tensor.ru.

    Attributes:
        tenzor (tuple): Локатор ссылки или кнопки "Тензор" на странице.
    """
    
    tenzor = (By.CSS_SELECTOR, '.sbisru-Contacts__border-left--border-xm > a')
        
    def __init__(self, browser):
        """
        Инициализирует экземпляр TenzorPage.

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

    def btn_tenzor(self):
        """
        Ожидает появления баннера 'Тензор' и возвращает его как WebElement.

        :return: Найденный и видимый элемент баннера "Тензор"
        :rtype: selenium.webdriver.remote.webelement.WebElement
        :raises selenium.common.exceptions.TimeoutException:
            Если элемент не стал видимым за заданное время
        """
        return WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located(self.tenzor),
            message=f"Не удалось найти элемент по локатору {self.tenzor}"
        )
    
    def btn_tenzor_is_displayed(self):
        """
        Проверяет, отображается ли баннер 'Тензор' на странице.

        Перед проверкой повторно ищет элемент, чтобы избежать ошибки 
        StaleElementReferenceException. Ожидает появления элемента до 10 секунд.

        :return: True, если элемент видим для пользователя, иначе False
        :rtype: bool
        :raises selenium.common.exceptions.TimeoutException:
            Если элемент не найден за указанное время ожидания
        """
        element = WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located(self.tenzor)
        )
        return element.is_displayed()
    
    def btn_tenzor_click(self):
        """
        Кликает по баннеру 'Тензор', открывает ссылку в новой вкладке и
        переключается на неё.

        :return: URL новой страницы после перехода
        :rtype: str
        :raises selenium.common.exceptions.TimeoutException:
            Если новая вкладка не открылась или не произошёл переход на домен tensor.ru
        """
        original_window = self.browser.current_window_handle

        self.btn_tenzor().click()

        # Ждём появления нового окна
        WebDriverWait(self.browser, 10).until(
            EC.new_window_is_opened
        )

        # Переключаемся на новое окно
        for window in self.browser.window_handles:
            if window != original_window:
                self.browser.switch_to.window(window)
                break

        # проверяем URL
        WebDriverWait(self.browser, 10).until(
            EC.url_contains("tensor.ru"),
            message="Не произошёл переход на сайт Тензор"
        )

        return self.browser.current_url
        
    