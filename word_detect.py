ENG_VOWELS: str = 'AEIOUY'
CYRILLIC_VOWELS: str = 'АЕЁИОУЫЭЮЯ'

print('Добро пожаловать в программу "Буква-Детектив!\n')

print('Выберите алфавит:\n')
print('1. Латинский')
print('2. Кириллица\n')


def is_correct_alphabet_number(n: int) -> bool:
    if n not in [1, 2]:
        print("Упс! Выбран неверный режим. Попробуйте ещё раз...")
        return False
    return True


def check_letter(
        vowels: str,
        char: str,
        first_and_last_letter: tuple[str, str]
) -> str:
    """

    :param vowels:
    :param char:
    :param first_and_last_letter: Первая и последняя буква алфавита.
    :return:
    """
    first, last = first_and_last_letter

    if char in vowels:
        return f'{char} - гласная буква!'
    elif first < char < last:
        return f"{char} - согласная буква!"

    return 'Упс! Неизвестная буква. Попробуйте другую!'


def main(num, el):
    if num == 1:
        print(check_letter(ENG_VOWELS, el, ('A', 'Z')))
    elif num == 2:
        print(check_letter(CYRILLIC_VOWELS, el, ('А', 'Я')))


if __name__ == '__main__':

    try:
        a = int(input('Введите номер алфавита: '))
    except ValueError or a not in [1, 2]:
        print("Упс! Выбран неверный режим. Попробуйте ещё раз...")
    else:
        if is_correct_alphabet_number(a):
            if a == 1:
                main(a, input('Введите букву латинского алфавита: ').upper())
            if a == 2:
                main(a, input('Введите букву кириллицы: ').upper())
