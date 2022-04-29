# initial data and variables
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

words = {}

levels = {
    0: "Нулевой",
    1: "Так себе",
    2: "Можно лучше",
    3: "Норм",
    4: "Хорошо",
    5: "Отлично",
}

answers = {}
true_answers = 0

# user input
user_input = input("Выберите уровень сложности.\nЛегкий, средний, сложный.\n")
user_input = user_input.lower()

# level selection
if user_input == 'легкий':
    words = words_easy
if user_input == 'средний':
    words = words_medium
if user_input == 'сложный':
    words = words_hard

# level selected
if words:
    print(f'Выбран {user_input} уровень сложности.')

    for k, v in words.items():

        current_word = k
        len_word = len(v)
        first_char_word = v[:1]

        user_ready = bool(input('Нажмите enter\n'))

        if not user_ready:
            # we find the end of the word
            remainder = len_word + 10 % 10

            if remainder == 1:
                word_ending = 'а'
            elif 1 < remainder < 5:
                word_ending = 'ы'
            else:
                word_ending = ''
            # we receive a response from the user
            answer = input(f'{current_word}, {len_word} букв{word_ending},'
                           f' начинается на {first_char_word}...\n')
            answer = answer.lower()

            current_word = current_word.title()

            if answer == v:
                print(f'Верно, {current_word} — это {v}.')
                answers[current_word] = True
            else:
                print(f'Неверно, {current_word} — это {v}.')
                answers[current_word] = False
        else:

            user_exit = input('Вы хотите играть? Напишете да или нет.\n')

            if user_exit == 'да':
                continue
            else:
                break

    print('Правильно отвечены слова:')

    for a in answers.items():
        if a[1]:
            true_answers += 1
            print(a[0])

    print('Неправильно отвечены слова:')

    for a in answers.items():
        if not a[1]:
            print(a[0])

    print(f'Ваш ранг: {levels[true_answers]}')

# the level is not selected
else:
    print('Вы не выбрали уровень сложности. Запустите программу заново.')