class Word:
    def __init__(self, word):
        self._hidden_word = word
        self._len = len(self._hidden_word)
        self._state = ['X']*self._len

    @property
    def word(self):
        return self._hidden_word

    @property
    def state(self):
        return "".join(self._state)
    
    def reveal(self, user_input: str):
        for index in range(self._len):
            if self.word[index] == user_input:
                self._state[index] = self.word[index]