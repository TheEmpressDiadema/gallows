from enum import Enum

class MenuElements(Enum):
    START = "1"
    DIFFICULTY = "2"
    QUIT = "3"

class Difficulties(Enum):
    EASY = "1"
    NORMAL = "2"
    HARD = "3"
    CRAZY = "4"