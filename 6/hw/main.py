import random


def word_jumble(word):
    """Функция перемешивания слов"""

    chars_list = list(word)
    random.shuffle(chars_list)
    return ''.join(chars_list)


def read_top():
    """Функция чтения топа и выдачи результатов"""

    with open('top.txt') as f:
        total_games = 0
        max_score = 0
        top_user = ''
        for line in f:
            total_games += 1
            user, score = line.split(':')
            int_score = int(score)
            if int_score > max_score:
                max_score = int_score
                top_user = user
    return f'Лучший результат у игрока {top_user} со счетом {max_score}\n' \
           f'Всего игр - {total_games}'


def write_top(name, score):
    """Функция записи в топ счета и имени"""

    with open('top.txt', 'a') as f:
        f.write(f"{name}:{score}\n")


username = input("Введите ваше имя\n")
user_score = 0

with open('words.txt') as file:
    for word in file:  # цикл перебора слов из файла построчно
        clear_word = word.rstrip()
        jumble_word = word_jumble(clear_word)
        print(f"Угадайте слово: {jumble_word}")
        user_input = input().lower()
        if user_input == clear_word:
            print("Верно, вы получаете 10 очков")
            user_score += 10
        else:
            print(f"Неверно! Верный ответ - {clear_word}")

write_top(username, user_score)
print(read_top())
