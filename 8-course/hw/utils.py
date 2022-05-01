import json
import random


def load_questions():
    """Выгружаем вопросы в список из файла"""

    with open('questions.json') as f:
        raw_json = f.read()

    question_list = json.loads(raw_json)

    return question_list


def random_by_num():
    list_ = load_questions()
    n = random.randint(0, len(list_) - 1)
    return list_[n]


def print_statistics(answers, score):
    total_answers = len(answers)
    right_answers = answers.count(True)
    return f'Вот и все\n' \
           f'Отвечено верно {right_answers} вопроса из {total_answers}\n' \
           f'Набрано баллов: {score}'
