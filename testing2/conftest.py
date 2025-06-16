from selenium.webdriver.remote.webdriver import WebDriver
from selenium import webdriver
from selenium.webdriver.common.by import By
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
    chrome_options = Options()

    if download_dir:
        prefs = {
            "download.default_directory": download_dir,
            "download.prompt_for_download": False,       # ❌ Не спрашивать "Сохранить"
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
    options = _configure_browser()
    chrome_browser = webdriver.Chrome(options=options)
    chrome_browser.implicitly_wait(10)
    yield chrome_browser
    chrome_browser.quit()



@pytest.fixture()
def browser_with_download(request):
    download_dir = os.path.join(os.path.dirname(request.path), "downloads")
    os.makedirs(download_dir, exist_ok=True)

    options = _configure_browser(download_dir)
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

# === Фикстуры страниц ===
@pytest.fixture
def contacts_page(browser):
    url = "https://saby.ru"
    page = ContactsPage(browser)
    page.open(url)
    return page

@pytest.fixture
def strengthInPeoplr_page(browser):
    url = "https://tensor.ru/"
    page = StrengthPage(browser)
    page.open(url)
    return page

@pytest.fixture
def tenzor_page(browser):
    url = "https://saby.ru/contacts"
    page = TenzorPage(browser)
    page.open(url)
    return page

@pytest.fixture
def working_page(browser):
    url = "https://tensor.ru/about"
    page = WorkingPage(browser)
    page.open(url)
    return page

@pytest.fixture
def region_page_contacts(browser):
    url = "https://saby.ru"
    page = RegionsPage(browser)
    page.open(url)
    return page

@pytest.fixture
def region_page(browser):
    url = "https://saby.ru/contacts"
    page = RegionsPage(browser)
    page.open(url)
    return page

@pytest.fixture
def download_page(browser):
    url = "https://saby.ru"
    page = DownloadPage(browser)
    page.open(url)
    return page

@pytest.fixture
def plugin_page(browser_with_download, request):
    url = "https://saby.ru/download?tab=plugin&innerTab=default"
    test_dir = os.path.dirname(request.path)
    page = SabyPluginPage(browser_with_download, test_dir=test_dir)
    page.open(url)
    return page