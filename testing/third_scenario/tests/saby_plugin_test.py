import os
import time
import pytest
from pages.saby_plugin_page import SabyPluginPage


def wait_for_file(download_dir, extension=".exe", timeout=30):
    start_time = time.time()
    while time.time() - start_time < timeout:
        files = os.listdir(download_dir)
        for file in files:
            if file.endswith(extension) and not file.endswith(".crdownload"):
                return os.path.join(download_dir, file)
        time.sleep(1)
    raise TimeoutError(f"Файл с расширением {extension} не найден за {timeout} секунд")


def test_download_saby_plugin(browser, request):
    test_dir = os.path.dirname(request.path)
    page = SabyPluginPage(browser, test_dir)

    # Открыть страницу
    page.open_page()

    time.sleep(5)

    # Выбрать раздел и ОС
    page.click_saby_plugin()
    time.sleep(5)
    
    # Убедиться, что Windows выбрана
    page.select_windows_if_not_selected()

    # Нажать на кнопку скачать
    page.click_download()
   
    # Ждать появления файла
    downloaded_file = wait_for_file(page.get_download_directory())

    # Проверить, что файл существует
    assert os.path.exists(downloaded_file), "Файл не был загружен"
    print(f"Файл успешно скачан: {downloaded_file}")

    
#Сравниваем размеры скаченного файла и файла на сайте
    
    #Размер скаченного файла
    actual_size = page.get_downloaded_file_size()
    print(f"Фактический размер файла: {actual_size} МБ")

    #Размер файла с сайта
    expected_size_mb = page.get_file_size_from_site() 

    # Сравнение
    tolerance = 0.1
    assert abs(actual_size - expected_size_mb) <= tolerance, \
        f"Размер отличается более чем на {tolerance} МБ"
    print("Размер файла совпадает с указанным на сайте")



    