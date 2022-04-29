import json


def load_professions():
    """Выгружаем профессии в список из файла"""

    with open('professions.json') as f:
        raw_json = f.read()

    professions_list = json.loads(raw_json)

    return professions_list


def load_students():
    """Выгружаем студентов в список из файла"""

    with open('students.json') as f:
        raw_json = f.read()

    students_list = json.loads(raw_json)

    return students_list


def get_student_by_pk(pk):
    """Получаем словарь информации о студенте по ключу"""

    return load_students()[pk - 1]


def get_profession_by_title(title):
    """Получаем словарь профессий по названию профы"""

    for s in load_professions():
        if s['title'] == title:
            return s


def check_fitness(student, profession):
    """Формируем словарь из имеющихся скиллов студента и разницы множеств"""

    student_skill_set = set(get_student_by_pk(student)['skills'])
    required_skill_set = set(get_profession_by_title(profession)['skills'])
    skills_he_lacks = required_skill_set.difference(student_skill_set)
    relevant_skills = student_skill_set.intersection(required_skill_set)
    skills_he_has_list = list(student_skill_set)
    skills_he_lacks_list = list(skills_he_lacks)
    skills_relevant_list = list(relevant_skills)
    len_relevant = len(relevant_skills)
    len_req = len(required_skill_set)
    fit_percent = round(len_relevant / len_req * 100)
    fitness_dict = {"has": skills_he_has_list,
                    "lacks": skills_he_lacks_list,
                    "relevant": skills_relevant_list,
                    "fit_percent": fit_percent
                    }
    return fitness_dict
