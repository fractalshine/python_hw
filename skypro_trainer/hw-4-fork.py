import os
import sys

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
level_count = 0

welcome = input("Выберите уровень сложности:\n"  # приветствие
                     "Легкий, Средний или Сложный\n")

if welcome == "легкий":
    words_level = words_easy
elif welcome == "средний":
    words_level = words_medium
elif welcome == "сложный":
    words_level = words_hard
else:
    print("Goodbye")
    os._exit(0)
    #     exit(0)

print(f'Выбран уровень сложности, мы предложим вам {len(words_level)}'
      f' слов, подберите перевод')
input("Нажмите Enter чтобы продолжить...")
for keys, items in words_level.items():
    print(f'{keys}, {len(items)} букв, начинается на {items[0]}...')
    user_input = input()
    if items in user_input:
        print(f'Верно, {keys} - это {items} ')
        answers.update({keys: True})
    else:
        print(f'Неверно, {keys} - это {items}')
        answers.update({keys: False})

print("Правильно отвечены слова")
for k, v in answers.items():
    if v is True:
        level_count += 1
        print(k)
print(f"Неправильно отвечены слова")
for k, v in answers.items():
    if v is not True:
        print(k)

print(f'Ваш ранг:\n{levels[level_count]}, это {level_count} баллов')
