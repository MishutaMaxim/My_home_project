from selenium import webdriver
import time
import math

from selenium.webdriver.common.by import By


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


browser = webdriver.Chrome()
try:
    browser.get('http://suninjuly.github.io/redirect_accept.html')

    # Нажать на кнопку
    browser.find_element(By.CLASS_NAME, 'btn').click()

    # Переключиться на новую вкладку
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    # Пройти капчу для робота и получить число-ответ
    magic_number = browser.find_element(By.ID, 'input_value').text
    answer = calc(magic_number)
    browser.find_element(By.ID, 'answer').send_keys(answer)
    browser.find_element(By.CLASS_NAME, 'btn').click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(4)
    # закрываем браузер после всех манипуляций
    browser.quit()
