import sys
import config

from enums import Difficulties

def _load_words(path: str):
    try:
        with open(path, "r", encoding="utf-8") as words_file:
            lines = words_file.readlines()
            words = []
            for line in lines:
                words.extend(line.strip().replace(",", "").split())
            return words
    except FileNotFoundError:
        print(f"Файл {path} не найден.")

class GameManager:
    def __init__(self):
        self._word_list = _load_words(config.NORMAL_PATH)

    def run_game(self):
        pass

    def set_difficulty(self, user_input: str):
        match user_input:
            case Difficulties.EASY.value:
                self._word_list = _load_words(config.EASY_PATH)
            case Difficulties.NORMAL.value:
                self._word_list = _load_words(config.NORMAL_PATH)
            case Difficulties.HARD.value:
                self._word_list = _load_words(config.HARD_PATH)
            case Difficulties.CRAZY.value:
                self._word_list = _load_words(config.CRAZY_PATH)
            case _:
                raise IndexError
    
    def quit(self):
        sys.exit(0)