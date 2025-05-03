# ----------------------------
# Разработчик: Andrey Sazhnev (dikey)
# Email: ausazhnev@gmail.com
# GitHub: https://github.com/ausazhnev
# Telegram: @ausazhnev
# Дата создания: 2025-05-02
# Дата последнего обновления:
# Описание: Мини-проект "Генератор паролей" — программа генерирует заданное количество
#           паролей и включает в себя умную настройку на длину пароля, а также на то,
#           какие символы требуется в него включить, а какие исключить.
# ----------------------------

from random import choice


def is_valid_num(user_data: str) -> bool:
    return user_data.isdigit() and int(user_data) > 1


def add_chars(message: str, chars: str) -> str:
    print(message)
    if input("Введите 'д'/'да' что бы использовать, иначе любое другое: ").lower() in ["д", "да"]:
        return chars
    else:
        return ""


def customization(digits: str, lowercase_letters: str, uppercase_letters: str,
                  punctuation: str, chars: str, symbols: str) -> tuple[int, int, str]:
    user_input_pas_count: str = input(f"Какое количество паролей сгенерировать? ")
    while not is_valid_num(user_input_pas_count):
        print("Вы ввели не корректное значение.")
        user_input_pas_count = input(f"Какое количество паролей сгенерировать? ")
    pas_count: int = int(user_input_pas_count)

    user_input_pas_len: str = input(f"Укажите длину пароля: ")
    while not is_valid_num(user_input_pas_len):
        print("Вы ввели не корректное значение.")
        user_input_pas_len = input(f"Укажите длину пароля: ")
    pas_len: int = int(user_input_pas_len)

    chars += add_chars(f"Использовать в пароле цифры {digits} ?", digits)
    chars += add_chars(f"Использовать в пароле маленькие буквы {lowercase_letters} ?", lowercase_letters)
    chars += add_chars(f"Использовать в пароле большие буквы {uppercase_letters} ?", uppercase_letters)
    chars += add_chars(f"Использовать в пароле символы {punctuation} ?", punctuation)

    print(f"Использовать в пароле символы {symbols} ?")
    if not input("Введите 'д'/'да' что бы использовать, иначе любое другое: ").lower() in ["д", "да"]:
        for c in symbols:
            chars = chars.replace(c, "")

    return pas_count, pas_len, chars


def pas_generator(pas_len: int, chars: str) -> str:
    return "".join(choice(chars) for _ in range(pas_len))


def main(digits: str, lowercase_letters: str, uppercase_letters: str, punctuation: str,
         symbols: str) -> None:
    chars: str = ""
    pas_count, pas_len, chars = customization(digits, lowercase_letters,
                                              uppercase_letters, punctuation, chars, symbols)
    for _ in range(pas_count):
        print(pas_generator(pas_len, chars))


if __name__ == "__main__":
    DIGITS: str = "0123456789"
    LOWERCASE_LETTERS: str = "abcdefghijklmnopqrstuvwxyz"
    UPPERCASE_LETTERS: str = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    PUNCTUATION: str = "!#$%&*+-=?@^_"
    SYMBOLS: str = "il1Lo0O"
    main(DIGITS, LOWERCASE_LETTERS, UPPERCASE_LETTERS, PUNCTUATION, SYMBOLS)
