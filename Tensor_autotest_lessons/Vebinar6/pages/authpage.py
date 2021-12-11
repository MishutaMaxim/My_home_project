from atf.ui import *


class AuthPage(Region):
    """"Страница авторизации"""

    AUTH_LOGIN = Element(By.CSS_SELECTOR, '[name = "login"]', 'Поле логин')
    AUTH_PASSWORD = Element(By.CSS_SELECTOR, '[name = "password"]', 'Поле пароль')
    AUTH_ENTER_BUTTON = Element(By.CSS_SELECTOR, '.auth-Form__submit', 'Кнопка войти')

    def auth(self, user_login: str, user_password: str):
        """
        Авторизация в аккаунте
        :param user_login: Логин пользователя
        :param user_password: Пароль пользователя
        """
        self.AUTH_LOGIN.type_in(user_login)
        self.AUTH_PASSWORD.type_in(user_password)
        self.AUTH_ENTER_BUTTON.click()
