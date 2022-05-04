from random import shuffle

from question import *
from utils import *


def main():
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
            if question.is_correct():
                answers.append(True)
                score += question.points
            else:
                answers.append(False)
        else:
            continue

    print(print_statistics(answers, score))


if __name__ == "__main__":
    main()
