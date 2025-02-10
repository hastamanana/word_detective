import string

LATIN_GLAS = {i for i in 'AEIOUY'}
CYRILIC_GLAS = {i for i in 'АЕЁИОУЫЭЮЯ'}
LATIN_UPPER_LETTERS = {i for i in string.ascii_uppercase}
CYRILLIC_UPPER_LETTERS = {i for i in 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'.upper()}


def alphabet(n: int) -> bool:
    if n not in [1,2]:
        print("Упс! Выбран неверный режим. Попробуйте ещё раз...")
        return False
    return True
    
def letter(num: int, el: str) -> bool:
    if num == 1:
        if el not in string.ascii_uppercase:
            print('Упс! Неизвестная буква. Попробуйте другую!')
            return False
        if el in LATIN_GLAS:
            print(f"{el} - гласная буква!")
        if el in LATIN_UPPER_LETTERS - (LATIN_UPPER_LETTERS & LATIN_GLAS):
            print(f"{el} - согласная буква!")
        return True
    if num == 2:
        if el not in CYRILLIC_UPPER_LETTERS:
            print(f"Упс! Неизвестная буква. Попробуйте другую!")
            return False
        if el in CYRILIC_GLAS:
            print(f"{el} - гласная буква!")
        if el in CYRILLIC_UPPER_LETTERS - (CYRILLIC_UPPER_LETTERS & CYRILIC_GLAS):
            print(f"{el} - согласная буква!")
        return True




def main(num, el):
    if not letter(num, el):
        return None
    
if __name__ == '__main__':
    try:
        a = int(input())
        if alphabet(a):
            main(a, input())
    except ValueError or a not in [1,2]:
        print("Упс! Выбран неверный режим. Попробуйте ещё раззззззззз...")
    
    