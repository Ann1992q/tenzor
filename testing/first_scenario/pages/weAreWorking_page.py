from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait 



class WorkingButtonPage(BasePage):
    
    # Локатор заголовка "Работаем"
    weAreWorking = (By.CSS_SELECTOR, '.tensor_ru-About__block3 .tensor_ru-header-h2')
    # Локатор всех изображений в разделе "Работаем"
    photo_locator = (By.CSS_SELECTOR, '.tensor_ru-About__block3 > .s-Grid-container img')


    def __init__(self, browser):
        super().__init__(browser)

    def open(self):
        # Открываем страницу "О компании" на Tensor.ru
        self.browser.get('https://tensor.ru/about')
    
    def working(self):
        
        # Ожидаем появление заголовка "Работаем" и прокручиваем к нему
        element = WebDriverWait(self.browser, 5).until(
            EC.visibility_of_element_located(self.weAreWorking)
        )
        self.browser.execute_script("arguments[0].scrollIntoView();", element)
        
        # Проверяем, что текст соответствует ожидаемому
        assert element.text.strip() == "Работаем", \
            f"Ожидался текст 'Работаем', получено: '{element.text}'"
        
        return element
        

    def get_all_photos(self):
        #Возвращает список всех изображений в разделе 'Работаем'
        return WebDriverWait(self.browser, 10).until(
            EC.visibility_of_all_elements_located(self.photo_locator)
        )

    def check_all_photos_same_size(self):
        #Проверяет, что все изображения имеют одинаковый размер
        photos = self.get_all_photos()

        assert len(photos) > 0, "Фотографии не найдены в разделе 'Работаем'"

        first_size = photos[0].size
        first_width = first_size['width']
        first_height = first_size['height']

        print(f"Размер первого фото: {first_width}x{first_height}")

        for i, photo in enumerate(photos):
            size = photo.size
            print(f"Фото {i+1}: {size['width']}x{size['height']}")

            assert size['width'] == first_width, \
                f"Ширина фото {i+1} отличается: {size['width']} != {first_width}"
            assert size['height'] == first_height, \
                f"Высота фото {i+1} отличается: {size['height']} != {first_height}"


   