from base_page import BasePage
from selenium.webdriver.common.by import By


class StrengthPage(BasePage):

    """
    Page Object для работы с блоком "Сила в людях" на главной странице Tensor.ru.
    
    Предоставляет методы для проверки отображения блока,
    клика по ссылке "Подробнее" и ожидания перехода на нужную страницу.

    Attributes:
        strength (tuple): Локатор заголовка блока "Сила в людях".
        more_details (tuple): Локатор ссылки "Подробнее" под блоком.
    """
        
    strength = (By.CSS_SELECTOR, '.tensor_ru-Index__block4-content > p:first-of-type')
    more_details = (By.CSS_SELECTOR, '.tensor_ru-Index__block4-content .tensor_ru-link') 
    
    def block_strength(self):
        """Находит заголовок 'Сила в людях' и прокручивает к нему."""
        element = self.find_visible(*self.strength)
        self.scroll_to(*self.strength)
        return element
    
    
    def block_strength_is_displayed(self):
        """Проверяет, отображается ли блок 'Сила в людях'."""
        self.block_strength()
        return True
    
 
    def link_more_details(self):
        """Находит ссылку 'Подробнее'."""
        element = self.find_visible(*self.more_details)
        return element
        

    def link_more_details_is_displayed(self):
        """Проверяет, отображается ли ссылка 'Подробнее'."""
        self.link_more_details()
        return True
       
    def click_more_details_and_wait_for_about_page(self):
        """Кликает по ссылке 'Подробнее' и ожидает перехода на /about."""
        btn = self.find_clickable(*self.more_details)
        btn.click()
        self.wait_for_url("https://tensor.ru/about")
       