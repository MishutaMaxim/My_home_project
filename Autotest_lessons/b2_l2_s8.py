from selenium import webdriver
import time
import os

from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
try:
    browser.get('http://suninjuly.github.io/file_input.html')

    # Заполняем поля
    browser.find_element(By.NAME, 'firstname').send_keys('Владимир')
    browser.find_element(By.NAME, 'lastname').send_keys('Путин')
    browser.find_element(By.NAME, 'email').send_keys('vova@molodec.ru')

    # Загружаем файлик
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'empty_file.txt')
    browser.find_element(By.ID, 'file').send_keys(file_path)

    # Отправляем заполненную форму
    button = browser.find_element(By.CLASS_NAME, 'btn')
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(4)
    # закрываем браузер после всех манипуляций
    browser.quit()
