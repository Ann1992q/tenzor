from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os


class BasePage:
    def __init__(self, browser):
        self.browser = browser

    def find(self, *args):
        return self.browser.find_element(*args)


class BasePageForSaby:
    """Инициализирует страницу Saby с учётом директории теста.
        
        :param browser: экземпляр драйвера Selenium
        :param test_dir: директория, из которой запускается тест
    """
    def __init__(self, browser: WebDriver, test_dir: str):
        self.browser = browser
        self.test_dir = test_dir
        # Создаём папку downloads относительно текущего теста
        self.download_dir = os.path.join(test_dir, "downloads")
        os.makedirs(self.download_dir, exist_ok=True)

    def find(self, by, value, timeout=15):
        return WebDriverWait(self.browser, timeout).until(
            EC.element_to_be_clickable((by, value))
        )

    def get_download_directory(self) -> str:
        """Возвращает путь к папке, куда будут скачиваться файлы в этом тесте."""
        return self.download_dir

    def open(self, url: str):
        self.browser.get(url)