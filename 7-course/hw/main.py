from utils import *


def is_pk_in_db():
    while True:
        try:
            user_input = int(input("Введите номер студента\n"))
        except ValueError:
            print("Вы ввели не число, повторите ввод")
            continue
        else:
            user_input = user_input
        try:
            student_dict = get_student_by_pk(user_input)
        except IndexError:
            user_input = input("Такого студента нет, желаете повторить поиск?((Y)es/(N)o)\n").lower()
            if user_input == "y":
                continue
            else:
                quit(0)
        else:
            return student_dict, user_input


student_dict, pk_student_input = is_pk_in_db()

student = student_dict['full_name']
student_skills = student_dict['skills']

print(f'Студент {student}\n'
      f'Знает: {", ".join(student_skills)}')

ask_profession = input(f"выберите специальность для оценки студента {student}\n").title()

try:
    check_fitness(pk_student_input, ask_profession)
except TypeError:
    print("Такой профы нет")
    quit(0)

fitness_dict = check_fitness(pk_student_input, ask_profession)
if len(fitness_dict['relevant']) != 0:
    relevant_skills = ", ".join(fitness_dict['relevant'])
else:
    relevant_skills = "нет подходящих навыков"
lacks_skills = ", ".join(fitness_dict['lacks'])
fit_percent = fitness_dict['fit_percent']
print(f'Пригодность {fit_percent}\n'
      f'{student} знает: {relevant_skills}\n'
      f'{student} не знает: {lacks_skills}')
