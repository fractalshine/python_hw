order = [
    {"skolko": 5.0, "poroda": "тунец", "sred_razmer": 300},
    {"skolko": 15.0, "poroda": "окунь", "sred_razmer": 250},
    {"skolko": 20.0, "poroda": "щука", "sred_razmer": 460},
]
order_converted = []

for dict_line in order:
    count = round(dict_line['skolko'])
    specie = dict_line['poroda'].title()
    avg_size = dict_line['sred_razmer'] // 10
    new_order = {"count": count, "specie": specie, "avg_size": avg_size}
    order_converted.append(new_order)




# Не удаляйте текст ниже, он нужен для проверки

for item in order_converted:
    for key, value in item.items():
        print(key, value)
