from random import choice as choose_word

from gallows.config import MASK_FILLER, MAX_MISTAKE_COUNT

class RoundManager:

    def choose_word(self, word_list: list[str]) -> str:
        return choose_word(word_list)
    
    def create_mask(self, word: str) -> list[str]:
        return ["_"]*len(word)

    def reveal_letter(self, mask: list[str], word: str, letter: str) -> bool:
        is_revealed = False
        for index in range(len(word)):
            if word[index] == letter:
                mask[index] = letter
                is_revealed = True
        return is_revealed
    
    def get_status(self, mask: list[str], mistake_count: int) -> int:
        if MASK_FILLER not in mask:
            return 1
        if mistake_count == MAX_MISTAKE_COUNT - 1:
            return 2
        return 3