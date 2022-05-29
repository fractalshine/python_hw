import json


def load_candidates():
    """Выгружаем кандидатов в список из файла"""

    with open('candidates.json') as f:
        raw_json = f.read()

    candidates_list = json.loads(raw_json)

    return candidates_list

