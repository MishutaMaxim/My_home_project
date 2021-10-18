from selenium import webdriver
import time
import os

try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/file_input.html')

    # Заполняем поля
    browser.find_element_by_name('firstname').send_keys('Владимир')
    browser.find_element_by_name('lastname').send_keys('Путин')
    browser.find_element_by_name('email').send_keys('vova@molodec.ru')


    # Загружаем файлик
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'empty_file.txt')
    browser.find_element_by_id('file').send_keys(file_path)

    # Отправляем заполненную форму
    button = browser.find_element_by_class_name('btn')
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(4)
    # закрываем браузер после всех манипуляций
    browser.quit()