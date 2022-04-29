import json
import random


def load_questions():
    """Выгружаем вопросы в список из файла"""

    with open('questions.json') as f:
        raw_json = f.read()

    question_list = json.loads(raw_json)

    return question_list


# def random_question():
#     list_questions = load_questions()
#     for s in load_questions():
#         return s['question']


def random_by_num():
    list_ = load_questions()
    n = random.randint(0, len(list_) - 1)
    return list_[n]



