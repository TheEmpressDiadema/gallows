import sys
import config
import random

from word import Word
from gallows import Gallows

class Game:

    def _set_word(self, words: list[str]):
        self._word = Word(random.choice(words))

    def _start_round(self, used_letters: list[str], stage):
        print(f"Ход номер: {stage}")

    def run(self):
        used_letters = []
        while True:
            pass