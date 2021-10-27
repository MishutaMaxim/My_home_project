from selenium import webdriver
import time
import math

from selenium.webdriver.common.by import By


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/execute_script.html')

    # Считаем выражение и подставляем в поле
    x = browser.find_element(By.ID, 'input_value').text
    y = calc(int(x))
    browser.find_element(By.ID, 'answer').send_keys(y)

    # Отмечаем чекбокс
    Checkbox = browser.find_element(By.ID, 'robotCheckbox')
    browser.execute_script("return arguments[0].scrollIntoView(true);", Checkbox)
    Checkbox.click()

    # Отмечаем радио
    radio = browser.find_element(By.ID, 'robotsRule')
    browser.execute_script("return arguments[0].scrollIntoView(true);", radio)
    radio.click()

    # Отправляем заполненную форму
    button = browser.find_element(By.CLASS_NAME, 'btn')
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(4)
    # закрываем браузер после всех манипуляций
    browser.quit()
