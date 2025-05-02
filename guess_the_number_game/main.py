from random import randint


def is_valid(user_input: str, max_num: int = None) -> bool:
    if not user_input.isdigit():
        return False
    if max_num != None:
        return 1 <= int(user_input) <= max_num
    else:
        return int(user_input) > 1


def play_again():
    user_choice: str = input("Хотите сыграть еще раз? ('д' - Да / любое другое - Нет)")
    return user_choice.lower() == 'д'


def new_game() -> tuple[str, int, int, int]:
    print("Начинаем игру 'Угадай число'")
    user_name = input("Введите свое имя: ")
    count = 0
    max_num = input("Установите верхнюю границу от 1 до ..: ")
    while not is_valid(max_num):
        print("Вы ввели некорректное значение! Попробуем еще раз...")
        max_num = input("Установите верхнюю границу от 1 до ..: ")
    max_num = int(max_num)
    hidden_number = randint(1, max_num)

    return user_name, count, max_num, hidden_number


def game(user_name: str, count: int, max_num: int, hidden_number: int) -> None:
    while True:
        count += 1
        # print("Введите число: ", end="")
        guess: str = input("Введите число: ")
        if not is_valid(guess, max_num):
            continue
        guess = int(guess)

        if guess > hidden_number:
            print("Ваше число больше загаданного, попробуйте еще разок")
        elif guess < hidden_number:
            print("Ваше число меньше загаданного, попробуйте еще разок")
        else:
            print(f"Поздравляю {user_name}! Ты победил!!!\n"
                  f"Использовал попыток {count}")
            break


def main() -> None:
    count: int = 0
    in_game: bool = True
    max_num: int = 100
    user_name: str = ""
    hidden_number: int = 0

    while in_game:
        user_name, count, max_num, hidden_number = new_game()
        game(user_name, count, max_num, hidden_number)
        in_game = play_again()

    print(f"{user_name} отлично поиграли. До встречи...")


if __name__ == "__main__":
    main()
