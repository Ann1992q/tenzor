from pages.base_page import BasePage
from selenium.webdriver.common.by import By
# Для работы с явными ожиданиями
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class StrengthButtonPage(BasePage):
    
    # Локатор блока "Сила в людях"
    block_strength = (By.CSS_SELECTOR, '.tensor_ru-Index__block4-content > p:first-of-type')
    # Локатор ссылки "Подробнее" под блоком
    link_more_details = (By.CSS_SELECTOR, '.tensor_ru-Index__block4-content .tensor_ru-link') 
    
    def __init__(self, browser):
        # Передаем экземпляр браузера в базовый класс
        super().__init__(browser)

    def open(self):
        # Открываем главную страницу Tensor
        self.browser.get('https://tensor.ru/')

    def block(self):
        # Ожидаем появление блока "Сила в людях" и прокручиваем к нему
        element = WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located(self.block_strength)
        )
        self.browser.execute_script("arguments[0].scrollIntoView();", element)
        
        # Проверяем, что текст соответствует ожидаемому
        assert element.text.strip() == "Сила в людях", \
            f"Ожидался текст 'Сила в людях', получено: '{element.text}'"
        
        return element
    
    
    def block_strength_is_displayed(self):
        # Проверяет, отображается ли блок "Сила в людях"
        return self.block().is_displayed()
    
 
    def more_details(self):
        # Явное ожидание появления ссылки "Подробнее"
        return WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located(self.link_more_details)
        )

    def more_details_is_displayed(self):
        # Проверяет, отображается ли ссылка "Подробнее"
        return self.more_details().is_displayed()
    