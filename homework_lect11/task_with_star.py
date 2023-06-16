# Перейти на  https://sbis.ru/
# В Footer'e найти "Скачать СБИС"
# Перейти по ней
# Скачать СБИС Плагин для вашей ОС в папку с данным тестом
# Убедиться, что плагин скачался
# Вывести на печать размер скачанного файла в мегабайтах
# Для сдачи задания пришлите код и запись с экрана прохождения теста

from pathlib import Path
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep
import os

options = Options()
options.add_experimental_option("prefs", {
    "download.default_directory": os.getcwd(),
    "download.prompt_for_download": False,
    "download.directory_upgrade": True,
    "safebrowsing.enabled": True
})

url_sbis = 'https://sbis.ru/'
driver = webdriver.Chrome(options=options)
driver.maximize_window()
try:
    # Перейти на https://sbis.ru/
    driver.get(url_sbis)
    assert driver.current_url == url_sbis, 'Не верно открыт сайт'
    sleep(2)

    # В Footer'e найти "Скачать СБИС"
    sbis_download = driver.find_element(By.LINK_TEXT, "Скачать СБИС")
    assert sbis_download.is_displayed(), "В Footer'e нет опции 'Скачать СБИС'"
    assert sbis_download.text == 'Скачать СБИС', 'Текст элемента не соответствует эталону "Скачать СБИС"'
    sleep(3)

    # Перейти по ней
    sbis_download.location_once_scrolled_into_view
    sbis_download.click()
    sleep(3)

    # Скачать СБИС Плагин для вашей ОС в папку с данным тестом
    tab_plugin = driver.find_element(By.CSS_SELECTOR, '[data-id="plugin"]')
    tab_plugin.click()
    sleep(2)
    sbis_plugin = driver.find_element(By.XPATH, '//a[contains(@href, "setup-full.msi")]')
    assert sbis_plugin.is_displayed(), 'Не отображается блок для скачивания полной версии СБИС Плагина'
    link_sbis_plugin = sbis_plugin.get_attribute("href")
    driver.get(link_sbis_plugin)
    sleep(130)

    # Убедиться, что плагин скачался
    filename = Path(link_sbis_plugin).name
    plugin_path = os.path.join(os.getcwd(), filename, )
    assert os.path.exists(plugin_path), 'Плагин не скачан'

    # Вывести на печать размер скачанного файла в мегабайтах
    print(f'Размер файла установки плагина = {round(os.path.getsize(plugin_path) / 1024 ** 2, 2)} Mb')
finally:
    driver.quit()
