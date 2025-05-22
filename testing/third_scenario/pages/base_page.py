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
    def __init__(self, browser: WebDriver, test_dir: str):
        self.browser = browser
        self.test_dir = test_dir
        self.download_dir = os.path.join(test_dir, "downloads")
        os.makedirs(self.download_dir, exist_ok=True)

    def find(self, by, value, timeout=15):
        return WebDriverWait(self.browser, timeout).until(
            EC.element_to_be_clickable((by, value))
        )

    def get_download_directory(self) -> str:
        return self.download_dir

    def open(self, url: str):
        self.browser.get(url)