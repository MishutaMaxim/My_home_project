from selenium import webdriver
import time
import math
from selenium.webdriver.common.by import By


def calc(number):
    return str(math.log(abs(12 * math.sin(int(number)))))


browser = webdriver.Chrome()
try:
    browser.get("http://suninjuly.github.io/math.html")

    # Считаем выражение и подставляем в поле
    x_element = browser.find_element(By.ID, 'input_value')
    x = x_element.text
    y = calc(x)
    browser.find_element(By.ID, 'answer').send_keys(y)

    # Отмечаем чекбокс
    browser.find_element(By.ID, 'robotCheckbox').click()

    # Отмечаем радио
    browser.find_element(By.ID, 'robotsRule').click()

    # Отправляем заполненную форму
    button = browser.find_element(By.CLASS_NAME, 'btn')
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(4)
    # закрываем браузер после всех манипуляций
    browser.quit()
