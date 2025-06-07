from base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait 



class WorkingPage(BasePage):
    """
    Page Object для работы с разделом "Работаем" на странице https://tensor.ru/about.

    Предоставляет методы для проверки наличия заголовка,
    получения всех изображений и проверки их одинакового размера.

    Attributes:
        working (tuple): Локатор заголовка "Работаем".
        photo_locator (tuple): Локатор всех изображений в разделе.
    """
    
    working = (By.CSS_SELECTOR, '.tensor_ru-About__block3 .tensor_ru-header-h2')
    
    photo_locator = (By.CSS_SELECTOR, '.tensor_ru-About__block3 > .s-Grid-container img')


    def __init__(self, browser):
        """
        Инициализирует экземпляр WorkingPage.

        :param browser: WebDriver-сессия, передаваемая из pytest-фикстуры
        :type browser: selenium.webdriver.remote.webdriver.WebDriver
        """
        super().__init__(browser)

    def open(self, url):
        """
        Открывает указанную веб-страницу в браузере.

        :param url: URL адрес целевой страницы
        :type url: str
        """
        self.browser.get(url)
    
    def weAreWorking_title(self):
        """
        Находит заголовок 'Работаем', прокручивает к нему и проверяет текст.
        """
        element = WebDriverWait(self.browser, 20).until(
            EC.visibility_of_element_located(self.working),
            message="Заголовок 'Работаем' не найден"
        )

        # Прокрутка к элементу
        element.location_once_scrolled_into_view

        # Проверка текста
        actual_text = element.text.strip()
        expected_text = "Работаем"
        assert actual_text == expected_text, \
            f"Ожидался текст '{expected_text}', получено: '{actual_text}'"

        return element

    def get_all_photos(self):
        """
        Ожидает появления всех изображений в разделе 'Работаем' и возвращает их
        список.

        :return: Список элементов изображений в разделе "Работаем"
        :rtype: List[selenium.webdriver.remote.webelement.WebElement]
        :raises selenium.common.exceptions.TimeoutException:
            Если ни одно изображение не стало видимым за заданное время
        """
        return WebDriverWait(self.browser, 10).until(
            EC.visibility_of_all_elements_located(self.photo_locator)
        )

    def check_all_photos_same_size(self):
        """
        Проверяет, что все изображения в разделе 'Работаем' имеют одинаковый размер.

        :raises AssertionError:
            Если хотя бы одно изображение отличается по ширине или высоте
        :raises selenium.common.exceptions.TimeoutException:
            Если изображения не загрузились за заданное время
        """
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


   