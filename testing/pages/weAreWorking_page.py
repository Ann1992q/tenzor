from base_page import BasePage
from selenium.webdriver.common.by import By


class WorkingPage(BasePage):
    """
    Page Object для работы с разделом "Работаем" на странице tensor.ru/about.

    Предоставляет методы для проверки наличия заголовка,
    получения всех изображений и проверки их одинакового размера.

    Attributes:
        working (tuple): Локатор заголовка "Работаем".
        photo_locator (tuple): Локатор всех изображений в разделе.
    """
    
    working = (By.CSS_SELECTOR, '.tensor_ru-About__block3 .tensor_ru-header-h2')
    photo_locator = (By.CSS_SELECTOR, '.tensor_ru-About__block3 > .s-Grid-container img')


    def weAreWorking_title(self):
        """
        Проверяет наличие заголовка 'Работаем' и его текст.

        Прокручивает к заголовку и убеждается, что он отображается корректно.
        """
        expected_text = "Работаем"
        self.scroll_to(*self.working)
        element = self.find_visible(*self.working)

        actual_text = self.get_text(element)
        assert actual_text == expected_text, \
            f"Ожидался текст '{expected_text}', получено: '{actual_text}'"

    def get_all_photos(self):
        """
        Находит все видимые фотографии в разделе 'Работаем'.

        Returns:
            list[WebElement]: Список элементов изображений.
        """
        return self.find_all_visible(*self.photo_locator)
       

    def check_all_photos_same_size(self):
        """
        Проверяет, что все изображения в разделе 'Работаем' имеют одинаковый размер.

        Raises:
            AssertionError: Если хотя бы одно фото отличается по ширине или высоте.
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


   