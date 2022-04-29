from random import choice  # импортируем функцию choice

from data import morse_dict, word_list  # импортируем словари и списки слов для игры

answers = []


def morse_encode(word):
    encoded_word = ""
    for char in word:
        encoded_word += morse_dict[char] + " "
    return encoded_word.rstrip()


def get_word():  # функция для получения случайного слова из заданного списка
    random_word = choice(word_list)
    return random_word


def print_statistics():
    total_answers = len(answers)
    right_answers = answers.count(True)
    wrong_answers = answers.count(False)
    return f'Всего задачек: {total_answers}\n' \
           f'Отвечено верно: {right_answers}\n' \
           f'Отвечено неверно: {wrong_answers}'


print("Сегодня мы потренируемся расшифровывать морзянку")
input("Нажмите Enter чтобы продолжить...")

while True:
    word_count = 0
    for word in word_list:
        word_count += 1
        rand_word = get_word()
        morse_encode_word = morse_encode(rand_word)
        print(f"Слово {word_count} - {morse_encode_word}")
        user_input = input().lower()
        if user_input == rand_word:
            print(f'Верно, было загадано {rand_word}')
            answers.append(True)
        else:
            print(f'Неверно, загадано {rand_word}')
            answers.append(False)
    print(print_statistics())
    replay = input("Ответьте \"Да\" если желаете повторить игру,"
                   " в противном случае игра завершится\n").lower()
    if replay == "да":
        answers.clear()
        print("Поехали!")
        # continue
    else:
        break


# print(morse_encode(get_word()))
# print(print_statistics())
