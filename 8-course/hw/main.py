from question import *
from utils import *

questions = []

q_dicts_list = load_questions()
for q in q_dicts_list:
    questions.append(Question(q['question'], q['answer'], q['difficulty']))


for question in questions:
    print(question.ask())
# print(questions)
# rand_dict = random_by_num()
# for q in q_dicts_list:
#     rand_dict = random_by_num()
#
#     q1 = Question(rand_dict['question'], rand_dict['answer'], rand_dict['difficulty'])
#
#     print(q1.build_question())


# # questions = [
# #     Question(q_dicts_list[0]['question'], q_dicts_list[0]['answer'], q_dicts_list[0]['difficulty']),
# #     Question(q_dicts_list[1]['question'], q_dicts_list[1]['answer'], q_dicts_list[1]['difficulty']),
# #     Question(q_dicts_list[2]['question'], q_dicts_list[2]['answer'], q_dicts_list[2]['difficulty']),
# #     Question(q_dicts_list[3]['question'], q_dicts_list[3]['answer'], q_dicts_list[3]['difficulty'])
# # ]
# for q in questions:
#     print(q.build_question())
