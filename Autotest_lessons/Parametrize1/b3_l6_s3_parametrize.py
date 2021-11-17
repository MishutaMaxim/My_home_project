import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
import math


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


@pytest.mark.parametrize('number', ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"])
def test_guest_should_see_login_link(browser, number):
    link = f"https://stepik.org/lesson/{number}/step/1"
    browser.get(link)
    browser.implicitly_wait(5)
    answer = math.log(int(time.time()))
    browser.find_element(By.CLASS_NAME, "ember-text-area").send_keys(answer)
    browser.find_element(By.CLASS_NAME, "submit-submission").click()
    answer_text = browser.find_element(By.CLASS_NAME, "smart-hints__hint").text
    assert answer_text == "Correct!", f"Ошибка, мы получили текст: {answer_text}"
