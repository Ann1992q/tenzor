from selenium.webdriver.remote.webdriver import WebDriver
from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.contacts_page import ContactsPage
from pages.strengthInPeoplr_page import StrengthPage
from pages.tenzor_page import TenzorPage
from pages.weAreWorking_page import WorkingPage
from pages.regions_page import RegionsPage
import pytest


@pytest.fixture()
def browser():
    chrome_browser = webdriver.Chrome()
    chrome_browser.implicitly_wait(10)
    yield chrome_browser
    chrome_browser.quit()

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


