import string

LATIN_GLAS = set('AEIOUY')
CYRILIC_GLAS = set('АЕЁИОУЫЭЮЯ')
LATIN_UPPER_LETTERS = set(string.ascii_uppercase)
CYRILLIC_UPPER_LETTERS = set('абвгдеёжзийклмнопрстуфхцчшщъыьэюя'.upper())


print('Добро пожаловать в программу "Буква-Детектив!\n')

print('Выберите алфавит:\n')
print('1. Латинский')
print('2. Кириллица\n')

def is_correct_alphabet_number(n: int) -> bool:
    if n not in [1,2]:
        print("Упс! Выбран неверный режим. Попробуйте ещё раз...")
        return False
    return True
    

def alphabet_n_letter_of_alphabet(num: int, el: str) -> bool:
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
    if not alphabet_n_letter_of_alphabet(num, el):
        return None
    

if __name__ == '__main__':
    
    try:
        a = int(input('Введите номер алфавита: '))
    except ValueError or a not in [1,2]:
        print("Упс! Выбран неверный режим. Попробуйте ещё раз...")
    else:
        if is_correct_alphabet_number(a):
            if a == 1:
                main(a, input('Введите букву латинского алфавита: ').upper())
            if a == 2:
                main(a, input('Введите букву кириллицы: ').upper())
    
    