from random import shuffle

from question import *
from utils import *

questions = []
answers = []
score = 0

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
        # answers.append(question.is_correct())
        if question.is_correct():
            answers.append(True)
            score += question.points
        else:
            answers.append(False)

    else:
        continue

print(print_statistics(answers, score))

# rand_dict = random_by_num()
# for q in q_dicts_list:
#     rand_dict = random_by_num()
#
#     q1 = Question(rand_dict['question'], rand_dict['answer'], rand_dict['difficulty'])
#
#     print(q1.build_question())
