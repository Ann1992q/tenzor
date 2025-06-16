from base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from utils import wait_for_file
import os
import re



class SabyPluginPage(BasePage):
    """
    Page Object для работы с плагином СБИС на странице загрузки.
    """    
    # Локаторы элементов на странице
    btn_saby_plugin = (By.CSS_SELECTOR, '[data-id="plugin"]')
    btn_win = (By.XPATH,
    '//span[contains(text(), "Windows")]/ancestor::div[@data-id="default"]')
    btn_download = (By.LINK_TEXT, 'Скачать (Exe 10.40 МБ)')

    def click_saby_plugin(self):
        plugin_btn = self.find_clickable(*self.btn_saby_plugin)
        self.scroll_to(plugin_btn)
        plugin_btn.click()

    def select_windows_if_not_selected(self):
        element = self.find_visible(*self.btn_win)
        if 'controls-Checked__checked' not in element.get_attribute('class'):
            print("Windows не выбрана — выбираем")
            element.click()
        else:
            print("Windows уже выбрана")

    def click_download(self):
        download_link = self.find_clickable(*self.btn_download)
        file_url = download_link.get_attribute('href')

        print("Нажимаем 'Скачать'")
        print(f"Текст кнопки: {download_link.text}")
        print(f"href: {file_url}")

        # Переход напрямую по ссылке
        self.browser.get(file_url)

  
    def get_downloaded_file_size(self, extension: str = ".exe", timeout: int = 60) -> float:
        download_dir = self.get_download_directory()
        downloaded_file = wait_for_file(download_dir, extension=extension, timeout=timeout)
        size_bytes = os.path.getsize(downloaded_file)
        return round(size_bytes / (1024 * 1024), 2)
          
    
    def get_file_size_from_site(self)-> float:
        """
        Парсит размер файла с кнопки 'Скачать'.
        Поддерживает форматы: 'МБ' или 'MB'
        """
        text = self.find_visible(*self.btn_download).text.strip()
        match = re.search(r'(\d+[\.,]?\d*)\s*[МM][БB]', text, re.IGNORECASE)
        if not match:
            raise ValueError("Не удалось найти размер файла на кнопке")
        size_str = match.group(1).replace(',', '.')
        return float(size_str)
       
    
    