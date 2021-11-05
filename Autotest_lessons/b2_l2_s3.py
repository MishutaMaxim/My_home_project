from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

browser = webdriver.Chrome()
try:
    browser.get("http://suninjuly.github.io/selects1.html")

    # Считаем выражение данное на странице
    num1 = browser.find_element(By.ID, 'num1').text
    num2 = browser.find_element(By.ID, 'num2').text
    result = int(num1) + int(num2)

    # Выбираем вариант ответа
    Select(browser.find_element(By.ID, "dropdown")).select_by_value(str(result))

    # Отправляем
    browser.find_element(By.CLASS_NAME, 'btn').click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(4)
    # закрываем браузер после всех манипуляций
    browser.quit()
