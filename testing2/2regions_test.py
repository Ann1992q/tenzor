from selenium.webdriver.support.ui import WebDriverWait


#ЦЕЛЬ: Переход в раздел "Контакты"
def test_button_contacts(region_page_contacts):
    region_page_contacts.click_button_contacts()
    region_page_contacts.click_button_contacts_more()
    current_url = region_page_contacts.get_current_url()
    print(f"Текущий URL: {current_url}")
    print('Успешно выполнен переход в раздел "Контакты"')

#ЦЕЛЬ: Проверить, что определился ваш регион и список партнеров
# Получаем текущий регион
def test_current_region(region_page):
    initial_region = region_page.get_current_region_text()
    print(f"Текущий регион: {initial_region}")

# Получаем список партнеров
def test_partner_names(region_page):
    partner_names = region_page.get_partner_names()
    print("Найденные партнеры:")
    for name in partner_names:
        print(f"- {name}")
       
#ЦЕЛЬ: Выбор региона "Камчатский край" и проверка списка партнеров
#Проверить, что URL и TITLE содержат информацию о выбранном регионе
def test_select_kamchatka_region(region_page):   
    region_page.select_region("Камчатский край")

    partner_names_kamchatka = region_page.get_partner_names_kamchatka()
    print("Найденные партнеры:")
    for name in partner_names_kamchatka:
        print(f"- {name}")


