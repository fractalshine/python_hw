species = [
    {"specie": "Лещ", "len": "29", "sea": False, "desc": "Единственный представитель рода лещей из семейства карповых."},
    {"specie": "Щука", "len": "45", "sea": False, "desc": "Распространена в пресных водах Евразии и Северной Америки. Живёт обычно в прибрежной зоне, в водных зарослях, в непроточных или слабопроточных водах. "},
    {"specie": "Треска", "len": "33", "sea": True, "desc": "Треска встречается от прибрежной полосы до континентального шельфа, но в открытом море над большими глубинами редко. Её жизненный цикл привязан к морским течениям Северной Атлантики."},
    {"specie": "Камбала", "len": "25", "sea": True, "desc": " Тело плоское, сильно сжато с боков, глаза расположены не по бокам головы, а смещены на одну её сторону. Плавательного пузыря нет. "},
    {"specie": "Лосось", "len": "50", "sea": False, "desc": "Проходная форма обитает в северной части Атлантического океана. Заходит на нерест в реки от Португалии и Испании до Баренцева моря."},
]

s = input()

# list_of_all_values = [value for elem in species
#                       for value in elem.values()]

for line in species:
    if s == line['specie'] and line['sea']:
        print(f"{line['specie']}: {line['desc']}\n"
              f"Морская рыба\n"
              f"Промысловый размер: {line['len']}")
        break
    elif s == line['specie'] and not line['sea']:
        print(f"{line['specie']}: {line['desc']}\n"
              f"Пресноводная рыба\n"
              f"Промысловый размер: {line['len']} см")
        break
else:
    print("Информация не найдена")

# if s not in list_of_all_values:
#     print("Информация не найдена")