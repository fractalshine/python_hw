words_easy = {
    "family": "семья",
    "hand": "рука",
    "people": "люди",
    "evening": "вечер",
    "minute": "минута",
}

words_medium = {
    "believe": "верить",
    "feel": "чувствовать",
    "make": "делать",
    "open": "открывать",
    "think": "думать",
}

words_hard = {
    "rural": "деревенский",
    "fortune": "удача",
    "exercise": "упражнение",
    "suggest": "предлагать",
    "except": "кроме",
}

levels = {
    0: "Нулевой",
    1: "Так себе",
    2: "Можно лучше",
    3: "Норм",
    4: "Хорошо",
    5: "Отлично",
}
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
        # прерываем - уровень не выбран
        break
        # exit(0)  # google colab не обрабатывает exit

    print(f'Выбран "{welcome}" уровень сложности, мы предложим вам {len(words_level)}'
          f' слов, подберите перевод')
    # пользовательский ввод, готов ли он дальше, переменная user_ready и перевожу в bool
    # user_ready будет пустой если просто нажать Enter, т.е. False
    user_ready = bool(input("Нажмите Enter чтобы продолжить..."))

    if not user_ready:
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
        # Не забываем остановить цикл, конец игры
        # break
    else:
        # Уведомляем пользователя, что игра закончена
        print('Вы закончили игру')
        break
