from gallows.config.config import MAX_MISTAKE_COUNT
from gallows.management.manager import RoundManager
from gallows.management.validator import RoundInputValidator
from gallows.presentation.gallows import Gallows


class Round:

    def __init__(self, word_list: list[str]):
        self._word_list = word_list
        self._round_manager = RoundManager()
        self._input_validator = RoundInputValidator()
        self._load_params()

    def _load_params(self):
        self._word = self._round_manager.choose_word(self._word_list)
        self._mask = self._round_manager.create_mask(self._word)

    def _proceed_round(self, user_input: str, mistake_count: int):
        is_revealed = self._round_manager.reveal_letter(
            self._mask, self._word, user_input
        )
        match self._round_manager.get_status(self._mask, mistake_count):
            case 1:
                print(f"Вы выиграли, загаданное слово: {self._word}")
            case 2:
                print(f"Вы проиграли, загаданное слово: {self._word}")
            case _:
                if is_revealed:
                    self.run(mistake_count)
                else:
                    print("Нет такой буквы")
                    print(Gallows.get_stage(mistake_count))
                    print(f"Ошибок осталось:{MAX_MISTAKE_COUNT - mistake_count - 1}")
                    self.run(mistake_count + 1)

    def run(self, mistake_count: int = 0):
        try:
            print("".join(self._mask))
            user_input = input("Введите букву:").strip().lower()
            self._input_validator.validate(user_input)
            self._proceed_round(user_input, mistake_count)
        except ValueError as error:
            print(error)
            self.run(mistake_count)
