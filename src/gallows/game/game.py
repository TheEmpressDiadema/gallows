from gallows.config.config import WORDS_PATH
from gallows.presentation.menu import Menu
from gallows.game.round import Round
from gallows.management.validator import MenuInputValidator


class Game:

    def __init__(self):
        self._menu = Menu()
        self._menu_input_validator = MenuInputValidator()
        self._words = self._load_words()

    def _load_words(self) -> list[str]:
        with open(WORDS_PATH, encoding="utf-8") as words_file:
            return [word[:-1] for word in words_file.readlines()]

    def __call__(self):
        while True:
            self._menu.print_view()
            try:
                user_input = input().strip().lower()
                self._menu_input_validator.validate(user_input)
                if user_input == "1":
                    round = Round(self._words)
                    round.run()
                else:
                    break
            except ValueError as error:
                print(error)
