from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver


class StrengthButtonPage(BasePage):
    
    block_strength = (By.CSS_SELECTOR, '.tensor_ru-Index__block4-content > p:first-of-type')
    link_more_details = (By.CSS_SELECTOR, '.tensor_ru-Index__block4-content .tensor_ru-link') 
    
    def __init__(self, browser):
        super().__init__(browser)

    def open(self):
        self.browser.get('https://tensor.ru/')

    def block(self):
        # Явное ожидание + прокрутка
        element = WebDriverWait(self.browser, 10).until(
            EC.visibility_of_element_located(self.block_strength)
        )
        self.browser.execute_script("arguments[0].scrollIntoView();", element)
        
        assert element.text.strip() == "Сила в людях", \
        f"Ожидался текст 'Сила в людях', получено: '{element.text}'"
        
        return element
    
    
    def block_strength_is_displayed(self):
        return self.block().is_displayed()
    
 
    def more_details(self):
        return WebDriverWait(self.browser, 10).until(
        EC.visibility_of_element_located(self.link_more_details)
    )

    def more_details_is_displayed(self):
        return self.more_details().is_displayed()
    