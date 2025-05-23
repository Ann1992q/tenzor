from pages.weAreWorking_page import WorkingButtonPage


# ЦЕЛЬ: Проверить наличие раздела "Работаем"
# и убедиться, что все фотографии в этом разделе имеют одинаковый размер
def test_working(browser):
    weAreWorking_page = WorkingButtonPage(browser)
    weAreWorking_page.open()

    # Проверяем, отображается ли заголовок "Работаем"
    assert weAreWorking_page.working()
    print('Раздел "Работаем" присутствует на странице')

    # Проверяем, что все фото в этом разделе одного размера
    weAreWorking_page.check_all_photos_same_size()
    print('Все фотографии в разделе "Работаем" имеют одинаковый размер')

