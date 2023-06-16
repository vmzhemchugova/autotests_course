# Перейти на https://sbis.ru/
# Перейти в раздел "Контакты"
# Найти баннер Тензор, кликнуть по нему
# Перейти на https://tensor.ru/
# Проверить, что есть блок новости "Сила в людях"
# Перейдите в этом блоке в "Подробнее" и убедитесь, что открывается https://tensor.ru/about
# Для сдачи задания пришлите код и запись с экрана прохождения теста


from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

url_sbis = 'https://sbis.ru/'
url_tensor = 'https://tensor.ru/'
title_sbis = "СБИС — экосистема для бизнеса: учет, управление и коммуникации"
driver = webdriver.Chrome()
driver.maximize_window()
try:
    # Перейти на https://sbis.ru/
    driver.get(url_sbis)
    assert driver.current_url == url_sbis, 'Не верно открыт сайт'
    assert driver.title == title_sbis, 'Неверный заголовок'
    sleep(2)

    # Перейти в раздел "Контакты"
    contacts = driver.find_element(By.CSS_SELECTOR, '[href="/contacts"].sbisru-Header__menu-link')
    assert contacts.text == 'Контакты', 'Неверный текст элемента'
    assert contacts.is_displayed(), 'Элемент не отображается'
    contacts.click()
    sleep(3)

    # Найти баннер Тензор, кликнуть по нему
    banner_tensor = driver.find_element(By.CSS_SELECTOR, '#contacts_clients [href="https://tensor.ru/"]')
    assert banner_tensor.is_displayed(), 'Баннер Тензора не отображается'
    banner_tensor.click()
    sleep(5)

    # Перейти на https://tensor.ru/
    driver.switch_to.window(driver.window_handles[1])
    assert driver.current_url == url_tensor, 'Неверный адрес сайта Тензора'

    # Проверить, что есть блок новости "Сила в людях"
    power_people = driver.find_element(By.CSS_SELECTOR, '.tensor_ru-Index__block4-content')
    assert power_people.is_displayed()

    # Перейдите в этом блоке в "Подробнее" и убедитесь, что открывается https://tensor.ru/about
    details = driver.find_element(By.CSS_SELECTOR, '.tensor_ru-Index__block4-content .tensor_ru-Index__link')
    details.location_once_scrolled_into_view
    sleep(3)
    assert details.is_displayed(), 'Элемент "Подробнее" в блоке "Сила в людях" не отображается'
    assert details.text == 'Подробнее', 'Текст на элементе не соответствует эталону Подробнее'
    details.click()
    sleep(3)
    assert driver.current_url == url_tensor + 'about', 'Ссылка не соответствует url https://tensor.ru/about'

finally:
    driver.quit()
