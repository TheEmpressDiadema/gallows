
class IngameValidator:
    def validate_used(self, used_letters: list[str], user_input: str):
        if user_input in used_letters:
            print("Вы уже вводили эту букву\n")
            return False
        return True
    
    def validate_alpha(self, user_input: str):
        alphabet = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
        if not user_input in alphabet:
            print("Алфавит эксепшон\n")
            return False
        return True
    
    def validate_len(self, user_input: str):
        if len(user_input) > 1:
            print("Вы ввели более одной буквы\n")
            return False
        if len(user_input) < 1:
            print("Вы ввели меньше одной буквы")
            return False
        return True