from base_page import BasePage
from selenium.webdriver.common.by import By


class DownloadPage(BasePage):

    """
    Page Object для работы с кнопкой 'Скачать локальные версии' на главной странице Saby.ru.
    
    Предоставляет методы для проверки наличия и клика по ссылке "Скачать локальные версии"
    """

    # Локатор ссылки "Скачать локальные версии"  
    download_link_locator = (By.LINK_TEXT, 'Скачать локальные версии')


    def link_download(self):
        """Находит видимую ссылку 'Скачать локальные версии'.

        Returns:
            WebElement: Ссылка.
        """
        return self.find_visible(*self.download_link_locator)

    def is_download_link_displayed(self):
        """Проверяет, отображается ли ссылка 'Скачать локальные версии'.

        Returns:
            bool: True, если ссылка отображается.
        """
        self.link_download()
        return True
    
    def click_download_link(self):
        """Кликает по ссылке 'Скачать локальные версии'"""
        link = self.find_clickable(*self.download_link_locator)
        link.click()
    
    