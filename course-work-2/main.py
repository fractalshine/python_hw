from utils import *
from player import Player


def main():
    username = input("Введите имя игрока")

    player = Player(username)

    rand_word = load_random_word()
    print(f"Приветствую тебя {player.username}")
    print(f"Составьте {rand_word.get_len()} слов из слова {rand_word.initial_word}\n"
          f"чтобы остановить игру набери слово \"stop\"")
    print("Поехали, ваше первое слово?")
    for word in rand_word.subwords:
        user_input = input()
        if user_input in player.used_words:
            print(f"слово \"{user_input}\" уже использовалось")
            continue
        elif rand_word.is_correct(user_input):
            print("Верно, такое слово существует")
            player.add_used_word(user_input)
            print(player.used_words)
        elif user_input == "stop":
            print(f"Пока, ты отгадал {len(player.used_words)} слов.")
            quit(0)
        else:
            print("Такого слова в списке нет, увы")

    print(f"Слова закончились, игра завершена!\n"
          f"Вы отгадали {len(player.used_words)} слов!")


if __name__ == "__main__":
    main()