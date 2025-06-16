from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os



class BasePage:
    def __init__(self, browser: WebDriver, test_dir: str = None):
        self.browser = browser
        self.test_dir = test_dir or os.getcwd()
        # Создаём папку downloads относительно текущего теста
        self.download_dir = os.path.join(self.test_dir, "downloads")
        os.makedirs(self.download_dir, exist_ok=True)

    def open(self, url: str):
        self.browser.get(url)

    # === Методы ожидания элементов ===
    def find_clickable(self, by, value, timeout=15):
        """Ждёт, пока элемент станет кликабельным, и возвращает его"""
        return WebDriverWait(self.browser, timeout).until(
            EC.element_to_be_clickable((by, value))
        )

    def find_visible(self, by, value, timeout=15):
        """Ждёт, пока элемент станет видимым, и возвращает его"""
        return WebDriverWait(self.browser, timeout).until(
            EC.visibility_of_element_located((by, value))
        )
    
    def scroll_to(self, element):
        """Прокручивает к элементу"""
        self.browser.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)

    def find_present(self, by, value, timeout=15):
        """Ждёт появление элемента в DOM и возвращает его"""
        return WebDriverWait(self.browser, timeout).until(
            EC.presence_of_element_located((by, value))
        )
    
    def find_all_visible(self, by, value, timeout=15):
        """Ждёт появления всех элементов и возвращает их список"""
        return WebDriverWait(self.browser, timeout).until(
            EC.visibility_of_all_elements_located((by, value))
        )
    
    # === Вспомогательные методы для работы с элементами ===
    
    def get_text(self, element):
        """Возвращает текст элемента с обрезанием пробелов"""
        return element.text.strip()
    
    def get_attribute(self, element, attr_name):
        """Получает значение атрибута у элемента"""
        return element.get_attribute(attr_name)
    

    # === Работа с файлами ===

    def get_download_directory(self):
        """Возвращает путь к папке, куда будут скачиваться файлы в этом тесте"""
        return self.download_dir
    
    # === Работа с URL ===

    def wait_for_url(self, expected_url: str, timeout=15):
        """Ожидает, пока текущий URL не станет равен заданному"""
        WebDriverWait(self.browser, timeout).until(
            EC.url_to_be(expected_url),
            f"Ожидался URL '{expected_url}', но был '{self.browser.current_url}'"
        )

    def current_url(self):
        """Возвращает текущий URL браузера"""
        return self.browser.current_url

    



