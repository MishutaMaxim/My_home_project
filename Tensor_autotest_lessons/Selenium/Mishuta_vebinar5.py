# Зайти на https://sbis.ru/
# Перейти по ссылке поддержка
# Кликнуть по кнопке "Скачать"
# Получить все ссылки на обновления и записать их в файл
def chek_download_links():
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    driver = webdriver.Chrome()
    try:
        # Ссылка и локаторы
        link = 'https://sbis.ru/'
        support_locator = (By.XPATH, "//a[starts-with(@href, '/support')]")
        downloads_locator = (By.XPATH, "//a[starts-with(@href, '/download')]")
        downloads_link = (By.CSS_SELECTOR, ".sbis_ru-DownloadNew-loadLink a")
        download_links = []
        # Открываем линк, переходим в поддержку, переходим в скачать
        driver.get(link)
        driver.find_element(*support_locator).click()
        driver.find_element(*downloads_locator).click()
        # Перебираем все элементы с локатором ссылки скачивания
        for element in driver.find_elements(*downloads_link):
            # Проверяем что элемент виден на странице, в противном случае мы находим все 20 ссылок с других вкладок
            if element.is_displayed():
                # Записываем ссылку элемента в список
                download_links.append(element.get_attribute('href'))
        # Переписываем все ссылки из списка в файл
        with open('vebinar5_download_links.txt', 'w') as file:
            for link in download_links:
                file.write(link + '\n')
    # Закрываем браузер
    finally:
        driver.quit()


# chek_download_links()

# 1. Сосчитать сколько в каталоге установки python:
# папок
# файлов с расширением ".py"
# файлов с расширением ".exe"
# всего файлов
# 2. Записать результаты в файл
def file_counter():
    import os
    import sys
    home = os.path.dirname(sys.executable)
    os.chdir(home)
    print(os.getcwd())


file_counter()
