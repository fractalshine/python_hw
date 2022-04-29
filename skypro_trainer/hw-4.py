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

answers = {}

words_level = {}

welcome = input("Выберите уровень сложности:\n"
                "Легкий, Средний или Сложный\n")

if welcome == "легкий":
    words_level.update({welcome: words_easy})
elif welcome == "средний":
    words_level.update({welcome: words_easy})
elif welcome == "сложный":
    words_easy.update({welcome: words_easy})

for keys in words_level:
    # print(f'это ключ -', keys)
    # print("это значение", words_level[keys])
    for k, v in words_level[keys].items():
        print(k, len(v))
        user_input = input()
        if v in user_input:
            print("Верно")
        else:
            print("Неверно")



# print(words_level[welcome]["rural"])
