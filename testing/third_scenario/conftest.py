import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import os


@pytest.fixture()
def browser(request):
    test_dir = os.path.dirname(request.path)
    download_dir = os.path.join(test_dir, "downloads")
    os.makedirs(download_dir, exist_ok=True)

    chrome_options = Options()
    prefs = {
        "download.default_directory": download_dir,
        "safebrowsing.enabled": "false"
    }
    chrome_options.add_experimental_option("prefs", prefs)

    driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(10)

    yield driver

    driver.quit()