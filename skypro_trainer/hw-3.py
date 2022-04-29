questions = ["My name ___ Vova", "I ___ a coder", "I live ___ Moscow", "It's ___ you"]
answers = ["is", "am", "in", "for"]
score = 0  # счетчик баллов
right_answer_total = 0  # счетчик верных ответов

welcome = input("Привет! Предлагаю проверить свои знания английского! Набери \"ready\" чтобы начать!\n")

if welcome == "ready":
    for i in range(len(questions)):
        question_1 = input(f"Заполни пробел в предложении верно: {questions[i]}\n"  # начало блока  вопроса
                           "Твой ответ: ")
        if question_1 == answers[i]:
            print("Ответ верный\nВы получаете 10 баллов!")
            score += 10
            right_answer_total += 1
            continue
        else:
            print(f"Неправильно. Правильный ответ: {answers[i]}")
            continue

    percentage = int(right_answer_total / len(questions) * 100)  # считаем процент

    if 2 <= right_answer_total <= 4:  # работаем с окончаниями
        ending1 = "вопроса"
    else:
        ending1 = "вопрос"

    if percentage == 33:
        ending2 = "процента"
    else:
        ending2 = "процентов"

    print(f"Вот и все!\n"
          f"Вы ответили на верно на {right_answer_total} {ending1} из {len(questions)}.\n"
          f"Вы заработали {score} баллов.\n"
          f"Это {percentage} {ending2}")

else:
    print("Кажется, вы не хотите играть. Очень жаль")

