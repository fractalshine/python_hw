import json


def load_candidates_from_json():
    """Выгружаем кандидатов в список из файла"""

    with open('candidates.json', "r", encoding='utf-8') as f:
        candidates_list = json.load(f)

    return candidates_list


def get_candidates_by_name(candidate):
    """Получаем кандидата по имени"""

    candidates_list = load_candidates_from_json()
    candidate_lower = candidate.lower()
    names_list = []

    for dictionary in candidates_list:
        candidate_string_lower = dictionary['name'].lower()
        if candidate_lower in candidate_string_lower:
            names_list.append(dictionary)
            continue
    return names_list


def get_candidates_by_skill(skill_name):
    """"Получаем список словарей кандидатов по навыку"""

    dict_list = load_candidates_from_json()
    skill_name_lower = skill_name.lower()
    skilled_list = []

    for dictionary in dict_list:
        skill = dictionary['skills'].strip().lower().split(', ')
        if skill_name_lower in skill:
            skilled_list.append(dictionary)
            continue
    return skilled_list


def get_candidate(pk):
    """Получаем словарь кандидатов по айди"""

    dict_list = load_candidates_from_json()

    for dictionary in dict_list:
        if dictionary['id'] == pk:
            return dictionary


print(get_candidates_by_name("sheree"))
