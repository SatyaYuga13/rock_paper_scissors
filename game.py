
# Консольная игра «Камень — Ножницы — Бумага»


import random
import json


# Используем общий набор вариантов, чтобы не повторять их в коде
CHOICES = ("камень", "ножницы", "бумага")


class ScoreBoard:
    # При создании нового счётчика обе стороны начинают с нуля
    def __init__(self):
        self.player_wins = 0
        self.computer_wins = 0

    def update_score(self, winner):
        """Обновляет счёт после завершения раунда."""
        if winner == "player":
            self.player_wins += 1
        elif winner == "computer":
            self.computer_wins += 1

    def display_score(self):
        """Выводит текущий счёт в консоль."""
        print(
            f"Счёт — игрок: {self.player_wins}, "
            f"компьютер: {self.computer_wins}"
        )

    def save_results(self):
        """Сохраняет текущий счёт в файл scores.json."""
        scores = {
            "Победы игрока": self.player_wins,
            "Победы компьютера": self.computer_wins,
        }

        with open("scores.json", "w", encoding="utf-8") as file:
            json.dump(scores, file, ensure_ascii=False, indent=4)


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
        return "draw"

    # Перечисляем ситуации, в которых выигрывает игрок
    winning_pairs = {
        ("камень", "ножницы"),
        ("ножницы", "бумага"),
        ("бумага", "камень"),
    }

    if (user_choice, computer_choice) in winning_pairs:
        return "player"

    return "computer"


# Запуск игры
# Игра продолжается, пока пользователь не введёт команду «выход»
def main():
    print("Добро пожаловать в игру «Камень — Ножницы — Бумага»!")

    scoreboard = ScoreBoard()
    messages = {
        "player": "Вы победили!",
        "computer": "Победил компьютер!",
        "draw": "Ничья!",
    }

    while True:
        user_choice = get_user_choice()

        if user_choice is None:
            scoreboard.save_results()
            print("Результаты сохранены в файле scores.json.")
            print("Спасибо за игру!")
            break

        computer_choice = get_computer_choice()
        winner = determine_winner(user_choice, computer_choice)

        print(f"\nВы выбрали: {user_choice}")
        print(f"Компьютер выбрал: {computer_choice}")
        print(messages[winner])

        scoreboard.update_score(winner)
        scoreboard.display_score()


if __name__ == "__main__":
    # Этот блок запускается только при прямом запуске файла game.py
    main()