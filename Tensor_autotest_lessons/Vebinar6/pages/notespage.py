from atf.ui import *


class NotesPage(Region):
    NOTE_NEW_BUTTON = Element(By.CSS_SELECTOR, '[sbisname="addNote"]', 'Кнопка +Заметка')
    NOTE_INPUT_AREA = Element(By.CSS_SELECTOR, '.mce-content-body', 'Поле ввода заметки')
    NOTE_LIST_REGISTRY = CustomList(By.CSS_SELECTOR, '.ws-note__content', 'Заметка в реестре')
    NOTE_DELETE_BUTTON = Element(By.CSS_SELECTOR, '.icon-Erase', 'Кнопка удаления заметки')
    NOTE_DELETE_SUBMINT_BUTTON = Element(By.CSS_SELECTOR, '[sbisname="positiveButton"]', 'Кнопка подтверждения')
    NOTE_SAVE_BUTTON = Element(By.CSS_SELECTOR, '[sbisname="okButton"]', 'Кнопка сохранения заметки')

    def new_note(self, input_texts: str):
        """
        Создание новой заметки
        :param input_texts: Текс в заметке
        """
        self.NOTE_NEW_BUTTON.click()
        self.NOTE_INPUT_AREA.type_in(input_texts)
        self.NOTE_SAVE_BUTTON.click()

    def find_note(self, find_texts: str):
        """
        Проверка отображения заметки в реестре с указанным текстом
        :param find_texts: Текст в заметке
        """
        self.NOTE_LIST_REGISTRY.item(with_text=find_texts).should_be(Displayed, msg='В реестре нет заметки с таким текстом')

    def delete_note(self, texts_in_note: str):
        """
        Удаление заметки с указанным текстом
        :param texts_in_note: Текст в заметке
        """
        self.NOTE_LIST_REGISTRY.item(with_text=texts_in_note).should_be(Displayed, msg='Заметки нет в реестре')
        self.NOTE_LIST_REGISTRY.item(with_text=texts_in_note).click()
        self.NOTE_DELETE_BUTTON.click()
        self.NOTE_DELETE_SUBMINT_BUTTON.click()
        self.NOTE_LIST_REGISTRY.item(with_text=texts_in_note).should_not_be(Displayed, msg='Заметка осталась в реестре после удаления')
