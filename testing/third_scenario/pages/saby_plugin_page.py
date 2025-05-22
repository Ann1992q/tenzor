from pages.base_page import BasePageForSaby
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
import time
import os
import re



class SabyPluginPage(BasePageForSaby):

    BTN_SABY_PLUGIN = (By.CSS_SELECTOR, '[data-id="plugin"]')
    BTN_WINDOWS = (By.XPATH,
    '//span[contains(text(), "Windows")]/ancestor::div[@data-id="default"]')
    BTN_DOWNLOAD = (By.LINK_TEXT, 'Скачать (Exe 10.37 МБ)')


    URL = "https://saby.ru/download?tab=plugin&innerTab=default "

    def __init__(self, browser: WebDriver, test_dir: str):
        super().__init__(browser, test_dir)

    def open_page(self):
        self.open(self.URL)

    def click_saby_plugin(self):
        self.find(*self.BTN_SABY_PLUGIN).click()

    def select_windows_if_not_selected(self):
        element = self.find(*self.BTN_WINDOWS)
        if 'controls-Checked__checked' not in element.get_attribute('class'):
            print("Windows не выбрана — выбираем")
            element.click()
        else:
            print("Windows уже выбрана")

    def click_download(self):
        self.find(*self.BTN_DOWNLOAD).click()

    #Размер скаченного файла
    def get_downloaded_file_size(self, extension: str = ".exe") -> float:
        download_dir = self.get_download_directory()
        for file in os.listdir(download_dir):
            if file.endswith(extension) and not file.endswith(".crdownload"):
                file_path = os.path.join(download_dir, file)
                size_bytes = os.path.getsize(file_path)
                return round(size_bytes / (1024 * 1024), 2)
        raise FileNotFoundError("Файл не найден")
    
    #Размер файла на сайте
    def get_file_size_from_site(self) -> float:
        text = self.find(*self.BTN_DOWNLOAD).text.strip()
        match = re.search(r'(\d+[\.,]?\d*)\s*[МM][БB]', text, re.IGNORECASE)
        if not match:
            raise ValueError("Не удалось найти размер файла на кнопке")
        size_str = match.group(1).replace(',', '.')
        return float(size_str)
       
    
    