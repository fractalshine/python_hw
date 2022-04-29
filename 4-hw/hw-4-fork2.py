from dictionaries import words_easy, words_medium, words_hard, levels  # импортируем словари

words_level = {}
answers = {}


while True:
    level_count = 0
    welcome = input("Выберите уровень сложности:\n"  # приветствие
                    "Легкий, Средний или Сложный\n").lower()

    if welcome == "легкий":
        words_level = words_easy
    elif welcome == "средний":
        words_level = words_medium
    elif welcome == "сложный":
        words_level = words_hard
    else:
        print("Такой сложности, увы, нет")
        exit(0)  # google colab не обрабатывает exit

    print(f'Выбран "{welcome}" уровень сложности, мы предложим вам {len(words_level)}'
          f' слов, подберите перевод')
    input("Нажмите Enter чтобы продолжить...")
    for keys, items in words_level.items():
        print(f'{keys}, {len(items)} букв, начинается на {items[0]}...')
        user_input = input()
        if items in user_input:
            print(f'Верно. {keys.title()} - это {items} ')
            answers.update({keys: True})
            level_count += 1
        else:
            print(f'Неверно. {keys.title()} - это {items}')
            answers.update({keys: False})

    if level_count == 0:
        print("Увы, правильных ответов нет")
        for k, v in answers.items():
            if v is not True:
                print(k)
    elif 0 < level_count < len(levels) - 1:
        print("Правильно отвечены слова")
        for k, v in answers.items():
            if v is True:
                print(k)
        print(f"Неправильно отвечены слова")
        for k, v in answers.items():
            if v is not True:
                print(k)
    elif level_count == len(levels) - 1:
        print("Поздравляем, все слова отгаданы успешно, вот они")
        for k, v in answers.items():
            if v is True:
                print(k)

    print(f"Ваш ранг:\n{levels[level_count]}, это {level_count} баллов")
    replay = input("Ответьте \"Да\" если желаете повторить игру,"
                   " в противном случае программа завершится\n").lower()
    if replay == "да":
        print("Поехали!")
        # continue
    else:
        break

