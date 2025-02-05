class Menu:
    def print(self):
        print("1. Новая игра\n2. Сменить сложность\n3. Выйти\n")

class DifficultyMenu(Menu):
    def print(self):
        print("1. Легко\n2. Нормально\n3. Сложно\n4. Безумие=)\n")