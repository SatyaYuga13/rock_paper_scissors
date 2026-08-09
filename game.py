
# Консольная игра «Камень — Ножницы — Бумага»


import random


# Используем общий набор вариантов, чтобы не повторять их в коде
CHOICES = ("камень", "ножницы", "бумага")


# Компьютер случайно выбирает один из допустимых ходов
def get_computer_choice():
    return random.choice(CHOICES)


# Запрашиваем ход до тех пор, пока пользователь не введёт допустимый вариант.
def get_user_choice():
    while True:
        choice = input(
            "Выберите: камень, ножницы, бумага или выход: "
        ).strip().lower()

        # Команда «выход» позволит завершить игру из основного цикла.
        if choice == "выход":
            return None

        if choice in CHOICES:
            return choice

        print("Ошибка: введите камень, ножницы, бумага или выход.")


def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "Ничья!"

    # Перечисляем только ситуации, в которых выигрывает игрок
    winning_pairs = {
        ("камень", "ножницы"),
        ("ножницы", "бумага"),
        ("бумага", "камень"),
    }

    if (user_choice, computer_choice) in winning_pairs:
        return "Вы победили!"

    return "Победил компьютер!"


# Запуск игры
# Игра продолжается, пока пользователь не введёт команду «выход»
def main():
    print("Добро пожаловать в игру «Камень — Ножницы — Бумага»!")

    while True:
        user_choice = get_user_choice()

        if user_choice is None:
            print("Спасибо за игру!")
            break

        computer_choice = get_computer_choice()

        print(f"\nВы выбрали: {user_choice}")
        print(f"Компьютер выбрал: {computer_choice}")
        print(determine_winner(user_choice, computer_choice))


if __name__ == "__main__":
    # Этот блок запускается только при прямом запуске файла game.py
    main()