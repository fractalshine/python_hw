from utils import *
from player import Player
from basicword import BasicWord

# print(load_random_word())

username = input("Ввведите имя игрока")

player = Player(username)

rand_word = load_random_word()
print(f"Приветствую тебя {player.username}")
print(f"Составьте {rand_word.get_len()} слов из слова {rand_word.initial_word}\n"
      f"чтобы остановить игру набери слово \"stop\"")
print("Поехали, ваше первое слово?")
for word in rand_word.subwords:
    user_input = input()

    if rand_word.is_correct(user_input):
        print("right")
        player.add_used_word(user_input)
    elif user_input == "stop":
        print(f"Пока, ты отгадал {len(player.used_words)} слов.")
        quit(0)
    else:
        print("wrong")

print(f"Слова закончились, игра завершена!\n"
      f"Вы отгадали {len(player.used_words)} слов!")
