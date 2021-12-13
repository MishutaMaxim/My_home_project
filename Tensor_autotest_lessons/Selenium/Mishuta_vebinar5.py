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
        support_locator = (By.CSS_SELECTOR, "a[href='/support']")
        downloads_locator = (By.CSS_SELECTOR, "a[href='/download']")
        downloads_link = (By.CSS_SELECTOR, ".sbis_ru-DownloadNew-loadLink a")
        download_links = []
        # Открываем линк, переходим в поддержку, переходим в скачать
        driver.implicitly_wait(5)
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



# 1. Сосчитать сколько в каталоге установки python:
# папок
# файлов с расширением ".py"
# файлов с расширением ".exe"
# всего файлов
# 2. Записать результаты в файл
def file_counter():
    import os
    import sys
    start_path = os.getcwd()
    path = os.path.dirname(sys.executable)
    os.chdir(path)
    print(os.getcwd())
    dir_count, py_count, exe_count, file_count = 0, 0, 0, 0
    for root, dirs, files in os.walk(path):
        for _dir in dirs:
            dir_count += 1
        for _file in files:
            file_count += 1
            if _file[-3:] == '.py':
                py_count += 1
            if _file[-4:] == '.exe':
                exe_count += 1
    os.chdir(start_path)
    with open('vebinar5_file_counter.txt', 'w', encoding="utf-8") as file:
        file.write('В каталоге - ' + path + '\n')
        file.write('Папок - ' + str(dir_count) + '\n')
        file.write('Файлов с расширением ".py" - ' + str(py_count) + '\n')
        file.write('Файлов с расширением ".exe" - ' + str(exe_count) + '\n')
        file.write('Всего файлов - ' + str(file_count) + '\n')


file_counter()
