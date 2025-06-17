from selenium import webdriver 
from selenium.webdriver.common.by import By
from pages.download_page import DownloadPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.saby_plugin_page import SabyPluginPage
import time
import os


#ЦЕЛИ:
# 1. Переход на saby.ru и в Footer'e поиск и переход на "Скачать локальные версии"
# 2. Скачать плагин для WINDOWS, веб-установщикв папку с данным тестом
# 3. Убедиться, что плагин скачался
# 4. Сравнить размер скачанного файла в мегабайтах с тем, что на сайте


def test_button_download(download_page):
    """Проверяет наличие ссылки 'Скачать локальные версии'."""   
    assert download_page.is_download_link_displayed(), '"Скачать локальные версии" не найдена на странице'
    print('"Скачать локальные версии" есть на странице')
    
    
def test_link_download_clicked(download_page):
    """Проверяет переход по ссылке 'Скачать локальные версии'."""
    download_page.click_download_link()
    assert "download" in download_page.current_url(), "Не перешли на страницу загрузки"
    print('Ссылка кликабельна. Выполнен переход на страницу загрузки')


def test_download_saby_plugin(plugin_page):
    """Проверяет скачивание плагина СБИС для Windows и сравнивает размер."""
    print("URL страницы:", plugin_page.current_url())
    print("Папка загрузки:", plugin_page.get_download_directory())

    plugin_page.click_saby_plugin()
    plugin_page.select_windows_if_not_selected()
    plugin_page.click_download()

    # Ждём несколько секунд, чтобы убедиться, что загрузка началась
    time.sleep(5)

    try:
        downloaded_file = plugin_page.get_downloaded_file_size(timeout=60)
        print(f"Файл успешно скачан: {downloaded_file} МБ")
    except TimeoutError:
        print("Файл не был загружен")
        print("Содержимое папки:", os.listdir(plugin_page.get_download_directory()))
        raise
    
     # Размер файла с сайта
    expected_size_mb = plugin_page.get_file_size_from_site()
    print(f"Размер файла на сайте: {expected_size_mb} МБ")

    # Сравнить размеры
    tolerance = 0.1  # допуск в 0.1 МБ
    assert abs(downloaded_file - expected_size_mb) <= tolerance, \
        f"Размер отличается более чем на {tolerance} МБ"

    print("Размер файла совпадает с указанным на сайте")
    
   


    