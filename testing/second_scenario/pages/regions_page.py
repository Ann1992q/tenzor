from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class RegionsPage(BasePage):
    # Локаторы элементов на странице контактов Saby
    button_contacts = (By.CLASS_NAME, 'sbis_ru-Header__menu-link')
    button_contacts_more = (By.CLASS_NAME, 'sbisru-Header-ContactsMenu__arrow-icon')
    
    my_region = (By.CSS_SELECTOR, '.sbis_ru-Region-Chooser.ml-16.ml-xm-0 > .sbis_ru-Region-Chooser__text.sbis_ru-link')
    partner_items_locator = (By.CSS_SELECTOR, '[data-qa="item"]')
    kamchatkaKrai = (By.CSS_SELECTOR, '[title="Камчатский край"]')
    partner_items_locatorKK = (By.CSS_SELECTOR, '[title="Saby - Камчатка"]')
    
    
    def __init__(self, browser):
        super().__init__(browser)

    def open(self):
        self.browser.get('https://saby.ru')

    def button1(self):
        return self.find(*self.button_contacts)
    
    def button2(self):
        return self.find(*self.button_contacts_more)
    
    def region(self):
        # Ожидает появления региона и возвращает его текст
        element = WebDriverWait(self.browser, 15).until(
            EC.visibility_of_element_located(self.my_region)
        )
        region_text = element.text.strip()
        print(f"Текущий регион: {region_text}")
        return region_text
    
    def get_partner_names(self):
        # Возвращает список названий партнёров в текущем регионе
        elements = self.browser.find_elements(*self.partner_items_locator)
        names = [el.text.strip() for el in elements if el.text.strip()]
        return names
    
    def get_partner_namesKK(self):
        # Возвращает список названий партнёров для Камчатского края
        elements = self.browser.find_elements(*self.partner_items_locatorKK)
        names = [el.text.strip() for el in elements if el.text.strip()]
        return names
    

    
    