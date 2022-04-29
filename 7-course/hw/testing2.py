from utils import *


pk_student_input = int(input("Введите номер студента\n"))

try:
    get_student_by_pk(pk_student_input)
except IndexError:
    print("Такого студента нет")
    quit(0)

student_dict = get_student_by_pk(pk_student_input)
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
