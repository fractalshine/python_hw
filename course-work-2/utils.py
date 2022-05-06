# url = 'https://jsonkeeper.com/b/9ZM4'
import random

import requests

from basicword import BasicWord


def load_json():
    """Выгружаем json с вебсайта в список"""

    resp = requests.get('http://95.31.213.27/words_v2.json', params={'method': 'getQuote', 'format': 'json'})
    data = resp.json()
    return data


def random_by_num():
    list_ = load_json()
    n = random.randint(0, len(list_) - 1)
    return list_[n]


def load_random_word():
    rand_word = random_by_num()
    bw = BasicWord(rand_word['word'], rand_word['subwords'])
    return bw


# print(load_random_word())
