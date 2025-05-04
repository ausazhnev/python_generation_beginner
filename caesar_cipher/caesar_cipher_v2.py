# ----------------------------
# Разработчик: Andrey Sazhnev (dikey)
# Email: ausazhnev@gmail.com
# GitHub: https://github.com/ausazhnev
# Telegram: @ausazhnev
# Дата создания: 2025-05-04
# Дата последнего обновления:
# Описание: Мини-проект "шифр Цезаря v2" — На вход программе подаётся строка текста на английском языке,
#           в которой нужно зашифровать все слова. Каждое слово строки следует зашифровать с помощью
#           шифра Цезаря (циклического сдвига на длину этого слова). Строчные буквы при этом остаются
#           строчными, а прописные – прописными. Гарантируется, что между различными словами
#           присутствует один пробел.
# ----------------------------

def create_alphabet() -> tuple[list[str], list[str]]:
    low_list: list = [chr(elem) for elem in range(ord('a'), ord('z') + 1)]
    upper_list: list = [chr(elem) for elem in range(ord('A'), ord('Z') + 1)]
    return low_list, upper_list


def get_char(char: str, chars: list, step: int) -> str:
    return chars[(chars.index(char) + step) % len(chars)]


def coder(text: str, low: list, upper: list) -> str:
    new_text: str = ""
    for word in text.split():
        step: int = sum(c.isalpha() for c in word)
        for c in word:
            if c in low:
                new_text += get_char(c, low, step)
            elif c in upper:
                new_text += get_char(c, upper, step)
            else:
                new_text += c
        new_text += " "
    return new_text.strip()


def main() -> None:
    user_text: str = input("Введите шифруемый текст... ")
    low_list, upper_list = create_alphabet()
    print(coder(user_text, low_list, upper_list))


if __name__ == "__main__":
    main()
