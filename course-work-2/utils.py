import random

import requests

from basicword import BasicWord


def load_json():
    """Выгружаем json с вебсайта в список"""

    resp = requests.get('http://95.31.213.27/words_v2.json', params={'method': 'getQuote', 'format': 'json'})
    data = resp.json()
    return data


def random_by_num():
    """Возвращает случайный словарь из списка словарей"""

    list_of_dicts = load_json()
    n = random.randint(0, len(list_of_dicts) - 1)
    return list_of_dicts[n]


def load_random_word():
    """Возвращает экземпляр со словом и списком подслов"""

    rand_word = random_by_num()
    bw = BasicWord(rand_word['word'], rand_word['subwords'])
    return bw
