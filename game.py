import random

from word import Word
from gallows import Gallows
from validators import IngameValidator


class Game:

    def __init__(self, words: list[str]):
        self._word = Word(random.choice(words))
        self._gallows = Gallows()
        self._used_letters = []
        self._validator = IngameValidator()
        self._stage = 0
        self._max_stages = 5

    def run(self):
        while True:
            self._run_round()
            if self._word.is_fully_revealed():
                print("Вы выиграли")
                print(f"Загаданное слово: {self._word.word}")
                break
            if self._stage == self._max_stages:
                self._gallows.print_stage(self._stage)
                print("Вы проиграли")
                print(f"Загаданное слово: {self._word.word}")
                break

    def _print_status(self):
        self._gallows.print_stage(self._stage)
        print(f"Состояние отгадвания =) {self._word.state}")
        print(f"Использованные буквы: {','.join(self._used_letters)}")
        print(f"Осталось попыток: {self._stage}")

    def _validate_input(self, user_input: str) -> bool:
        is_valid = self._validator.validate_alpha(user_input)
        is_valid &= self._validator.validate_len(user_input)
        is_valid &= self._validator.validate_used(self._used_letters, user_input)
        return is_valid

    def _process_input(self) -> str:
        user_input = input("Введите букву: ").lower()
        while not self._validate_input(user_input):
            user_input = input("Введите букву: ")
        return user_input

    def _run_round(self):
        self._print_status()
        user_input = self._process_input()
        self._used_letters.append(user_input)
        if user_input in self._word.word:
            self._word.reveal(user_input)
        else:
            self._stage += 1