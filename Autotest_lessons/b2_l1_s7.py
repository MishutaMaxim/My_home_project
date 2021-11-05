from selenium import webdriver
import time
import math
from selenium.webdriver.common.by import By


def get_calc(inp_number):
    return str(math.log(abs(12 * math.sin(int(inp_number)))))


browser = webdriver.Chrome()
try:
    browser.get("http://suninjuly.github.io/get_attribute.html")

    # Считаем выражение и подставляем в поле
    number = browser.find_element(By.ID, 'treasure').get_attribute('valuex')
    result = get_calc(int(number))
    browser.find_element(By.ID, 'answer').send_keys(result)

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
