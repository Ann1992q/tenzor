from selenium import webdriver
from pages.contacts_page import ContactsPage
from pages.strengthInPeoplr_page import StrengthPage
from pages.tenzor_page import TenzorPage
from pages.weAreWorking_page import WorkingPage
from pages.regions_page import RegionsPage
from pages.download_page import DownloadPage
from pages.saby_plugin_page import SabyPluginPage
from selenium.webdriver.chrome.options import Options
import pytest
import os

def _configure_browser(download_dir: str = None):
    """Конфигурирует опции Chrome для автоматизации и загрузок.

    Args:
        download_dir: Путь к директории для загрузок.

    Returns:
        Options: Настроенные опции Chrome.
    """
    chrome_options = Options()

    if download_dir:
        prefs = {
            "download.default_directory": download_dir,
            "download.prompt_for_download": False,       # Не спрашивать "Сохранить"
            "download.directory_upgrade": True,
            "safebrowsing.enabled": True,
            "profile.default_content_settings.popups": 0,
            "profile.content_settings.exceptions.automatic_downloads": [
                {"setting": 1, "origin": "*"}
            ]
        }
        chrome_options.add_experimental_option("prefs", prefs)

    # Отключаем флаг автоматизации
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    return chrome_options

@pytest.fixture()
def browser():
    """Фикстура запуска браузера без настройки директории загрузок."""
    options = _configure_browser()
    chrome_browser = webdriver.Chrome(options=options)
    chrome_browser.implicitly_wait(10)
    yield chrome_browser
    chrome_browser.quit()



@pytest.fixture()
def browser_with_download(request):
    """Фикстура запуска браузера с настройкой директории загрузок.

    Args:
        request: Объект pytest.request для получения пути теста.

    Yields:
        WebDriver: Настроенный экземпляр браузера.
    """
    download_dir = os.path.join(os.path.dirname(request.path), "downloads")
    os.makedirs(download_dir, exist_ok=True)

    options = _configure_browser(download_dir)
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


# === Вспомогательные фабличные функции ===

def _open_saby_page(browser, page_class):
    """
    Вспомогательная фабричная функция для открытия страниц Saby.ru.
    
    Args:
        browser: Экземпляр WebDriver.
        page_class: Класс страницы (например, ContactsPage).

    Returns:
        page_class: Инициализированный экземпляр страницы.
    """
    page = page_class(browser)
    page.open("https://saby.ru")
    return page

def _open_contacts_page(browser, page_class):
    """
    Вспомогательная фабричная функция для открытия страницы https://saby.ru/contacts. 
    
    Args:
        browser: Экземпляр WebDriver.
        page_class: Класс страницы (например, TenzorPage, RegionsPage).

    Returns:
        page_class: Инициализированный экземпляр нужной страницы.
    """
    page = page_class(browser)
    page.open("https://saby.ru/contacts")
    return page

# === Фикстуры страниц ===
@pytest.fixture
def contacts_page(browser):
    """
    Фикстура для работы с разделом 'Контакты' на главной странице Saby.ru.

    Returns:
        ContactsPage: Страница с кнопкой 'Контакты'.
    """
    return _open_saby_page(browser, ContactsPage)

@pytest.fixture
def strengthInPeoplr_page(browser):
    """
    Фикстура для работы с блоком 'Сила в людях' на главной странице Tensor.ru.

    Returns:
        StrengthPage: Страница с блоком 'Сила в людях'.
    """
    url = "https://tensor.ru/"
    page = StrengthPage(browser)
    page.open(url)
    return page

@pytest.fixture
def tenzor_page(browser):
    """
    Фикстура для работы с баннером 'Тензор' на странице контактов Saby.ru.

    Returns:
        TenzorPage: Страница с баннером 'Тензор'.
    """
    return _open_contacts_page(browser, TenzorPage)

@pytest.fixture
def working_page(browser):
    """
    Фикстура для работы с разделом 'Работаем' на странице tensor.ru/about.

    Returns:
        WorkingPage: Страница с разделом 'Работаем'.
    """
    url = "https://tensor.ru/about"
    page = WorkingPage(browser)
    page.open(url)
    return page

@pytest.fixture
def region_page_contacts(browser):
    """
    Фикстура для работы с регионами на главной странице saby.ru.

    Returns:
        RegionsPage: Страница с регионами.
    """
    return _open_saby_page(browser, RegionsPage)

@pytest.fixture
def region_page(browser):
    """
    Фикстура для работы с регионами на странице контактов Saby.ru.

    Returns:
        RegionsPage: Страница с регионами на странице контактов.
    """
    return _open_contacts_page(browser, RegionsPage)

@pytest.fixture
def download_page(browser):
    """
    Фикстура для работы с кнопкой 'Скачать локальные версии' на saby.ru.

    Returns:
        DownloadPage: Страница с кнопкой 'Скачать'.

    """
    return _open_saby_page(browser, DownloadPage)

@pytest.fixture
def plugin_page(browser_with_download, request):
    """
    Фикстура для работы с плагином СБИС на странице загрузки.

    Args:
        browser_with_download (WebDriver): Браузер с настройками загрузки.
        request: pytest request object для получения пути теста.

    Returns:
        SabyPluginPage: Страница с плагином СБИС.
    """
    url = "https://saby.ru/download?tab=plugin&innerTab=default"
    test_dir = os.path.dirname(request.path)
    page = SabyPluginPage(browser_with_download, test_dir=test_dir)
    page.open(url)
    return page