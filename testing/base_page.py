from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os



class BasePage:
    """Базовый класс для всех страниц проекта.

    Предоставляет общие методы для работы с элементами, навигации,
    ожидания элементов, скроллинга, работы с файлами и URL.
    """
    def __init__(self, browser: WebDriver, test_dir: str = None):
        """Инициализирует BasePage.

        Args:
            browser: Экземпляр WebDriver.
            test_dir: Путь к директории теста для сохранения загрузок.
        """
        self.browser = browser
        self.test_dir = test_dir or os.getcwd()
        # Создаём папку downloads относительно текущего теста
        self.download_dir = os.path.join(self.test_dir, "downloads")
        os.makedirs(self.download_dir, exist_ok=True)

    def open(self, url: str):
        self.browser.get(url)

    # === Методы ожидания элементов ===
    def find_clickable(self, by, value, timeout=15):
        """Ждёт, пока элемент станет кликабельным, и возвращает его.

        Args:
            by: Метод поиска (например, By.ID, By.CSS_SELECTOR).
            value: Значение локатора.
            timeout: Время ожидания в секундах.

        Returns:
            WebElement: Кликабельный элемент.
        """
        return WebDriverWait(self.browser, timeout).until(
            EC.element_to_be_clickable((by, value))
        )

    def find_visible(self, by, value, timeout=15):
        """Ждёт, пока элемент станет видимым, и возвращает его.

        Args:
            by: Метод поиска.
            value: Значение локатора.
            timeout: Время ожидания в секундах.

        Returns:
            WebElement: Видимый элемент.
        """
        return WebDriverWait(self.browser, timeout).until(
            EC.visibility_of_element_located((by, value))
        )
    
    def scroll_to(self, by, value, timeout=15):
        """
        Прокручивает страницу так, чтобы указанный элемент стал видимым.

        Находит элемент с помощью заданных локаторов и прокручивает к нему,
        используя JavaScript (arguments[0].scrollIntoView).

        Args:
            by (selenium.webdriver.common.by.By): Метод поиска элемента (например, By.ID, By.CSS_SELECTOR).
            value (str): Значение локатора, по которому будет найден элемент.
            timeout (int, optional): Время ожидания элемента в секундах. По умолчанию 15.

        Returns:
            WebElement: Найденный и прокрученный элемент.

        Raises:
            TimeoutException: Если элемент не станет видимым за указанное время.
        """
        element = self.find_visible(by,value, timeout)
        self.browser.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)

    def find_present(self, by, value, timeout=15):
        """Ждёт появление элемента в DOM и возвращает его.

        Args:
            by: Метод поиска.
            value: Значение локатора.
            timeout: Время ожидания в секундах.

        Returns:
            WebElement: Найденный элемент.
        """
        return WebDriverWait(self.browser, timeout).until(
            EC.presence_of_element_located((by, value))
        )
    
    def find_all_visible(self, by, value, timeout=15):
        """Ждёт появления всех элементов и возвращает их список.

        Args:
            by: Метод поиска.
            value: Значение локатора.
            timeout: Время ожидания в секундах.

        Returns:
            list[WebElement]: Список видимых элементов.
        """
        return WebDriverWait(self.browser, timeout).until(
            EC.visibility_of_all_elements_located((by, value))
        )
    
    def click_via_js(self, by, value):
        """Кликает по элементу с помощью JavaScript."""
        element = self.find_visible(by, value)
        self.browser.execute_script("arguments[0].click();", element)
    
    # === Вспомогательные методы для работы с элементами ===
    
    def get_text(self, element):
        """Возвращает текст элемента с обрезанием пробелов.

        Args:
            element: Целевой WebElement.

        Returns:
            str: Обработанный текст элемента.
        """
        return element.text.strip()
    
    def get_attribute(self, element, attr_name):
        """Получает значение атрибута у элемента.

        Args:
            element: Целевой WebElement.
            attr_name: Имя атрибута.

        Returns:
            str: Значение атрибута или None.
        """
        return element.get_attribute(attr_name)
    

    # === Работа с файлами ===

    def get_download_directory(self):
        """Возвращает путь к папке загрузки для текущего теста.

        Returns:
            str: Абсолютный путь к директории загрузки.
        """
        return self.download_dir
    
    # === Работа с URL ===

    def wait_for_url(self, expected_url: str, timeout=15):
        """Ожидает, пока текущий URL не станет равен заданному.

        Args:
            expected_url: Ожидаемый URL.
            timeout: Время ожидания в секундах.

        Raises:
            TimeoutException: Если URL не совпал за отведённое время.
        """
        WebDriverWait(self.browser, timeout).until(
            EC.url_to_be(expected_url),
            f"Ожидался URL '{expected_url}', но был '{self.browser.current_url}'"
        )

    def current_url(self):
        """Возвращает текущий URL браузера.

        Returns:
            str: Текущий URL.
        """
        return self.browser.current_url
    



    



