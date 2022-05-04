# url = 'https://jsonkeeper.com/b/9ZM4'
import random

import requests


# resp = requests.get('https://jsonkeeper.com/b/9ZM4', params={'method': 'getQuote', 'format': 'json'})
# print(resp.text)
# data = resp.json()
# for s in data:
#     print(s['subwords'])


def load_json():
    """Выгружаем json с вебсайта в список"""

    resp = requests.get('http://95.31.213.27/words.json', params={'method': 'getQuote', 'format': 'json'})
    data = resp.json()
    return data


def random_by_num():
    list_ = load_json()
    n = random.randint(0, len(list_) - 1)
    return list_[n]


print(random_by_num())
