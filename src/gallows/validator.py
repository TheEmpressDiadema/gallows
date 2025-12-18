from abc import ABC


class Validator(ABC):

    _alphabet: str

    def validate(self, user_input: str):
        if len(user_input) != 1:
            raise ValueError("Длина ввода не соответствует требуемой: 1")
        if user_input not in self._alphabet:
            raise ValueError("Введена буква другого алфавита")


class MenuInputValidator(Validator):

    _alphabet: str = "12"


class RoundInputValidator(Validator):

    _alphabet: str = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
