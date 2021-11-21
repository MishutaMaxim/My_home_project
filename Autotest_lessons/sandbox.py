from selenium import webdriver

# инициализируем драйвер браузера. После этой команды вы должны увидеть новое открытое окно браузера
driver = webdriver.Chrome()

driver.get("https://stepik.org/lesson/25969/step/8")
print(driver.current_url)
