"""
Авторизоваться на сайте fix-online.sbis.ru (Демо_тензор/Демо123)
Перейти в раздел Заметок (Документы – Заметки)
Создать заметку с вашим текстом
Убедиться, что она теперь отображается
Удалить вашу заметку
"""

from atf import run_tests
from atf.ui import *
from ..pages.notespage import NotesPage
from ..pages.authpage import AuthPage


class Test_Note(TestCaseUI):

    @classmethod
    def setup_class(cls):
        cls.browser.open('https://fix-online.sbis.ru/page/notes')
        AuthPage(cls.driver).auth('демо_тензор', 'Демо123')

    def setup(self):
        NotesPage(self.driver).NOTE_NEW_BUTTON.should_be(Displayed, wait_time=5)

    def test_01_notes(self):
        note_test_message = 'Это новая заметка'
        NotesPage(self.driver).new_note(note_test_message)
        NotesPage(self.driver).find_note(note_test_message)
        NotesPage(self.driver).delete_note(note_test_message)

    def teardown(self):
        self.browser.close_windows_and_alert()


if __name__ == '__main__':
    run_tests()
