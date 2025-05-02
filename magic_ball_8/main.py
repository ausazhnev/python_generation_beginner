# ----------------------------
# Разработчик: Andrey Sazhnev (dikey)
# Email: ausazhnev@gmail.com
# GitHub: https://github.com/ausazhnev
# Telegram: @ausazhnev
# Описание: Мини-проект "Магический шар 8" — программа для шуточного предсказания будущего.
#           Пользователь задает вопрос, а программа случайным образом отвечает на него.
# ----------------------------

from random import choice
from time import sleep


def again() -> bool:
    user_choice: str = input("Хочешь задать еще один вопрос? ('д' - Да / иначе - 'Нет')")
    return user_choice.lower() in ['д', 'да']


def response_output(answers: list) -> None:
    print(choice(answers))


def main(answers: list) -> None:

    is_again: bool = True

    print("Привет, я магический шар...")
    user_name: str = input("Как тебя зовут? ")
    print(f"Привет, {user_name}")

    while is_again:
        input("Задай свой вопрос...")
        sleep(1)
        print("Судьба уже близко")
        sleep(2)
        response_output(answers)
        sleep(1)
        is_again = again()

    print(f"Буду ждать твоего возвращения, {user_name}")


if __name__ == "__main__":
    ANSWERS: list = ["Бесспорно", "Предрешено", "Никаких сомнений", "Определённо да",
                     "Можешь быть уверен в этом", "Мне кажется - да", "Вероятнее всего",
                     "Хорошие перспективы", "Знаки говорят - да", "Да", "Пока неясно, попробуй снова",
                     "Спроси позже", "Лучше не рассказывать", "Сейчас нельзя предсказать",
                     "Сконцентрируйся и спроси опять", "Даже не думай", "Мой ответ - нет",
                     "По моим данным - нет", "Перспективы не очень хорошие", "Весьма сомнительно"]
    main(ANSWERS)
