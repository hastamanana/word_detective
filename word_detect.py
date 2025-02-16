from languages import alphabets, codes, info_messages


def show_game_info() -> None:
    available_alphabets: tuple[str, ...] = (
        "Латинский",
        "Кириллица",
    )

    print('Добро пожаловать в программу "Буква-Детектив!\n')
    print("Выберите алфавит:\n")
    for index, name in enumerate(available_alphabets, start=1):
        print(f"{index}. {name}")
    print()


def check_letter(char: str, lang: str) -> str:
    vowels: str = alphabets.get(lang).get("vowels").upper()
    consonants: str = alphabets.get(lang).get("consonants").upper()

    if char in vowels:
        return f"{char} - гласная буква!"
    elif char in consonants:
        return f"{char} - согласная буква!"

    return "Упс! Неизвестная буква. Попробуйте другую!"


def main() -> str:
    show_game_info()

    try:
        user_choice: int = int(input("Введите номер алфавита: "))
    except ValueError as err:
        print(f"[ОШИБКА] {err}")
    else:
        if user_choice not in codes:
            return "Упс! Выбран неверный режим. Попробуйте ещё раз..."

        lang: str = codes.get(user_choice)
        hint_msg: str = info_messages.get(lang).get("enter_char")
        char: str = input(f"{hint_msg}: ")

        return check_letter(char, lang)


if __name__ == "__main__":
    print(main())
