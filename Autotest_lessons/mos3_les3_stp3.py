import unittest
from selenium import webdriver
import time

class Test_registration(unittest.TestCase):
    def test_registration1(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        browser.find_element_by_css_selector('[placeholder="Input your first name"]').send_keys('Vladimir')
        browser.find_element_by_css_selector('[placeholder="Input your last name"]').send_keys('Putin')
        browser.find_element_by_css_selector('[placeholder="Input your email"]').send_keys('vova@molodec.ru')
        browser.find_element_by_css_selector('[placeholder="Input your phone:"]').send_keys('111')
        browser.find_element_by_css_selector('[placeholder="Input your address:"]').send_keys('Kremlin')

        # Отправляем заполненную форму
        browser.find_element_by_css_selector("button.btn").click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        # записываем в переменную welcome_text текст
        welcome_text = browser.find_element_by_tag_name("h1").text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!", "Registration error", )

        # закрываем браузер после всех манипуляций
        browser.quit()

    def test_registration2(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        browser.find_element_by_css_selector('[placeholder="Input your first name"]').send_keys('Vladimir')
        browser.find_element_by_css_selector('[placeholder="Input your last name"]').send_keys('Putin')
        browser.find_element_by_css_selector('[placeholder="Input your email"]').send_keys('vova@molodec.ru')
        browser.find_element_by_css_selector('[placeholder="Input your phone:"]').send_keys('111')
        browser.find_element_by_css_selector('[placeholder="Input your address:"]').send_keys('Kremlin')

        # Отправляем заполненную форму
        browser.find_element_by_css_selector("button.btn").click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        # записываем в переменную welcome_text текст
        welcome_text = browser.find_element_by_tag_name("h1").text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!", "Registration error", )

        # закрываем браузер после всех манипуляций
        browser.quit()


if __name__ == "__main__":
    unittest.main()
