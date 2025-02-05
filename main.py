from enums import MenuElements
from manager import GameManager
from menu import Menu, DifficultyMenu

class Program:
    
    def __init__(self):
        self._menu_view = Menu()
        self._difficulty_view = DifficultyMenu()

    def run(self):
        manager = GameManager()
        while True:
            self._menu_view.print()
            match input():
                case MenuElements.START.value:
                    manager.run_game()
                case MenuElements.DIFFICULTY.value:
                    self._difficulty_view.print()
                    manager.set_difficulty()
                case MenuElements.QUIT.value:
                    break
                case _:
                    print("Неверный ввод пункта меню\n")
                    continue

if __name__ == "__main__":
    program = Program()
    program.run()