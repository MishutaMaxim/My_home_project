from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/selects1.html")

    # Считаем выражение данное на странице
    num1 = browser.find_element_by_id('num1').text
    num2 = browser.find_element_by_id('num2').text
    result = int(num1) + int(num2)

    # Выбираем вариант ответа
    Select(browser.find_element_by_id("dropdown")).select_by_value(str(result))

    # Отправляем
    browser.find_element_by_class_name('btn').click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(4)
    # закрываем браузер после всех манипуляций
    browser.quit()