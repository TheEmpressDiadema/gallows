import sys

from gallows.config import WORDS_PATH
from gallows.menu import Menu
from gallows.round import Round
from gallows.validator import MenuInputValidator

class Game:

    def __init__(self):
        self._menu = Menu()
        self._menu_input_validator = MenuInputValidator()
        self._words = self._load_words()

    def _load_words(self) -> list[str]:
        with open(WORDS_PATH, encoding="utf-8") as words_file:
            return [word[:-1] for word in words_file.readlines()]
    
    def _process_input(self, user_input: str):
        if user_input == "1":
            round = Round(self._words)
            round.run()
        else:
            sys.exit(0)
        

    def __call__(self):
        while True:
            self._menu.print_view()
            try:
                user_input = input().strip().lower()
                self._menu_input_validator.validate(user_input)
                self._process_input(user_input)
            except ValueError as error:
                print(error)