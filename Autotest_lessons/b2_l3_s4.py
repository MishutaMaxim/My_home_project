from selenium import webdriver
import time
import math

from selenium.webdriver.common.by import By


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/alert_accept.html')

    # Нажимаем кнопку
    browser.find_element(By.CLASS_NAME, 'btn').click()

    # Принять confirm
    browser.switch_to.alert.accept()

    # На новой странице решить капчу для роботов, чтобы получить число с ответом
    magic_number = browser.find_element(By.ID, 'input_value').text
    answer = calc(magic_number)
    browser.find_element(By.ID, 'answer').send_keys(answer)
    browser.find_element(By.CLASS_NAME, 'btn').click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(4)
    # закрываем браузер после всех манипуляций
    browser.quit()
