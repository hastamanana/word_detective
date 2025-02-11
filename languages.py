import string

alphabets: dict[str, dict[str, str]] = {
    "en": {
        "vowels": "aeiouy",
        "consonants": string.ascii_lowercase,
    },
    "ru": {
        "vowels": "аеёиоуыэюя",
        "consonants": "бвгджзйклмнпрстфхцчшщъь",
    },
}

info_messages: dict[str, dict[str, str]] = {
    "en": {
        "enter_char": "Введите букву латинского алфавита",
    },
    "ru": {
        "enter_char": "Введите букву кириллицы",
    },

}

codes: dict[int, str] = {
    1: "en",
    2: "ru",
}
