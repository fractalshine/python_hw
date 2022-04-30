from question import *
from utils import *
from random import shuffle

questions = []

q_dicts_list = load_questions()
for q in q_dicts_list:
    questions.append(Question(q['question'], q['answer'], q['difficulty']))

shuffle(questions)

for question in questions:
    if not question.is_asked:
        print(question.build_question())
        question.is_asked = True
        question.user_answer = input()
        question.build_feedback()
    else:
        continue

# print(questions)
# rand_dict = random_by_num()
# for q in q_dicts_list:
#     rand_dict = random_by_num()
#
#     q1 = Question(rand_dict['question'], rand_dict['answer'], rand_dict['difficulty'])
#
#     print(q1.build_question())


