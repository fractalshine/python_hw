from random import choice  # импортируем функцию choice

from data import morse_dict, word_list  # импортируем словари и списки слов для игры

answers = []


def morse_encode(word):
    """Функция кодирования слова в азбуку морзе, которая в качестве аргумента
    получает слово"""

    encoded_word = ""
    for char in word:
        encoded_word += morse_dict[char] + " "
    return encoded_word.rstrip()


def get_word():
    """Функция для получения случайного слова из заданного списка"""

    random_word = choice(word_list)
    return random_word


def print_statistics():
    """Функция для подсчета статистики"""

    total_answers = len(answers)
    right_answers = answers.count(True)
    wrong_answers = answers.count(False)
    return f'Всего задачек: {total_answers}\n' \
           f'Отвечено верно: {right_answers}\n' \
           f'Отвечено неверно: {wrong_answers}'


print("Сегодня мы потренируемся расшифровывать морзянку")
input("Нажмите Enter чтобы продолжить...")

while True:  # бесконечный цикл игры
    print(f'Выберите количество загадываемых слов от 1 до {len(word_list)},'
          f' сейчас в словаре - {len(word_list)} слов')
    user_choice = int(input())
    word_count = 0
    for word in word_list[0:user_choice]:
        '''цикл перебора по списку, ограничитель - пользовательский ввод'''
        word_count += 1
        rand_word = get_word()  # вызываем функцию получения случайного слова
        morse_encode_word = morse_encode(rand_word)  # вызываем функцию кодирования
        print(f"Слово {word_count} - {morse_encode_word}")
        user_input = input().lower()
        if user_input == rand_word:
            print(f'Верно, было загадано {rand_word}\n')
            answers.append(True)
        else:
            print(f'Неверно, загадано {rand_word}\n')
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
