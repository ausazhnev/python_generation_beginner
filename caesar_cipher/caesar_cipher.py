# ----------------------------
# Разработчик: Andrey Sazhnev (dikey)
# Email: ausazhnev@gmail.com
# GitHub: https://github.com/ausazhnev
# Telegram: @ausazhnev
# Дата создания: 2025-05-03
# Дата последнего обновления:
# Описание: Мини-проект "шифр Цезаря" — программа, способная шифровать и дешифровать текст в соответствии
#           с алгоритмом Цезаря.
#           Программа запрашивает у пользователя следующие данные:
#           - направление: шифрование или дешифрование;
#           - язык алфавита: русский или английский;
#           - шаг сдвига (со сдвигом вправо).
# ----------------------------


def create_alphabets(id_lang: int) -> tuple[list[str], list[str]]:
    if id_lang == 1:
        low_list: list = [chr(elem) for elem in range(ord('а'), ord('я') + 1)]
        upper_list: list = [chr(elem) for elem in range(ord('А'), ord('Я') + 1)]
    else:
        low_list: list = [chr(elem) for elem in range(ord('a'), ord('z') + 1)]
        upper_list: list = [chr(elem) for elem in range(ord('A'), ord('Z') + 1)]
    # Первый вариант через тернарный оператор, читается сложно
    # low_list: list = [chr(elem) for elem in
    #                   range(ord('a') if id_lang == 2 else ord('а'), ord('z') + 1 if id_lang == 2 else ord('я') + 1)]
    # upper_list: list = [chr(elem) for elem in
    #                     range(ord('A') if id_lang == 2 else ord('А'), ord('Z') + 1 if id_lang == 2 else ord('Я') + 1)]
    return low_list, upper_list


def get_char(c: str, chars: list, step: int) -> str:
    idx: int = chars.index(c) + step
    return chars[idx] if idx < len(chars) else chars[idx % len(chars)]


def coder(text: str, step: int, low: list, upper: list) -> str:
    new_text: str = ""
    for c in text:
        if c in low:
            new_text += get_char(c, low, step)
        elif c in upper:
            new_text += get_char(c, upper, step)
        else:
            new_text += c
    return new_text


def user_choice(message: str) -> int:
    print(message)
    user_input: str = input("Введите 1 или 2... ")
    while not (user_input.isdigit() and int(user_input) in [1, 2]):
        user_input = input("Введите 1 или 2... ")
    return int(user_input)


def is_valid_step() -> int:
    step: str = input("Введите сдвиг (цифра): ")
    while not (step.isdigit() and int(step) > 1):
        step = input("Введите сдвиг (цифра): ")
    return int(step)


def main() -> None:
    lang: int = user_choice("Выберете язык:\n - 1 - Ru Русский.\n - 2 - En - Английский.")
    low, upper = create_alphabets(lang)
    work_format: int = user_choice("Выберете формат:\n - 1 - Кодирование.\n - 2 - Декодирование.")
    user_text: str = input("Введите исходную строку: ")
    step: int = is_valid_step()

    if work_format != 1: step *= -1
    print(coder(user_text, step, low, upper))


if __name__ == "__main__":
    main()
