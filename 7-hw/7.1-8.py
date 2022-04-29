employees = [

    {"fio": "Киселёв Всеволод Эдуардович ", "vaccinated": True},
    {"fio": "Довлатова Эмилия Ефимовна", "vaccinated": False},
    {"fio": "Аверин Мартын Егорович", "vaccinated": True},
    {"fio": "Князева Августа Егоровна", "vaccinated": False},
    {"fio": "Шанская Аграфена Семеновна", "vaccinated": True},
    {"fio": "Куприна Марина Викторовна", "vaccinated": False},
    {"fio": "Селезнев Константин Игоревич", "vaccinated": False},
]

vaccinated = []
not_vaccinated = []

for line in employees:
    if line['vaccinated']:
        vaccinated.append(line['fio'])
    else:
        not_vaccinated.append(line['fio'])
print("Вакцинированные")
print('\n'.join(vaccinated))
print("Остальные")
print('\n'.join(not_vaccinated))
