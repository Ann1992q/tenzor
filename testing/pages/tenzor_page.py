from base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException


class TenzorPage(BasePage):
    """
    Page Object для работы с баннером 'Тензор' на странице контактов Saby.ru.

    Предоставляет методы для проверки отображения баннера,
    клика по нему и ожидания открытия новой вкладки с сайтом tensor.ru.

    Attributes:
        tenzor (tuple): Локатор ссылки или кнопки "Тензор" на странице.
    """
    
    tenzor = (By.CSS_SELECTOR, '.sbisru-Contacts__border-left--border-xm > a')
     
    def btn_tenzor(self):
        """Находит видимый элемент баннера 'Тензор'."""
        return self.find_visible(*self.tenzor)
       
    
    def btn_tenzor_is_displayed(self):
        """Проверяет, отображается ли баннер 'Тензор'."""
        element = self.btn_tenzor()
        return True
    
    def btn_tenzor_click(self):
        """
        Кликает по баннеру 'Тензор', ожидает открытия новой вкладки и переключается на неё.

        Returns:
            str: URL новой страницы после перехода.
        
        Raises:
            TimeoutException: Если не открылось новое окно или не загрузился нужный URL.
            Exception: Если элемент остаётся недоступным после нескольких попыток.
        """
        
        original_window = self.browser.current_window_handle

        # Находим и кликаем по кнопке с защитой от stale element
        for _ in range(3): # попробуем максимум 3 раза
            try:
                btn = self.find_clickable(*self.tenzor)
                btn.click()
                break # если успешно — выходим из цикла
            except StaleElementReferenceException:
                continue # иначе повторяем поиск
        else:
            raise Exception("Не удалось кликнуть по элементу — StaleElementReferenceException")

        # Ждём появления нового окна
        WebDriverWait(self.browser, 10).until(
            EC.new_window_is_opened([original_window])
        )

        # Переключаемся на новое окно
        for window in self.browser.window_handles:
            if window != original_window:
                self.browser.switch_to.window(window)
                break

        # проверяем URL
        WebDriverWait(self.browser, 10).until(
            EC.url_contains("tensor.ru"),
            message="Не произошёл переход на сайт Тензор"
        )

        return self.browser.current_url
        
    